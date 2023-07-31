#/////////////////////////////////////////////////////////////////////#
#                            TO DO LIST :                             #
#                                                                     #
#/////////////////////////////////////////////////////////////////////#

from scripts.variables import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((SENDER_IP, SENDER_PORT))

if os.path.exists(file_path):
    file = open(file_path, 'r')
    file_data = file.read()
    try:
        registeredUsers = json.loads(file_data)
    except json.JSONDecodeError:
        pass
    items = list(registeredUsers.items())
    if registeredUsers != {}:
        receiverNames = [value for _, value in items]
        receiverIPs = [key for key, _ in items]
    if debugging:
        print(f"\nCurrent IPs  : {receiverIPs},\nCurrent Names: {receiverNames},\nCurrent Items: {items}")
        
class MainWindows(QMainWindow):
    closed = pyqtSignal()
    
    def __init__(self):
        global registeredUsers, receiverNames, receiverIPs
        super(MainWindows, self).__init__()
        uic.loadUi('chatBox\scripts\chatBox.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.sendingButton.clicked.connect(self.sendButton)
        self.clearScreenButton.clicked.connect(self.clearListWidget)
        self.addReceiverButton.clicked.connect(self.addUser)
        self.registeredUserList.currentIndexChanged.connect(self.selectionChange)
        self.eraseTextFileButton.clicked.connect(self.clearSAVEDFILE)
        self.removeSelectedButton.clicked.connect(self.rmSelRegUser)
        self.saveCurrentListButton.clicked.connect(self.saveCurrentRegUsers)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        if len(receiverIPs) != 0 and len(receiverNames) != 0: 
            self.receiverName_Input.setText(receiverNames[0])
            self.receiverIP_Input.setText(receiverIPs[0])
        
        self.names_count = {}
        
        self.userList = self.registeredUserList
        self.userList.addItems(receiverNames)

    def update(self):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            message = data.decode()
            if debugging:
                print(f"---\nMessage Received : {message}")
            if registeredUsers[server[0]] != "":
                self.listWidget.insertItem(0, f"[From {registeredUsers[server[0]]}] : {message}")
            else:
                self.listWidget.insertItem(0, f"[From [Unknown User] : {message}")
            self.listWidget.item(0).setForeground(QtCore.Qt.white)


    def sendButton(self):
        SENDER_IP = "127.0.0.1"
        
        if self.receiverIP_Input.text().strip() != "":
            receiverName = self.receiverName_Input.text().strip()
            RECEIVER_IP = self.receiverIP_Input.text()
        else:
            RECEIVER_IP = "127.0.0.1"
            receiverName = ""

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = self.yourMessage_Input.text().strip()
        data = message.encode("Utf8")
        if debugging:
            print(f"---\nMessage sent: \"{message}\" \nReceiver's IP: {RECEIVER_IP} ({receiverName}) \nReceiver's Port : {RECEIVER_PORT}") 
        sock.sendto(data, (RECEIVER_IP, RECEIVER_PORT))

    def clearListWidget(self):
        self.listWidget.clear()

    def addUser(self):
        global registeredUsers, receiverNames, receiverIPs, name_bis

        receiverName = self.receiverName_Input.text().strip()
        RECEIVER_IP = self.receiverIP_Input.text().strip()
        if not (receiverName in receiverNames and RECEIVER_IP in receiverIPs):
            if receiverName:
                if receiverName in receiverNames:
                    count = self.names_count.get(receiverName, 0) + 1
                    self.names_count[receiverName] = count
                    if debugging:
                        print(self.names_count)
                    modified_name = f"{receiverName}_{count}"
                    name_bis.append(modified_name)
                    registeredUsers[RECEIVER_IP] = modified_name
                else:
                    registeredUsers[RECEIVER_IP] = receiverName

            self.userList.addItem(receiverName)

            receiverNames.append(str(receiverName))
            receiverIPs.append(str(RECEIVER_IP))
        
    def selectionChange(self):
        global registeredUsers, receiverNames, receiverIPs    
        currentIndex = self.userList.currentIndex()
        
        if len(receiverIPs) != 0 and len(receiverNames) != 0: 
            self.receiverName_Input.setText(str(receiverNames[currentIndex]))
            self.receiverIP_Input.setText(str(receiverIPs[currentIndex]))
        else:
            pass
        
    def clearSAVEDFILE(self):
        global file_path, items, receiverIPs, receiverNames, registeredUsers, name_bis
        
        items.clear()
        receiverIPs.clear()
        receiverNames.clear()
        registeredUsers.clear()
        name_bis.clear()
        
        self.names_count.clear()
        
        self.userList.clear()
        
        if os.path.exists(file_path):
            file = open(file_path, 'w')
            file.truncate(0)
            print("Registered Users and File content have been deleted.")
            file.write("{}")
        else:
            print("file does not exist")
            
    def rmSelRegUser(self):
        global receiverIPs, receiverNames, registeredUsers, items
        
        currentIndex = self.userList.currentIndex()
        self.userList.removeItem(currentIndex)
        print(currentIndex)
        
        removedItem = items.pop(currentIndex)
        removedIP = receiverIPs.pop(currentIndex)
        removedName = receiverNames.pop(currentIndex)
        
        if debugging:
            print(f"Removed Item: {removedItem} | Removed IP: {removedIP} | Removed Name: {removedName}\n\n----")
            print(f"\nCurrent IPs  : {receiverIPs},\nCurrent Names: {receiverNames},\nCurrent Items: {items}")
        
    def saveCurrentRegUsers(self):
        global receiverIPs, receiverNames, registeredUsers, items
        
        registeredUsers.clear()
        formatted_data = {ip: name for ip, name in items}
        registeredUsers.update(formatted_data)
        
        
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

def on_window_closed():
    file = open(file_path, "w")
    json.dump(registeredUsers, file)
    file.close()

app = QApplication(sys.argv)
window = MainWindows()
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window.closed.connect(on_window_closed)

app.exec_()