"""
Simulateur de jeu de 52 cartes

Liam BERGE TG1 | 21/10/2023
"""

from modulesFunction import JeuDeCartes, Ui_MainWindow_StartMenu, Ui_MainWindow_Player1, Ui_MainWindow_Player2
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,  QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
import threading
import socket
import pickle
from time import sleep
from random import randint
from functools import partial

class startMenu(QMainWindow, Ui_MainWindow_StartMenu):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startGame)
        
        SENDER_NAME = socket.gethostname()
        self.SENDER_IP = socket.gethostbyname(SENDER_NAME)
        self.SENDER_PORT = 5000

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)
        self.sock.bind((self.SENDER_IP, self.SENDER_PORT))
        
        self.playerChosen = 0
        self.game_window = None
        self.game_window2 = None
        self.debugging = True
        
        if self.debugging:
            
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
    
    def startGame(self):
        self.RECEIVER_IP = self.lineEdit.text().strip()
        self.RECEIVER_PORT = 5000
        
        if not self.debugging:
            if self.radioButton.isChecked():

                self.playerChosen = 1
                self.game_window = player1Window(self)

            elif self.radioButton_2.isChecked():

                self.playerChosen = 2
                self.game_window = player2Window(self)
                
        else:
            self.playerChosen = 1
            self.game_window = player1Window(self)
            self.game_window2 = player2Window(self)
            
        #message = str(self.playerChosen)
        #data = message.encode("Utf8")
        #self.sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))
        
        if self.debugging:
            if self.game_window and self.game_window2:
                self.game_window.show()
                self.game_window2.show()
        elif not self.debugging:
            if self.game_window:
                self.game_window.show()
        self.close()

###############
# 192.168.1.202
###############

class player1Window(QMainWindow, Ui_MainWindow_Player1):
    
    def __init__(self, start_menu):
        # Confused as to, why doesn't it regonized the elements of the ui?
        
        super(player1Window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.show()
        
        self.SENDER_IP = start_menu.SENDER_IP
        self.SENDER_PORT = start_menu.SENDER_PORT
        self.RECEIVER_IP = start_menu.RECEIVER_IP
        self.RECEIVER_PORT = start_menu.RECEIVER_PORT
        self.sock = start_menu.sock
        self.debugging = start_menu.debugging
        
        self.IP_RECEVEUR_LABEL.setText("Leur IP: "+self.RECEIVER_IP)
        self.IP_SENDER_LABEL.setText("Votre IP: "+self.SENDER_IP)
        self.sendingButton.clicked.connect(self.sendMessage)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        
        self.showPossibleCards.clicked.connect(self.showCards)
        self.addCard.clicked.connect(self.addCardToDeck)
        self.cardWindow = None
        
        self.comptA = 0
        self.packetA = [] 
        self.batailleA = []
        
        self.comptB = 0
        self.packetB = []
        self.batailleB = []
        
        self.ready1 = False
        
        
    def update(self):
        #Barely even touched it yet..
        try:
            data, server = self.sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            # Data received will be a tuple for the card's IP and colour
            #message = data.decode()
            
            message = pickle.loads(data)
            print("To Player1: ",message, " | ", type(message))
            
            for key, values in JeuDeCartes().images.items():
                if str(JeuDeCartes().nomCarte(key)) == message[0]:
                    self.changeCurrentCardB(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key))

            if message[1] == True and self.ready1:
                self.sendingButton.setEnabled(True)
                self.showPossibleCards.setEnabled(True)
            
            if self.debugging:
                print(f"---\nPlayer 1 has received a message: {message}")
                
    def sendMessage(self):
        # Still under huge development
        self.ready1 = True
        
        message = (self.currentCardA.text().strip(), self.ready1)
        
        #data = message.encode("Utf8")
        data = pickle.dumps(message)
        self.sendingButton.setEnabled(False)
        self.showPossibleCards.setEnabled(False)

        if self.debugging:
            print(f"---\nMessage sent: \"{message}\" \nReceiver's IP: {self.RECEIVER_IP}\nReceiver's Port : {self.RECEIVER_PORT}")

        self.sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))
        
    def showCards(self):
        # Shows a window, within is shown to have every card of the player's.
        self.cardWindow = cardWindow(self, self.packetA)
        self.cardWindow.show()
        
    def addCardToDeck(self):
        # Random Card Generator [ONLY FOR TEST PURPOSES]
        self.packetA.append((randint(0,12),randint(0,3)))
        
    def changeCurrentCardA(self, imagePathNameA, newCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieA.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameA)+".png"))
        self.currentCardA.setText(newCard)
    def changeCurrentCardB(self, imagePathNameB, newCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieB.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameB)+".png"))
        self.currentCardB.setText(newCard)


