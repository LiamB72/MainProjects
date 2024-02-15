"""
Simulateur de jeu de 52 cartes
Liam BERGE TG1 | Started On: 21/10/2023 | Last Edit: 22/01/2024
"""

import pickle
import socket
import sys
from functools import partial

from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QMessageBox, QVBoxLayout, QHBoxLayout, \
    QScrollArea

from modulesFunction import JeuDeCartes


class startMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UIs/startMenu.ui", self)
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

        self.gmChosen = "Target Score"
        self.targetScore = self.spinBox.value()

        self.helpButton.clicked.connect(self.helpWindow)

        self.confirmButton.clicked.connect(self.setVariables)
        self.radioButton.toggled.connect(self.gameSelectionEnabled)
        self.radioButton_2.toggled.connect(self.gameSelectionDisabled)
        self.gamemode1.toggled.connect(self.enableTargetScore)

    def setVariables(self):

        if self.gamemode1.isChecked():
            self.gmChosen = "Target Score"
            self.targetScore = self.spinBox.value()

    def gameSelectionEnabled(self):
        self.gm_Selection.setEnabled(True)

    def gameSelectionDisabled(self):
        self.gm_Selection.setEnabled(False)

    def enableTargetScore(self):
        self.spinBox.setEnabled(True)

    def helpWindow(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QIcon("Resources/QTImages/information.png"))
        msg.setText(
            "Appuyez sur la touche \"Win\", puis tapez : \"cmd\" et appuyez sur Entrée. Ensuite, écrivez : "
            "\"ipconfig\", puis ré-appuyez sur la touche Entrée, enfin recherchez l'IPv4 que vous enverrez au "
            "deuxième joueur.\n(Cette IP ce présente ainsi: xxx.xxx.xxx.xxx, par exemple: 192.168.1.2)")
        msg.setWindowTitle("Aide")
        msg.exec_()

    # When pressing the start button!
    def startGame(self):
        self.RECEIVER_IP = self.lineEdit.text().strip()

        if self.RECEIVER_IP == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QIcon("Resources/QTImages/warning.png"))
            msg.setText("Veuiller entrer l'IPv4 de l'autre joueur.")
            msg.setWindowTitle("Attention !")
            msg.exec_()

        if self.RECEIVER_IP != "":
            self.RECEIVER_PORT = 5000

            if self.radioButton.isChecked():
                self.playerChosen = 1
                self.game_window = playerWindow(self, 1)

            elif self.radioButton_2.isChecked():
                self.playerChosen = 2
                self.game_window = playerWindow(self, 2)

            if self.game_window:
                self.game_window.show()

            self.close()


