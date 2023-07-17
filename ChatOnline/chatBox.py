from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui,uic
import sys
import socket

UDP_IP_DU_BINOME = ""
UDP_PORT_DU_BINOME = 5000

UDP_IP_MON_PC = ""
UDP_PORT_MON_PC = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP_MON_PC, UDP_PORT_MON_PC))

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('chatBox.ui', self)
        self.setFixedSize(self.size())
        self.show()

        self.pushButton.clicked.connect(self.boutonEnvoi)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.miseAJour)
        self.timer.start(100)

    def miseAJour(self):
        try:
            data, server = sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            message = data.decode()
            self.listWidget.insertItem(0, message)
            self.listWidget.item(0).setForeground(QtCore.Qt.blue)

    def boutonEnvoi(self):
        UDP_IP_MON_PC = self.lineEditOwn.text()
        UDP_IP_DU_BINOME = self.lineEditTheir.text()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = self.lineEdit.text()
        octets = message.encode("Utf8")
        #print(octets)
        sock.sendto(octets, (UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()