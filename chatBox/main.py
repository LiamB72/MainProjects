# Program entirely made by me, had to scroll throu a lot and a lot of stack overflow stuff and what not programming&debuggin' sites to find the right solution and used a bit of the forbidden one too :p

from scripts.variables import *

if os.path.exists(file_path):
    file = open(file_path, 'r')
    file_data = file.read()
    try:
        registeredUsers = json.loads(file_data)
    except json.JSONDecodeError:
        pass
    items = list(registeredUsers.items())
    if registeredUsers != {}:
        receiverNames = [key for key, _ in items]
        receiverIPs = [value for _, value in items]
    #print(items, receiverNames, receiverIPs)
    

class MainWindows(QMainWindow):
    closed = pyqtSignal()
    
    def __init__(self):
        global registeredUsers, receiverNames, receiverIPs
        super(MainWindows, self).__init__()
        uic.loadUi('scripts\chatBox.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.sendingButton.clicked.connect(self.sendButton)
        self.pushClearButton.clicked.connect(self.clearListWidget)
        self.addUserButton.clicked.connect(self.addUser)
        self.registeredUserList.currentIndexChanged.connect(self.selectionChange)
        self.clearSAVEFILE.clicked.connect(self.clearSAVEDFILE)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        if len(receiverIPs) != 0 and len(receiverNames) != 0: 
            self.receiverName_Text.setText(receiverNames[0])
            self.receiverIP_Text.setText(receiverIPs[0])
        else:
            pass
        
        self.names_count = {}
        
        userList = self.registeredUserList
        userList.addItems(receiverNames)

    def update(self):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            message = data.decode()
            self.listWidget.insertItem(0, message)
            self.listWidget.item(0).setForeground(QtCore.Qt.white)


    def sendButton(self):
        
        if self.receiverIP_Text.text().strip() != "":
            RECEIVER_IP = self.receiverIP_Text.text().strip()
        else:
            RECEIVER_IP = "127.0.0.1"

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = self.messageToSend.text().strip()
        octets = message.encode("Utf8")
        print("Message sent:",message,"To:",RECEIVER_IP)
        sock.sendto(octets, (RECEIVER_IP, RECEIVER_PORT))

    def clearListWidget(self):
        self.listWidget.clear()

    def addUser(self):
        global registeredUsers, receiverNames, receiverIPs, name_bis
        userList = self.registeredUserList
        currentIndex = userList.currentIndex()

        receiverName = self.receiverName_Text.text().strip()
        RECEIVER_IP = self.receiverIP_Text.text().strip()
        if not (receiverName in receiverNames and RECEIVER_IP in receiverIPs):
            if receiverName:
                if receiverName in receiverNames:
                    count = self.names_count.get(receiverName, 0) + 1
                    self.names_count[receiverName] = count
                    print(self.names_count)
                    modified_name = f"{receiverName}_{count}"
                    name_bis.append(modified_name)
                    registeredUsers[modified_name] = RECEIVER_IP
                else:
                    registeredUsers[receiverName] = RECEIVER_IP

            userList.addItem(receiverName)

            receiverNames.append(str(receiverName)) # Append to the global variable
            receiverIPs.append(str(RECEIVER_IP))
        
    def selectionChange(self):
        global registeredUsers, receiverNames, receiverIPs
        userList = self.registeredUserList    
        currentIndex = userList.currentIndex()
        
        if len(receiverIPs) != 0 and len(receiverNames) != 0: 
            self.receiverName_Text.setText(str(receiverNames[currentIndex]))
            self.receiverIP_Text.setText(str(receiverIPs[currentIndex]))
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
        

        userList = self.registeredUserList
        userList.clear()
        
        if os.path.exists(file_path):
            file = open(file_path, 'w')
            file.truncate(0)
            print("Registered Users and File content have been deleted.")
            file.write("{}")
        else:
            print("file does not exist")
        
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