class playerWindow(QMainWindow):

    def __init__(self, start_menu: startMenu, player: int):
        super().__init__()
        self.player = player

        # Loads the ui according to which of the two ratio buttons have been selected 
        if self.player == 1:
            uic.loadUi("UIs/cartesJeux_ui-Player1.ui", self)
        elif self.player == 2:
            uic.loadUi("UIs/cartesJeux_ui-Player2.ui", self)

        # Make you unable to resize the window
        self.setFixedSize(self.size())
        self.show()

        self.SENDER_IP = start_menu.SENDER_IP
        self.SENDER_PORT = start_menu.SENDER_PORT
        self.IP_SENDER_LABEL.setText("Votre IP: " + self.SENDER_IP)

        self.RECEIVER_IP = start_menu.RECEIVER_IP
        self.RECEIVER_PORT = start_menu.RECEIVER_PORT
        self.IP_RECEVEUR_LABEL.setText("Leur IP: " + self.RECEIVER_IP)

        self.sock = start_menu.sock
        self.debugging = start_menu.debugging

        if self.player == 1:
            self.sendingButtonA.clicked.connect(self.sendMessage)

        if self.player == 2:
            self.sendingButtonB.clicked.connect(self.sendMessage)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        self.showPossibleCards.clicked.connect(self.showCards)
        self.cardWindow = None

        # Set the variables when player 1 has entered the game.
        if self.player == 1:

            self.jeu = JeuDeCartes()
            for _ in range(2):
                self.jeu.battre()

            self.paquetA = []
            self.tmpPaquetA = []
            self.paquetB = []

            self.game_mode = start_menu.gmChosen
            if self.game_mode == "Target Score":
                self.targetScore = start_menu.targetScore
                # print("Selected Gamemode: Target Score")
                # print(f"Target Score: {self.targetScore}")
                self.labelGamemode.setText(f"Mode de jeu: Score cible de {self.targetScore} points")

            if self.debugging:
                print(f"Cartes du jeu: {self.jeu.carte}")

            for i in range(0, round(len(self.jeu.carte) / 2)):
                self.paquetA.append(self.jeu.tirer())

            for i in range(0, round(len(self.jeu.carte))):
                self.paquetB.append(self.jeu.tirer())

            if self.debugging:
                print(f"\n\nCartes du jeu:{self.jeu.carte}\n\n\nPaquet A:{self.paquetA}\n\n\nPaquet B:{self.paquetB}")

            # Sends the variables to player 2.
            tempSock = self.sock
            tempSock.connect((self.RECEIVER_IP, self.RECEIVER_PORT))

            data = ("", False, (self.jeu, self.paquetB), (self.game_mode, self.targetScore))
            octets = pickle.dumps(data)
            tempSock.send(octets)

        elif self.player == 2:

            self.paquetB = []
            self.tmpPaquetB = []

        # Initialize other variables to be used by both players.

        self.comptA = 0
        self.batailleA = []
        self.chosenCardA = ()

        self.comptB = 0
        self.batailleB = []
        self.chosenCardB = ()

        self.ready1 = False
        self.ready2 = False

        self.round = 1

    # On a repeating clock of 100ms, it updates both the variables and the ui elements.
    def update(self):
        try:
            data, server = self.sock.recvfrom(1024)
        except socket.error as msg:
            data = None
        if data != None:

            # Message is a Tuple != string, so we use pickle.dumps to encode the tuple.
            # Then we use pickle.loads to decode the tuple.
            self.message = pickle.loads(data)

            if self.message[2] == ():  # To check if the starting data has been already given.

                if self.player == 1:
                    if self.message[1]:
                        self.ready2 = True

                    if self.debugging:
                        print("To Player1: ", self.message, " | ", type(self.message))

                elif self.player == 2:
                    if self.message[1]:
                        self.ready1 = True

                    if self.debugging:
                        print("To Player2: ", self.message, " | ", type(self.message))

                self.applyChanges()

            # Retrives the starting data.
            elif self.message[2] != () and self.player == 2:
                self.jeu = self.message[2][0]
                self.paquetB = self.message[2][1]

                self.game_mode = self.message[3][0]
                if self.game_mode == 'Target Score':
                    self.targetScore = self.message[3][1]
                    # print("Selected Gamemode: Target Score")
                    # print(f"Target Score: {self.targetScore}")
                    self.labelGamemode.setText(f"Mode de jeu: Score cible de {self.targetScore} points")

                # print(self.message[3], self.targetScore, self.game_mode)
                print("Tu as reçu les informations requises pour jouer !")

            self.checkPaquets()

    # Sends the card played       
    def sendMessage(self):

        # Whenever the player window is 1 or 2, it sends the correct text to the receiver's IP.
        if self.player == 1:
            self.ready1 = True
            if self.currentCardA.text().strip() == "":
                self.warningBox("Veuiller selectionner une carte.", "Resources/QTImages/warning.png")
                cardNotSelected = True

            elif self.currentCardA.text().strip() != "":
                cardNotSelected = False

            if not cardNotSelected:
                message = (self.currentCardA.text().strip(), self.ready1, (), ())
                self.sendingButtonA.setEnabled(False)

        elif self.player == 2:
            self.ready2 = True

            if self.currentCardB.text().strip() == "":
                self.warningBox("Veuiller selectionner une carte.", "Resources/QTImages/warning.png")
                cardNotSelected = True

            elif self.currentCardB.text().strip() != "":
                cardNotSelected = False

            if not cardNotSelected:
                message = (self.currentCardB.text().strip(), self.ready2, (), ())
                self.sendingButtonB.setEnabled(False)

        if cardNotSelected == False:
            self.showPossibleCards.setEnabled(False)
            self.applyChanges()

            # Explained in self.update()
            data = pickle.dumps(message)

            # Sends the data to the opponent.
            self.sock.sendto(data, (self.RECEIVER_IP, self.RECEIVER_PORT))

            self.checkPaquets()

            if self.debugging:
                print(
                    f"---\nMessage sent: \"{message}\" \nReceiver's IP: {self.RECEIVER_IP}\nReceiver's Port : {self.RECEIVER_PORT}")

    # Creates a warning box that warns the player of an action!
    def warningBox(self, message: str, path: str):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon(path))
        msg.setText(message)
        msg.setWindowTitle("Attention !")
        msg.exec_()

    # Shows the window which contains the deck of the player opening the window.
    def showCards(self):

        if self.player == 1:
            self.cardWindow = cardWindow(self, self.paquetA)

        elif self.player == 2:
            self.cardWindow = cardWindow(self, self.paquetB)

        self.cardWindow.show()

    # Changes the image of the card A and the text of the current card A played.
    def changeCurrentCardA(self, imagePathNameA: int, newCard: str, data: tuple):

        self.carteChoisieA.setPixmap(QtGui.QPixmap("Resources/data/" + str(imagePathNameA) + ".png"))
        self.currentCardA.setText(newCard)
        self.chosenCardA = data

    # Changes the image of the card B and the text of the current card A played.   
    def changeCurrentCardB(self, imagePathNameB: int, newCard: str, data: tuple):

        self.carteChoisieB.setPixmap(QtGui.QPixmap("Resources/data/" + str(imagePathNameB) + ".png"))
        self.currentCardB.setText(newCard)
        self.chosenCardB = data

    # Changes the UI elements, some variables and starts the actual game when both of the players are ready.
    def applyChanges(self):

        if self.ready1 and self.ready2:

            if self.player == 1:

                for key, _ in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == self.message[0]:
                        self.changeCurrentCardB(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key), self.message[0])

                self.sendingButtonA.setEnabled(True)


            elif self.player == 2:
                for key, _ in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == self.message[0]:
                        self.changeCurrentCardA(JeuDeCartes().images[key], JeuDeCartes().nomCarte(key), self.message[0])

                self.sendingButtonB.setEnabled(True)

            self.showPossibleCards.setEnabled(True)
            self.ready1, self.ready2 = False, False
            self.runGame()

    def checkPaquets(self):

        if self.player == 1:

            if len(self.paquetA) < 5:
                self.paquetA.extend(self.tmpPaquetA)
                self.tmpPaquetA.clear()

        elif self.player == 2:

            if len(self.paquetB) < 5:
                self.paquetB.extend(self.tmpPaquetB)
                self.tmpPaquetB.clear()

    # The title says it all.
    def runGame(self):
        indexA = 0
        indexB = 0

        carteJoueeA = ()
        carteJoueeB = ()
        roundWinner = ""
        self.bataille = False

        if self.comptA < self.targetScore or self.comptB < self.targetScore:

            if self.player == 1:
                carteJoueeA = self.chosenCardA

                for key, _ in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == self.message[0]:
                        carteJoueeB = key

                indexA = self.paquetA.index(carteJoueeA)

                #print(self.paquetA)
                #print(carteJoueeA)

            elif self.player == 2:

                carteJoueeB = self.chosenCardB

                for key, _ in JeuDeCartes().images.items():
                    if str(JeuDeCartes().nomCarte(key)) == self.message[0]:
                        carteJoueeA = key

                indexB = self.paquetB.index(carteJoueeB)

            if carteJoueeA[0] > carteJoueeB[0]:

                if self.player == 2:
                    self.paquetB.pop(indexB)

                if self.player == 1:
                    self.tmpPaquetA.append(carteJoueeA)
                    self.paquetA.pop(indexA)
                    self.tmpPaquetA.append(carteJoueeB)

                    if len(self.batailleA) != 0 and len(self.batailleB) != 0:
                        self.tmpPaquetA.extend(self.batailleA)
                        self.tmpPaquetA.extend(self.batailleB)
                        self.batailleA.clear()
                        self.batailleB.clear()
                        self.bataille = False

                self.comptA += 1
                roundWinner = "Joueur 1"

            elif carteJoueeB[0] > carteJoueeA[0]:

                if self.player == 1:
                    self.paquetA.pop(indexA)

                if self.player == 2:

                    self.tmpPaquetB.append(carteJoueeB)
                    self.paquetB.pop(indexB)
                    self.tmpPaquetB.append(carteJoueeA)

                    if len(self.batailleA) != 0 and len(self.batailleB) != 0:
                        self.tmpPaquetB.extend(self.batailleA)
                        self.tmpPaquetB.extend(self.batailleB)
                        self.batailleA.clear()
                        self.batailleB.clear()
                        self.bataille = False

                self.comptB += 1
                roundWinner = "Joueur 2"

            elif carteJoueeA[0] == carteJoueeB[0]:

                self.bataille = True

                self.currentWinner.setText("***********!!BATAILLE!!***********")

                self.batailleA.append(carteJoueeA)
                self.batailleB.append(carteJoueeB)

                if self.player == 1:
                    self.paquetA.pop(indexA)

                if self.player == 2:
                    self.paquetB.pop(indexB)

            if not self.bataille:
                self.currentWinner.setText(f"   Tour n°{self.round} | Gagnant : {roundWinner}")
                self.scoreA.setText(f"Score: {self.comptA}")
                self.scoreB.setText(f"Score: {self.comptB}")

                self.round += 1

        elif self.comptA < self.targetScore:

            print("Joueur 1 est le/la gagnant(e) !")
            self.currentWinner.setText("   Joueur 1 est le/la gagnant(e) !")
            self.showPossibleCards.setEnabled(False)
            if self.player == 1:
                self.sendingButtonA.setEnabled(False)
            if self.player == 2:
                self.sendingButtonB.setEnabled(False)

        elif self.comptB < self.targetScore:

            print("Joueur 2 est le/la gagnant(e) !")
            self.currentWinner.setText("   Joueur 2 est le/la gagnant(e) !")
            self.showPossibleCards.setEnabled(False)
            if self.player == 1:
                self.sendingButtonA.setEnabled(False)
            if self.player == 2:
                self.sendingButtonB.setEnabled(False)

        self.changeCurrentCardA(JeuDeCartes().images[carteJoueeA], "", ())
        self.changeCurrentCardB(JeuDeCartes().images[carteJoueeB], "", ())

        self.checkPaquets()


