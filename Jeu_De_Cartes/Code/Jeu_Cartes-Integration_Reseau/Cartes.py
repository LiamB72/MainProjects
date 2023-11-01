"""
Simulateur de jeu de 52 cartes

Liam BERGE TG1 | 21/10/2023
"""

from modulesFunction import JeuDeCartes, Ui_MainWindow_StartMenu
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
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
        self.debugging = False
        
        if self.debugging:
            
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
    
    def startGame(self):
        if not self.debugging:
            self.RECEIVER_IP = self.lineEdit.text().strip()
        else:
            self.RECEIVER_IP = self.SENDER_IP
        self.RECEIVER_PORT = 5000
        
        if not self.debugging:
            if self.radioButton.isChecked():

                self.playerChosen = 1
                self.game_window = playerWindow(self,1)

            elif self.radioButton_2.isChecked():

                self.playerChosen = 2
                self.game_window = playerWindow(self,2)
                
        else:
            self.playerChosen = 1
            self.game_window = playerWindow(self,1)
            self.game_window2 = playerWindow(self,2)
        
        if self.debugging:
            if self.game_window and self.game_window2:
                self.game_window.show()
                self.game_window2.show()
        elif not self.debugging:
            if self.game_window:
                self.game_window.show()
        self.close()

class playerWindow(QMainWindow):
    
    def __init__(self, start_menu, player):      
        super(playerWindow, self).__init__()
        
        self.player = player
        
        # Loads the ui according to which of the two ratio buttons have been selected 
        if self.player == 1:
            uic.loadUi("Code/Jeu_Cartes-Integration_Reseau/UIs/cartesJeux_ui-Player1.ui", self)
        elif self.player == 2:
            uic.loadUi("Code/Jeu_Cartes-Integration_Reseau/UIs/cartesJeux_ui-Player2.ui", self)
        
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
        
        self.jeu = JeuDeCartes()
        self.jeu.battre()
        
        self.comptA = 0
        self.paquetA = [] 
        self.batailleA = []
        
        self.comptB = 0
        self.paquetB = []
        self.batailleB = []

        if self.debugging:
            print(f"Cartes du jeu: {self.jeu.carte}")
            
        for i in range(0, round(len(self.jeu.carte)/2)):
            self.paquetA.append(self.jeu.tirer())
            self.paquetB.append(self.jeu.tirer())
            
        if self.debugging:
            print(f"\n\nCartes du jeu:{self.jeu.carte}\n\n\nPaquet A:{self.paquetA}\n\n\nPaquet B:{self.paquetB}")
                
        self.ready1 = False
        self.ready2 = False
        
        
    def update(self):
        try:
            data, server = self.sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:
            #message = data.decode()
            # The message is now a tuple that tells which card is played by the other party (which is btw a string and not a another tuple),
            # and then a bool to tell that the party A or B is ready. And so that's why we use pickle, it's to "serialize" (transform into bytes)
            # the message sent with pickle.dumps(data), then loads the message's data with pickle.loads(data), to retrive the tuple and its content.
            message = pickle.loads(data)
            if self.player == 1:
                print("To Player1: ",message, " | ", type(message))
            
                for key, values in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == message[0]:
                        self.changeCurrentCardB(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key))

                if message[1]:
                    self.ready2 = True
                
                if self.debugging:
                    print("To Player1: ",message, " | ", type(message))
                    
            elif self.player == 2:

                for key, values in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == message[0]:
                        self.changeCurrentCardA(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key))

                if message[1]:
                    self.ready1 = True
                    
                if self.debugging:
                    print("To Player2: ",message, " | ", type(message))
                    
            if self.ready1 and self.ready2:
                self.sendingButton.setEnabled(True)
                self.showPossibleCards.setEnabled(True)
            
    def sendMessage(self):
        # Whenever the player window is 1 or 2, it sends the correct text to the receiver's IP.
        if self.player == 1:
            self.ready1 = True
            message = (self.currentCardA.text().strip(), self.ready1)
        elif self.player == 2:
            self.ready2 = True
            message = (self.currentCardB.text().strip(), self.ready2)
            
        
        #data = message.encode("Utf8")
        # As stated previously in update, the message is now a tuple, which means it can't be encoded anymore (encode is for text only).
        # So we use pickle.dumps to transform the tuple into bytes and then send them tot he receiver's IP.
        
        data = pickle.dumps(message)
        self.sendingButton.setEnabled(False)
        self.showPossibleCards.setEnabled(False)

        if self.debugging:
            print(f"---\nMessage sent: \"{message}\" \nReceiver's IP: {self.RECEIVER_IP}\nReceiver's Port : {self.RECEIVER_PORT}")

        self.sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))
        
    def showCards(self):
        # Shows a window, within is shown the player's current card that they earn during the game.
        if self.player == 1:
            self.cardWindow = cardWindow(self, self.paquetA)
            
        elif self.player == 2:
            self.cardWindow = cardWindow(self, self.paquetB)
            
        self.cardWindow.show()
        
    def addCardToDeck(self):
        # Random Card Generator [ONLY FOR TEST PURPOSES]
        if self.player == 1:
            self.paquetA.append((randint(0,12),randint(0,3)))
        elif self.player == 2:
            self.paquetB.append((randint(0,12),randint(0,3)))
        
    def changeCurrentCardA(self, imagePathNameA, newCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieA.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameA)+".png"))
        self.currentCardA.setText(newCard)
        
    def changeCurrentCardB(self, imagePathNameB, newCard):
        # Changes the card's Pixel Map (It's Image) with a given Path
        self.carteChoisieB.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameB)+".png"))
        self.currentCardB.setText(newCard)


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
            
            if main_window.player == 1:
                main_window.changeCurrentCardA(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data))
            elif main_window.player == 2:
                main_window.changeCurrentCardB(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data))
            if main_window.debugging:
                print(f"Button clicked with data: {data} | Nom de Carte: {JeuDeCartes().nomCarte(data)}")
        self.close()


app = QApplication([])
window = startMenu()
window.show()

app.exec()