class player2Window(QMainWindow, Ui_MainWindow_Player2):
    
    def __init__(self, start_menu):
        # Confused as to, why doesn't it regonized the elements of the ui?
        
        super(player2Window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.show()
        
        self.SENDER_IP = start_menu.SENDER_IP
        self.SENDER_PORT = start_menu.SENDER_PORT
        self.RECEIVER_IP = start_menu.RECEIVER_IP
        self.RECEIVER_PORT = start_menu.RECEIVER_PORT
        self.sock = start_menu.sock
        self.debugging = start_menu.debugging
        
        self.IP_RECEVEUR_LABEL.setText("Leur IP: "+self.RECEIVER_IP)
        self.IP_SENDER_LABEL.setText("Votre IP: "+self.SENDER_IP)
        self.sendingButton.clicked.connect(self.sendMessage)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        
        self.showPossibleCards.clicked.connect(self.showCards)
        self.addCard.clicked.connect(self.addCardToDeck)
        self.cardWindow = None
        
        self.comptB = 0
        self.packetB = [] 
        self.batailleB = []
        
        self.ready2 = False
        
        
    def update(self):
        #Barely even touched it yet..
        try:
            data, server = self.sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            # Data received will be a tuple for the card's IP and colour
            # message = data.decode()
            message = pickle.loads(data)
            print("To Player2: ", message, " | ", type(message))
            
            for key, values in JeuDeCartes().images.items():
                if str(JeuDeCartes().nomCarte(key)) == message[0]:
                    self.changeCurrentCardA(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key))

            if message[1] == True and self.ready2:
                self.sendingButton.setEnabled(True)
                self.showPossibleCards.setEnabled(True)
            
            if self.debugging:
                print(f"---\nPlayer 2 has received a message: {message}")
                
    def sendMessage(self):
        # Still under huge development
        self.ready2 = True
        
        message = (self.currentCardB.text().strip(), self.ready2)
        
        #data = message.encode("Utf8")
        data = pickle.dumps(message)
        self.sendingButton.setEnabled(False)
        self.showPossibleCards.setEnabled(False)

        if self.debugging:
            print(f"---\nMessage sent: \"{message}\" \nReceiver's IP: {self.RECEIVER_IP}\nReceiver's Port : {self.RECEIVER_PORT}")

        self.sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))
        
    def showCards(self):
        # Shows a window, within is shown to have every card of the player's.
        self.cardWindow = cardWindow(self, self.packetB)
        self.cardWindow.show()
        
    def addCardToDeck(self):
        # Random Card Generator [ONLY FOR TEST PURPOSES]
        self.packetB.append((randint(0,12),randint(0,3)))
        
    def changeCurrentCardB(self, imagePathNameB, NewCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieB.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameB)+".png"))
        self.currentCardB.setText(NewCard)
    def changeCurrentCardA(self, imagePathNameA, NewCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieA.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameA)+".png"))
        self.currentCardA.setText(NewCard)

        
class cardWindow(QWidget):
    def __init__(self, main_window, deck):
        
        super().__init__()

        self.setWindowTitle("Card Storage")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.scroll_area = QScrollArea()
        self.setGeometry(200, 200, 500, 275)
        
        widget = QWidget()
        widget_layout = QHBoxLayout()
        widget.setLayout(widget_layout)
        
        lenghtDeck = len(deck)
        self.debugging = main_window.debugging
        
        if lenghtDeck != 0:
            for i in range(0, lenghtDeck):
            
                button = QPushButton()
                button.clicked.connect(partial(self.button_clicked, main_window))
                button.my_data = deck[i]

                pixmap = QPixmap("Resources/data/"+str(JeuDeCartes().images[deck[i]])+".png")
                button.setIcon(QIcon(pixmap))
                button.setIconSize(pixmap.size())
                button.setMaximumSize(pixmap.size())
                button.setMinimumSize(pixmap.size())
                widget_layout.addWidget(button)
                
            widget_layout.addStretch()  # Add spacing to the right
            self.scroll_area.setWidget(widget)
            self.layout.addWidget(self.scroll_area)
        else:
            pass


    def button_clicked(self, main_window):
        sender = self.sender()
        if hasattr(sender, 'my_data'):
            data = sender.my_data
            
            if isinstance(main_window, player1Window):
                main_window.changeCurrentCardA(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data))
            elif isinstance(main_window, player2Window):
                main_window.changeCurrentCardB(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data))
            print(f"Button clicked with data: {data} | Nom de Carte: {JeuDeCartes().nomCarte(data)}")
        self.close()


app = QApplication([])
window = startMenu()
window.show()

app.exec()