class cardWindow(QWidget):

    def __init__(self, main_window: playerWindow, deck: list):

        super().__init__()
        self.setWindowTitle("Card Storage")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.scroll_area = QScrollArea()
        self.setGeometry(200, 200, 700, 275)

        widget = QWidget()
        widget_layout = QHBoxLayout()
        widget.setLayout(widget_layout)

        lenghtDeck = len(deck)
        self.debugging = main_window.debugging

        # Creates a dynamic window of every card in the player's deck.
        if lenghtDeck != 0:
            for i in range(0, lenghtDeck):
                button = QPushButton()
                button.clicked.connect(partial(self.button_clicked, main_window))
                button.my_data = deck[i]

                pixmap = QPixmap("Resources/data/" + str(JeuDeCartes().images[deck[i]]) + ".png")
                button.setIcon(QIcon(pixmap))
                button.setIconSize(pixmap.size())
                button.setMaximumSize(pixmap.size())
                button.setMinimumSize(pixmap.size())
                widget_layout.addWidget(button)

            widget_layout.addStretch()
            self.scroll_area.setWidget(widget)
            self.layout.addWidget(self.scroll_area)
        else:
            print("Your deck is empty.")

    def button_clicked(self, main_window):
        sender = self.sender()
        if hasattr(sender, 'my_data'):
            data = sender.my_data

            if main_window.player == 1:
                main_window.changeCurrentCardA(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data), data)

            elif main_window.player == 2:
                main_window.changeCurrentCardB(JeuDeCartes().images[data], JeuDeCartes().nomCarte(data), data)

            if main_window.debugging:
                print(f"Button clicked with data: {data} | Nom de Carte: {JeuDeCartes().nomCarte(data)}")
        self.close()


app = QApplication(sys.argv)
window = startMenu()
window.show()

app.exec()
