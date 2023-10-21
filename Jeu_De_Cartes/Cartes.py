"""
Simulateur de jeu de 52 cartes

Liam BERGE TG1 | 21/10/2023 - Q5+Q6 Fini le 22/10/2023 à 00:33
"""
from time import sleep
from function import JeuDeCartes, Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.currentCardA.setText("Carte Actuel: PLACEHOLDER")
        self.currentCardB.setText("Carte Actuel: PLACEHOLDER")
        self.images = {(0, 0): "01",(1, 0): "02",(2, 0): "03",(3, 0): "04",(4, 0): "05",(5, 0): "06",(6, 0): "07",(7, 0): "08",(8, 0): "09",(9, 0): "10",(10, 0): "11",(11, 0): "12",(12, 0): "00",
                       (0, 1): "14",(1, 1): "15",(2, 1): "16",(3, 1): "17",(4, 1): "18",(5, 1): "19",(6, 1): "20",(7, 1): "21",(8, 1): "22",(9, 1): "23",(10, 1): "24",(11, 1): "25",(12, 1): "13",
                       (0, 2): "27",(1, 2): "28",(2, 2): "29",(3, 2): "30",(4, 2): "31",(5, 2): "32",(6, 2): "33",(7, 2): "34",(8, 2): "35",(9, 2): "36",(10, 2): "37",(11, 2): "38",(12, 2): "26",
                       (0, 3): "40",(1, 3): "41",(2, 3): "42",(3, 3): "43",(5, 3): "44",(4, 3): "45",(6, 3): "46",(7, 3): "47",(8, 3): "48",(9, 3): "49",(10, 3): "50",(11, 3): "51",(12, 3): "39"}
        
    def changeImageCarte(self, imagePathNameA, imagePathNameB):
        
        self.carteChoisieA.setPixmap(QtGui.QPixmap("data/"+str(imagePathNameA)+".png"))
        self.carteChoisieB.setPixmap(QtGui.QPixmap("data/"+str(imagePathNameB)+".png"))
        
    def changeTexte(self, stringA, stringB):
        
        self.currentCardA.setText(str(stringA))
        self.currentCardB.setText(str(stringB))

    def run(self):
        
        #Q5 Simuler un jeu de bataille entre 2 joueurs (robots)
        jeuA = JeuDeCartes()
        jeuB = JeuDeCartes()

        jeuA.battre()
        jeuB.battre()

        comptA = 0
        comptB = 0

        # Cartes remportées après un pli
        packetA = [] 
        packetB = [] 

        # Cartes durant une bataille (-> lorsque les deux joueurs pose une carte de valeur similaire)
        batailleA = []
        batailleB = []

        HumanWatching = True
        roundNb = 0
        roundWinner = "Noone"

        while (comptA <= 103 and comptB <= 103):
            
            carteJoueeA = jeuA.tirer()
            carteJoueeB = jeuB.tirer()
            
            self.currentWinner.setText(f"Round No.{roundNb} | WINNER: {roundWinner}")
            self.changeImageCarte(self.images[carteJoueeA], self.images[carteJoueeB])
            self.changeTexte(jeuA.nomCarte(carteJoueeA),jeuB.nomCarte(carteJoueeB))
            roundNb += 1
            
            if jeuA.nomCarte(carteJoueeA) == None:
                
                for i in range(len(packetA)):
                    jeuA.carte.append(packetA[i])
                packetA.clear()
                
                carteJoueeA = jeuA.tirer()
                
                
            elif jeuB.nomCarte(carteJoueeB) == None:
                
                for j in range(len(packetB)):
                    jeuB.carte.append(packetB[j])
                packetB.clear()
                
                carteJoueeB = jeuB.tirer()
            
            print(f"\njoueur 1 a tirer: {jeuA.nomCarte(carteJoueeA)}\njoueur 2 a tirer: {jeuB.nomCarte(carteJoueeB)}")
            if HumanWatching:
                sleep(2)
            
            if carteJoueeA[0] > carteJoueeB[0]:
                
                packetA.append(carteJoueeA)
                packetA.append(carteJoueeB)
                comptA += 1
                roundWinner = "Joueur 1"
                
            elif carteJoueeB[0] > carteJoueeA[0]:
                
                packetB.append(carteJoueeA)
                packetB.append(carteJoueeB)
                comptB += 1
                roundWinner = "Joueur 2"
                
            elif carteJoueeA[0] == carteJoueeB[0]:
                
                print("\n**************************\nBATAILLE!\n**************************")
                
                self.currentWinner.setText(f"Bataille !!!")
                
                if HumanWatching:
                    sleep(3)
                
                batailleA.append(carteJoueeA)
                batailleB.append(carteJoueeB)
                
                carteJoueeA = jeuA.tirer()
                carteJoueeB = jeuB.tirer()
                
                print(f"\njoueur 1 a tirer: {jeuA.nomCarte(carteJoueeA)}\njoueur 2 a tirer: {jeuB.nomCarte(carteJoueeB)}")
                if HumanWatching:
                    sleep(2)
                
                if carteJoueeA[0] > carteJoueeB[0]:
                
                    packetA.append(carteJoueeA)
                    packetA.append(carteJoueeB)
                    packetA.append(batailleA[0])
                    packetA.append(batailleB[0])
                    
                    batailleA.clear()
                    batailleB.clear()
                    
                    comptA += 1
                    roundWinner = "Joueur 1"

                elif carteJoueeB[0] > carteJoueeA[0]:

                    packetB.append(carteJoueeA)
                    packetB.append(carteJoueeB)
                    packetB.append(batailleA[0])
                    packetB.append(batailleB[0])
                    
                    batailleA.clear()
                    batailleB.clear()
                    
                    comptB += 1
                    roundWinner = "Joueur 2"
                    
            print(f"\n{roundWinner} a remporté le pli\n")
            print(f"\nLes scores sont:")
            print(f"Joueur 1: {comptA} ------- Joueur 2: {comptB}\n")
            self.scoreA.setText(f"Score: {comptA}")
            self.scoreB.setText(f"Score: {comptB}")
            if HumanWatching:
                sleep(2)
            
            #print("JeuA: ",jeuA.carte,"\n---------\nJeuB: ", jeuB.carte)
            #print("\n\nPacketA:",packetA, "\n---------\nPacketB:",packetB)
            
        if comptA == 104:
            
            print("\n\nJoueur 1 a gagné!!")
            self.roundWinner.setText(f"Gagnant du jeu: Joueur 1")
            
        elif comptB == 104:
            
            print("\n\nJoueur 2 a gagné!!")
            self.roundWinner.setText(f"Gagnant du jeu: Joueur 2")

    def threadStart(self):
            
        gameThread = threading.Thread(target=self.run)
        gameThread.start()

       
"""
#Q1 Initialisation de la classe « JeuDeCartes » : FAIT
jeux = JeuDeCartes()
print(jeux.carte)

#Q2 Affichage du nom de la carte : FAIT
jeux = JeuDeCartes()
jeux.nomCarte((1, 2))
jeux.nomCarte((12, 1)) 

#Q3 Battre les cartes : FAIT
#jeux = JeuDeCartes()
#jeux.battre()
#print(jeux.carte)

#Q4.1 Tirer une carte : FAIT
#jeux = JeuDeCartes()
#jeux.battre()
#print(jeux.carte)
#c = jeux.tirer()
#print(jeux.nomCarte(c))
#print()
#print(jeux.carte)

#Q4.2 Tirage de toutes le cartes : FAIT
#jeux = JeuDeCartes()
#jeux.battre()
#
#for n in range(53):
#    c = jeux.tirer()

"""
#Q5 : FAIT
app = QApplication([])
window = Window()

window.show()
window.threadStart()

app.exec()
