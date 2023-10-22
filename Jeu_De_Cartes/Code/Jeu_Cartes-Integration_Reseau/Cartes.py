"""
Simulateur de jeu de 52 cartes

Liam BERGE TG1 | 21/10/2023
"""
from time import sleep
from modulesFunction import JeuDeCartes, Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading
import socket

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        #self.sendingButton.clicked.connect(self.sendButton)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.RECEIVER_IP = ""
        self.RECEIVER_PORT = 500
        SENDER_NAME = socket.gethostname()
        self.SENDER_IP = socket.gethostbyname(SENDER_NAME)
        self.SENDER_PORT = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)
        self.sock.bind((self.SENDER_IP, self.SENDER_PORT))
        
        self.currentCardA.setText("Carte Actuel: PLACEHOLDER")
        self.currentCardB.setText("Carte Actuel: PLACEHOLDER")
        self.images = {(0, 0): "01",(1, 0): "02",(2, 0): "03",(3, 0): "04",(4, 0): "05",(5, 0): "06",(6, 0): "07",(7, 0): "08",(8, 0): "09",(9, 0): "10",(10, 0): "11",(11, 0): "12",(12, 0): "00",
                       (0, 1): "14",(1, 1): "15",(2, 1): "16",(3, 1): "17",(4, 1): "18",(5, 1): "19",(6, 1): "20",(7, 1): "21",(8, 1): "22",(9, 1): "23",(10, 1): "24",(11, 1): "25",(12, 1): "13",
                       (0, 2): "27",(1, 2): "28",(2, 2): "29",(3, 2): "30",(4, 2): "31",(5, 2): "32",(6, 2): "33",(7, 2): "34",(8, 2): "35",(9, 2): "36",(10, 2): "37",(11, 2): "38",(12, 2): "26",
                       (0, 3): "40",(1, 3): "41",(2, 3): "42",(3, 3): "43",(5, 3): "44",(4, 3): "45",(6, 3): "46",(7, 3): "47",(8, 3): "48",(9, 3): "49",(10, 3): "50",(11, 3): "51",(12, 3): "39"}
        self.debugging = False

    def update(self):
        try:
            data, server = self.sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            message = data.decode()
            ####################
            #A Compléter
            ####################
            if self.debugging:
                print(f"---\nMessage Received : {message}")
            

    def sendButton(self):
        
        # Si le texte de l'IP du recevant est vide
        if self.receiverIP_Input.text().strip() != "": 
            
            self.RECEIVER_IP = self.receiverIP_Input.text()
        else:
            self.RECEIVER_IP = "127.0.0.1"

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ####################
        message = None #A compléter
        ####################
        data = message.encode("Utf8")

        if self.debugging:
            print(f"---\nMessage sent: \"{message}\" \nReceiver's IP: {self.RECEIVER_IP}\nReceiver's Port : {self.RECEIVER_PORT}")

        sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))


app = QApplication([])
window = Window()
window.show()

app.exec()