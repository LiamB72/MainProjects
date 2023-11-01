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
                
        self.images = {(0, 0): "01",(1, 0): "02",(2, 0): "03",(3, 0): "04",(4, 0): "05",(5, 0): "06",(6, 0): "07",(7, 0): "08",(8, 0): "09",(9, 0): "10",(10, 0): "11",(11, 0): "12",(12, 0): "00",
                       (0, 1): "14",(1, 1): "15",(2, 1): "16",(3, 1): "17",(4, 1): "18",(5, 1): "19",(6, 1): "20",(7, 1): "21",(8, 1): "22",(9, 1): "23",(10, 1): "24",(11, 1): "25",(12, 1): "13",
                       (0, 2): "27",(1, 2): "28",(2, 2): "29",(3, 2): "30",(4, 2): "31",(5, 2): "32",(6, 2): "33",(7, 2): "34",(8, 2): "35",(9, 2): "36",(10, 2): "37",(11, 2): "38",(12, 2): "26",
                       (0, 3): "40",(1, 3): "41",(2, 3): "42",(3, 3): "43",(4, 3): "44",(5, 3): "45",(6, 3): "46",(7, 3): "47",(8, 3): "48",(9, 3): "49",(10, 3): "50",(11, 3): "51",(12, 3): "39"}

    def nomCarte(self, c):
        """Renvoie le nom de la carte (<c> doit être un tuple !!!)"""
        if self.carte != []:
            return str(self.valeur[c[0]])+" de "+str(self.couleur[c[1]])

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


class Ui_MainWindow_StartMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 352)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 0, 451, 161))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 130, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 210, 201, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 20, 71, 51))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 71, 51))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 240, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jeu De Carte"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "PlayerSelection"))
        self.radioButton_2.setText(_translate("MainWindow", "Joueur 2"))
        self.radioButton.setText(_translate("MainWindow", "Joueur 1"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "IP du second Joueur"))