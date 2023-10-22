from random import shuffle
from PyQt5 import QtCore, QtGui, QtWidgets

class JeuDeCartes(object):

    def __init__(self):
        """Construction du jeu de carte"""
        self.carte = []  # Liste vide à remplir
        """Simulation d'un jeu de 52 cartes"""
        # Valeur des cartes
        self.valeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
        # Couleur de la carte
        self.couleur = ["Trèfle", "Carreau", "Coeur", "Pique"]
        for indiceCouleur in range(len(self.couleur)):
            for indiceValeur in range(len(self.valeur)):
                self.carte.append((indiceValeur, indiceCouleur))


    def nomCarte(self, c):
        """Renvoie le nom de la carte (<c> doit être un tuple !!!)"""
        if self.carte != []:
            return f"{self.valeur[c[0]]} de {self.couleur[c[1]]}"

    def battre(self):
        """Mélange les cartes"""
        shuffle(self.carte)

    def tirer(self):
        """Retire une carte du jeu"""
        if self.carte != []:
            self.carteTirer = self.carte[0]
            del(self.carte[0])
            #print(f"{self.valeur[self.carteTirer[0]]} de {self.couleur[self.carteTirer[1]]}")
            
        else:
            print("Plus de cartes")
            
        
        return self.carteTirer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player1 = QtWidgets.QGroupBox(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(0, 280, 451, 291))
        self.player1.setAutoFillBackground(True)
        self.player1.setFlat(False)
        self.player1.setObjectName("player1")
        self.IP_SENDER_LABEL = QtWidgets.QLabel(self.player1)
        self.IP_SENDER_LABEL.setGeometry(QtCore.QRect(30, 160, 151, 41))
        self.IP_SENDER_LABEL.setObjectName("IP_SENDER_LABEL")
        self.currentCardA = QtWidgets.QLabel(self.player1)
        self.currentCardA.setGeometry(QtCore.QRect(30, 120, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.currentCardA.setFont(font)
        self.currentCardA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentCardA.setWordWrap(True)
        self.currentCardA.setObjectName("currentCardA")
        self.scoreA = QtWidgets.QLabel(self.player1)
        self.scoreA.setGeometry(QtCore.QRect(30, 90, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scoreA.setFont(font)
        self.scoreA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreA.setWordWrap(True)
        self.scoreA.setObjectName("scoreA")
        self.carteChoisieA = QtWidgets.QLabel(self.player1)
        self.carteChoisieA.setGeometry(QtCore.QRect(250, 20, 200, 275))
        self.carteChoisieA.setText("")
        self.carteChoisieA.setPixmap(QtGui.QPixmap("data/54.png"))
        self.carteChoisieA.setAlignment(QtCore.Qt.AlignCenter)
        self.carteChoisieA.setWordWrap(False)
        self.carteChoisieA.setIndent(1)
        self.carteChoisieA.setObjectName("carteChoisieA")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 0, 451, 291))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.scoreB = QtWidgets.QLabel(self.groupBox)
        self.scoreB.setGeometry(QtCore.QRect(250, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scoreB.setFont(font)
        self.scoreB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreB.setWordWrap(True)
        self.scoreB.setObjectName("scoreB")
        self.IP_RECEVEUR_TEXT = QtWidgets.QLineEdit(self.groupBox)
        self.IP_RECEVEUR_TEXT.setGeometry(QtCore.QRect(250, 180, 161, 31))
        self.IP_RECEVEUR_TEXT.setObjectName("IP_RECEVEUR_TEXT")
        self.currentCardB = QtWidgets.QLabel(self.groupBox)
        self.currentCardB.setGeometry(QtCore.QRect(250, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.currentCardB.setFont(font)
        self.currentCardB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentCardB.setWordWrap(True)
        self.currentCardB.setObjectName("currentCardB")
        self.IP_RECEVEUR_LABEL = QtWidgets.QLabel(self.groupBox)
        self.IP_RECEVEUR_LABEL.setGeometry(QtCore.QRect(250, 140, 151, 41))
        self.IP_RECEVEUR_LABEL.setObjectName("IP_RECEVEUR_LABEL")
        self.PlayerB = QtWidgets.QLabel(self.groupBox)
        self.PlayerB.setGeometry(QtCore.QRect(250, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PlayerB.setFont(font)
        self.PlayerB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.PlayerB.setWordWrap(True)
        self.PlayerB.setObjectName("PlayerB")
        self.carteChoisieB = QtWidgets.QLabel(self.groupBox)
        self.carteChoisieB.setGeometry(QtCore.QRect(10, 20, 181, 251))
        self.carteChoisieB.setText("")
        self.carteChoisieB.setTextFormat(QtCore.Qt.PlainText)
        self.carteChoisieB.setPixmap(QtGui.QPixmap("data/54.png"))
        self.carteChoisieB.setAlignment(QtCore.Qt.AlignCenter)
        self.carteChoisieB.setWordWrap(False)
        self.carteChoisieB.setIndent(1)
        self.carteChoisieB.setObjectName("carteChoisieB")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.scoreB.raise_()
        self.IP_RECEVEUR_TEXT.raise_()
        self.currentCardB.raise_()
        self.IP_RECEVEUR_LABEL.raise_()
        self.PlayerB.raise_()
        self.pushButton.raise_()
        self.carteChoisieB.raise_()
        self.currentWinner = QtWidgets.QLabel(self.centralwidget)
        self.currentWinner.setGeometry(QtCore.QRect(190, 270, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.currentWinner.setFont(font)
        self.currentWinner.setAutoFillBackground(True)
        self.currentWinner.setObjectName("currentWinner")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.player1.setTitle(_translate("MainWindow", "Joueur 1"))
        self.IP_SENDER_LABEL.setText(_translate("MainWindow", "Votre IP :"))
        self.currentCardA.setText(_translate("MainWindow", "Carte Placée : PLACEHOLDER"))
        self.scoreA.setText(_translate("MainWindow", "Score : "))
        self.groupBox.setTitle(_translate("MainWindow", "Joueur 2"))
        self.scoreB.setText(_translate("MainWindow", "Score : "))
        self.IP_RECEVEUR_TEXT.setPlaceholderText(_translate("MainWindow", "IP du receveur"))
        self.currentCardB.setText(_translate("MainWindow", "Carte Placée : PLACEHOLDER"))
        self.IP_RECEVEUR_LABEL.setText(_translate("MainWindow", "Leur IP :"))
        self.PlayerB.setText(_translate("MainWindow", "Joueur 2: (Lui)"))
        self.pushButton.setText(_translate("MainWindow", "Confirmer"))
        self.currentWinner.setText(_translate("MainWindow", "Round N | WINNER : PLACEHOLDER"))


