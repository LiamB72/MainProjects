from modules import JeuDeCartes, joueur

# Objective:
#   Goal : Beat the dealer
#   Go as closer to 21 than the dealer without going over
#   2 - 10 = Their respective face value
#   Jack, Queen, King = 10
#   Ace = 1/11 (Which is the best to the player (Being you/dealer))
#   How the game is done:
#   Two cards to each of the players and dealer
#   The players shows their cards, whilst the dealer only show one.
#   The players can, take more card, or stay with their current decK.
#   The dealer can also, take more card, or stay with their current decK.
#   If the player wins they get an equal amount to the initial bet.
#   If the player loses; they loses they're entire bet.
#   If the player pushes (get the equal amount of point than the dealer) = nor loses or wins

class BlackJack(JeuDeCartes):
    
    def __init__(self, cartes:list):
        
        super().__init__()      
        self.newList = []
        self.newList.extend(cartes)
        
        JeuDeCartes().battre(self.newList)
        
        self.moneyOnTheLine = str(input("Avec Argent Misé? (Y/N): "))
        if self.moneyOnTheLine == "Y":
            self.initialBet = float(input("Montant misé: "))
            self.currentBet = self.initialBet
        
        self.player = joueur("Joueur 1")
        self.plHand = self.player.deck
        self.plName = self.player.name
        self.dealer = joueur("Croupier")
        self.dlHand = self.dealer.deck
        self.dlName = self.dealer.name
        
        self.cardValue = {(x, y): x + 2 for x in range(9) for y in range(4)}
        self.cardValue.update({(x, y): 10 for x in range(9, 12) for y in range(4)})
        self.cardValue.update({(12, y): 11 for y in range(4)})

        self.run()

        
    def actionChoice(self):
        
        if self.moneyOnTheLine == "Y":
            pAct = input(f"\n{self.plName}: Hit (H) | Stand (S) | Double (D) | Split (SP): ")
            match pAct:
                case "H":
                    self.playerhAct()
                case "S":
                    self.playersAct()
                case "D":
                    self.dAct()
                case "SP":
                    self.spAct()
        else:
            pAct = input(f"\n{self.plName}: Hit (H) | Stand (S): ")
            match pAct:
                case "H":
                    self.playerhAct()
                case "S":
                    self.playersAct()
                    
        self.dealer
    
    def playerhAct(self):
        self.player.addCards(self.newList)
    
    def playersAct(self):
        self.player.intoName()
        return f"\n{self.plName} s'est couché(e) avec une main: {self.player.deckName}"
    
    def dAct(self):
        self.currentBet = self.initialBet * 2
        self.player.addCards(self.newList)
        
    def spAct(self):
        
        self.tempDeck1 = []
        self.tempDeck2 = []
        self.tempDeck3 = []
        self.tempDeck4 = []
          
        tempCard1 = self.player.addCards(self.newList)
        tempCard2 = self.player.addCards(self.newList)
        
        if tempCard1 != self.plHand[0] or tempCard2 != self.plHand[1]:
        
            self.tempDeck1.extend([self.plHand[0], self.plHand[2]])
            self.tempDeck2.extend([self.plHand[1], self.plHand[3]])
            
            self.plHand.pop(0)
            self.plHand.pop(1)

            res1 = self.calculatePoint(self.tempDeck1, self.dlHand)
            res2 = self.calculatePoint(self.tempDeck2, self.dlHand)
            # print("Split no.1:", ', '.join(map(str, res1))) # Converts the res1 into a str
            # print("Split no.2:", ', '.join(map(str, res2))) # Converts the res2 into a str
            
            if res1[0] > res2[0]:
                self.checkWinner(res1)
            elif res1[0] < res2[0]:
                self.checkWinner(res2)
                
        elif tempCard1 == self.plHand[0]:
            
            self.tempDeck1.extend([self.plHand[0], self.plHand[3]])
            self.tempDeck2.extend([self.plHand[1], self.plHand[4]])
            self.tempDeck2.extend([self.plHand[2], self.plHand[5]])

            self.plHand.pop(0)
            self.plHand.pop(1)
            self.plHand.pop(2)

            res1 = self.calculatePoint(self.tempDeck1, self.dlHand)
            res2 = self.calculatePoint(self.tempDeck2, self.dlHand)
            res3 = self.calculatePoint(self.tempDeck3, self.dlHand)

            if res1[0] > res2[0]:
                self.checkWinner(res1)
            elif res1[0] < res2[0]:
                self.checkWinner(res2)
                
            elif res1[0] > res3[0]:
                self.checkWinner(res1)
            elif res1[0] < res3[0]:
                self.checkWinner(res3)
                
            elif res2[0] > res3[0]:
                self.checkWinner(res2)
            elif res2[0] < res3[0]:
                self.checkWinner(res3)
            
    
    def dealerHAct(self):
        self.dealer.addCards(self.newList)
    
    def dealerSAct(self):
        self.dealer.intoName()
        return f"\n{self.dlName} s'est couché(e) avec une main: {self.dealer.deckName}"
    
    def checkWinner(self, res):
        print()
        results = res
        
        if results[0] > 21:
            if self.moneyOnTheLine == "N":
                return f"{self.plName} à dépassé(e) 21! {self.dlName} a gagné(e)."
            else:
                return f"{self.plName} à dépassé(e) 21! {self.dlName} a gagné(e). Tu as perdu(e) {self.currentBet}€."

        if results[1] > 21:
            if self.moneyOnTheLine == "N":
                return f"{self.dlName} à dépassé(e) 21! {self.plName} a gagné(e)."
            else:
                return f"{self.dlName} à dépassé(e) 21! {self.plName} a gagné(e). Tu as gagné(e) {self.currentBet}€."

        
        if results[0] > results[1]:
            if self.moneyOnTheLine == "Y":
                return f"{self.plName} a gagné(e) contre le dealer. Tu as gagné(e) {self.currentBet}€."
            else:
                return f"{self.plName} a gagné(e) contre le dealer."
        elif results[0] < results[1]:
            if self.moneyOnTheLine == "Y":
                return f"{self.dlName} a gagné(e) contre le joueur. Tu as perdu(e) {self.currentBet}€."
            else:
                return f"{self.dlName} a gagné(e) contre le joueur."
        
        elif results[0] == results[1]:
            return "Personne n'a gagné"
        
    def oneOreleven(self):
        for i in range(len(self.plHand)):
            
            if self.cardValue[self.plHand[i]] == 11:
                
                if self.cardValue[self.plHand[0]] + self.cardValue[self.plHand[1]] == 21:
                    break
                
                ask = int(input("L'as comte il comme 1 ou 11? :"))
            
                if ask == 1:
                    self.plHand[(1, self.plHand[i][1])][0] = self.plHand.pop(i)
    
    def calculatePoint(self, plHand:list, dlHand:list):
        
        res = []
        resPlayer = 0
        resDealer = 0
        
        for i in range(len(self.plHand)):
            resPlayer += self.cardValue[plHand[i]]
        
        for i in range(len(self.dlHand)):
            resDealer += self.cardValue[dlHand[i]]
            
        res.extend([resPlayer, resDealer])
        
        return res
    
    def run(self):
        
        for i in range(2):
            
            self.player.addCards(self.newList)
            self.dealer.addCards(self.newList)
        
        self.player.intoName()
        self.dealer.intoName()
        print(f'\nLa main du {self.plName} est: {(", ".join(self.player.deckName[i] for i in range(len(self.plHand))))}')
        print(f'La 2nd carte du {self.dlName} est: {self.dealer.deckName[1]}')
        
        self.actionChoice()
        self.oneOreleven()
        res = self.calculatePoint(self.plHand, self.dlHand)
        print(self.player)
        print(self.dealer)
        print(self.checkWinner(res))
        
        
blackJack = BlackJack(JeuDeCartes().carte)