#Chat texte en UDP sans QUdpSocket

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui,uic
import sys
import socket
import qdarkstyle

RECEIVER_IP= "127.0.0.1"   # IN UDP
RECEIVER_PORT = 5000

SENDER_IP = "127.0.0.1"
SENDER_PORT = 5000


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((SENDER_IP, SENDER_PORT))


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('PyFolder\chatBox\TEST\chat.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.sendButton.clicked.connect(self.sendButtonFunction)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateRequest)
        self.timer.start(100)

    def updateRequest(self):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            message = data.decode()
            print(f"Message Received : \"{message}\"")
            self.listWidget.insertItem(0, message)
            self.listWidget.item(0).setForeground(QtCore.Qt.black)


    def sendButtonFunction(self):
        msg=self.yourMessage_Input.text().strip()
        data = msg.encode("Utf8")
        print(f"# --------------- #\nMessage Sent : \"{msg}\" \nTo : {RECEIVER_IP} | Receiver's Port : {RECEIVER_PORT}\n# --------------- #")
        sock.sendto(data, (RECEIVER_IP, RECEIVER_PORT))

app = QApplication(sys.argv)
window = MainWindows()
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
app.exec_()



