"""
Simulateur de jeu de 52 cartes

Liam BERGE TG1 | 21/10/2023
"""
from time import sleep
from modulesFunction import JeuDeCartes, Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.currentCardA.setText("")
        self.currentCardB.setText("")
        self.images = JeuDeCartes().images
    
    def printCartesX(self, jeuX):
        print(jeuX.cartes())
        
    def printPacketX(self, packetX):
        
        print(packetX)
    
    def changeImageCarte(self, imagePathNameA:int, imagePathNameB:int):
        
        self.carteChoisieA.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameA)+".png"))
        self.carteChoisieB.setPixmap(QtGui.QPixmap("Resources/data/"+str(imagePathNameB)+".png"))
        
    def changeTexte(self, stringA:str, stringB:str):
        
        self.currentCardA.setText(stringA)
        self.currentCardB.setText(stringB)

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

        matchViewing = input("Regarder le match: (Y/N): ")
        matchViewing.capitalize()
        n = float(input("Vitesse du jeu (en secondes): "))
        roundNb = 0
        roundWinner = "Noone"
        
        carteJoueeA = jeuA.tirer()
        carteJoueeB = jeuB.tirer()

        while (comptA <= 103 and comptB <= 103):
            
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
            
            self.currentWinner.setText(f" Tour No.{roundNb} | Gagnant: {roundWinner}")
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
            sleep(n) 
            
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
                
                sleep(n)
                
                batailleA.append(carteJoueeA)
                batailleB.append(carteJoueeB)
                
                carteJoueeA = jeuA.tirer()
                carteJoueeB = jeuB.tirer()
                
                print(f"\njoueur 1 a tirer: {jeuA.nomCarte(carteJoueeA)}\njoueur 2 a tirer: {jeuB.nomCarte(carteJoueeB)}")
                sleep(n)    
                
                
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
            sleep(n)
            
            carteJoueeA = jeuA.tirer()
            carteJoueeB = jeuB.tirer()
            
            
        if comptA == 104:
            
            print("\n\nJoueur 1 a gagné!!")
            self.currentWinner.setText(f"Gagnant du jeu: Joueur 1")
            
        elif comptB == 104:
            
            print("\n\nJoueur 2 a gagné!!")
            self.currentWinner.setText(f"Gagnant du jeu: Joueur 2")

    def threadStart(self):
            
        gameThread = threading.Thread(target=self.run)
        gameThread.start()

def run():     
    run = int(input("Voir les Questions ou le jeu (1/2): "))
    return run

run = run()

if run == 1:
    
    #Q1 Initialisation de la classe « JeuDeCartes » : FAIT
    jeux = JeuDeCartes()
    print(f"\n\nQ1:{jeux.carte}")

    #Q2 Affichage du nom de la carte : FAIT
    jeux = JeuDeCartes()
    print("\n\nQ2:")
    print(jeux.nomCarte((1, 2)))
    print(jeux.nomCarte((12, 1)))

    #Q3 Battre les cartes : FAIT
    print("\n\nQ3:")
    jeux = JeuDeCartes()
    jeux.battre()
    print(jeux.carte)

    #Q4.1 Tirer une carte : FAIT
    print("\n\nQ4.1:")
    jeux = JeuDeCartes()
    jeux.battre()
    print(jeux.carte)
    c = jeux.tirer()
    print(jeux.nomCarte(c))
    print()
    print(jeux.carte)

    #Q4.2 Tirage de toutes le cartes: FAIT!
    print("\n\nQ4.2:")
    jeux = JeuDeCartes()
    jeux.battre()

    for n in range(53):
        c = jeux.tirer()
        print(jeux.nomCarte(c))

elif run == 2:
    
    app = QApplication([])
    window = Window()
    window.show()
    window.threadStart()
    app.exec()
    
else:
    run()