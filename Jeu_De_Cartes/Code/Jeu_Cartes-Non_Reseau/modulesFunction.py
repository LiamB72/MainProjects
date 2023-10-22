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
        self.carteChoisieA = QtWidgets.QLabel(self.centralwidget)
        self.carteChoisieA.setGeometry(QtCore.QRect(120, 320, 180, 250))
        self.carteChoisieA.setText("")
        self.carteChoisieA.setPixmap(QtGui.QPixmap("Jeu_Cartes-Non_Reseau/data/54.png"))
        self.carteChoisieA.setAlignment(QtCore.Qt.AlignCenter)
        self.carteChoisieA.setWordWrap(False)
        self.carteChoisieA.setIndent(1)
        self.carteChoisieA.setObjectName("carteChoisieA")
        self.currentCardA = QtWidgets.QLabel(self.centralwidget)
        self.currentCardA.setGeometry(QtCore.QRect(10, 420, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.currentCardA.setFont(font)
        self.currentCardA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentCardA.setWordWrap(True)
        self.currentCardA.setObjectName("currentCardA")
        self.playerA = QtWidgets.QLabel(self.centralwidget)
        self.playerA.setGeometry(QtCore.QRect(10, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.playerA.setFont(font)
        self.playerA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.playerA.setWordWrap(True)
        self.playerA.setObjectName("playerA")
        self.carteChoisieB = QtWidgets.QLabel(self.centralwidget)
        self.carteChoisieB.setGeometry(QtCore.QRect(390, 10, 180, 250))
        self.carteChoisieB.setText("")
        self.carteChoisieB.setTextFormat(QtCore.Qt.PlainText)
        self.carteChoisieB.setPixmap(QtGui.QPixmap("Jeu_Cartes-Non_Reseau/data/54.png"))
        self.carteChoisieB.setAlignment(QtCore.Qt.AlignCenter)
        self.carteChoisieB.setWordWrap(False)
        self.carteChoisieB.setIndent(1)
        self.carteChoisieB.setObjectName("carteChoisieB")
        self.currentCardB = QtWidgets.QLabel(self.centralwidget)
        self.currentCardB.setGeometry(QtCore.QRect(570, 130, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.currentCardB.setFont(font)
        self.currentCardB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentCardB.setWordWrap(True)
        self.currentCardB.setObjectName("currentCardB")
        self.PlayerB = QtWidgets.QLabel(self.centralwidget)
        self.PlayerB.setGeometry(QtCore.QRect(570, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PlayerB.setFont(font)
        self.PlayerB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.PlayerB.setWordWrap(True)
        self.PlayerB.setObjectName("PlayerB")
        self.currentWinner = QtWidgets.QLabel(self.centralwidget)
        self.currentWinner.setGeometry(QtCore.QRect(170, 260, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currentWinner.setFont(font)
        self.currentWinner.setObjectName("currentWinner")
        self.scoreA = QtWidgets.QLabel(self.centralwidget)
        self.scoreA.setGeometry(QtCore.QRect(10, 390, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scoreA.setFont(font)
        self.scoreA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreA.setWordWrap(True)
        self.scoreA.setObjectName("scoreA")
        self.scoreB = QtWidgets.QLabel(self.centralwidget)
        self.scoreB.setGeometry(QtCore.QRect(570, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scoreB.setFont(font)
        self.scoreB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreB.setWordWrap(True)
        self.scoreB.setObjectName("scoreB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currentCardA.setText(_translate("MainWindow", "Carte Actuel :"))
        self.playerA.setText(_translate("MainWindow", "Joueur 1:"))
        self.currentCardB.setText(_translate("MainWindow", "Carte Actuel :"))
        self.PlayerB.setText(_translate("MainWindow", "Joueur 2:"))
        self.currentWinner.setText(_translate("MainWindow", "Round N | WINNER : PLACEHOLDER"))
        self.scoreA.setText(_translate("MainWindow", "Score : "))
        self.scoreB.setText(_translate("MainWindow", "Score : "))

