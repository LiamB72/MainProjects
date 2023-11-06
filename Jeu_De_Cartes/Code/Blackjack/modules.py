from random import shuffle

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

    def nomCarte(self, a0:tuple):
        """Renvoie le nom de la carte """
        if self.carte != []:
            return f"{self.valeur[a0[0]]} de {self.couleur[a0[1]]}"

    def battre(self, cartes:list):
        """Mélange les cartes"""
        shuffle(cartes)

    def tirer(self, cartes:list):
        """Retire une carte du jeu"""
        if cartes != []:
            
            carteTirer = cartes[0]
            del(cartes[0])
            
        else:
            print("Plus de cartes")
        
        return carteTirer


class Joueur:
    
    def __init__(self, name:int):
        
        self.name = name
        self.deck = []
        self.deckName = []
        
    def addCards(self, cards:list):
        
        self.deck.append(JeuDeCartes().tirer(cards))
        
    def intoName(self):
        self.deckName.clear()
        for i in range(len(self.deck)):
            
            self.deckName.append(JeuDeCartes().nomCarte(self.deck[i]))
        
    def __repr__(self):
        self.intoName()
        return f"La main du {self.name} est : {', '.join(self.deckName)}"