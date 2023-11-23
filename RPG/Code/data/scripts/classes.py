if not (__name__ == "__main__"):
    from data.scripts.importedModules import *
else:
    from importedModules import *

class Player(pygame.sprite.Sprite):

    def __init__(self, position:list, size:int, img:str, collisions:list, stats:tuple=[str, int, int, int, int]):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        
        self.size = size
        
        self.collisions = collisions
        self.x, self.y = position
        
        self.rect.x = self.x * size
        self.rect.y = self.y * size
        
        self.nom         = stats[0]
        self.currentHP   = stats[1]
        self.maxHP       = stats[2]
        self.exp         = stats[3]
        self.niveau      = stats[4]
        
        self.requiredEXP = 100

    def healPlayer(self, a0:int):
        """
        Player's HP (Health Points) is increase by a0. Whilst staying under the maxHP.\n
        Otherwise is set to maxHP
        """
        while self.currentHP + a0 <= self.maxHP:
            
            self.currentHP += a0
            
        if self.currentHP + a0 > self.maxHP:
            
            self.currentHP = self.maxHP
            
    def damagePlayer(self, a0:int):
        """
        Player's HP (Health Points) is reduced by a0. Whilst staying over 0.
        """
        while self.currentHP - a0 < 0:
            
            self.currentHP -= a0
            
    def increaseEXP(self, a0:int, a1:int, a2:int):
        """
        Increases the experience points of the player by a0 amount (int)\n
        If player has increase in LV, it increased a1 given by a2 amount.
        """
        if self.exp < self.requiredEXP:
            self.exp += a0
        
        else:
            self.exp = (self.exp + self.a0) - self.requiredEXP
            self.requiredEXP += 100
            a1 += a2
            
    
    def checkStatus(self) -> bool:
        """
        Return True if the player's HP is still over 0.\n
        Return False otherwise.
        """
        return True if self.currentHP > 0 else False
    
#if self.currentHP - a0 == 0:
            
# self.currentHP = 0
# print("Player lost. Closing game...\nIf you wish to play again, please restart the game.")
# print("Player going a mimir")
    
    def testCollisionsDecor(self,x,y):
        
        if self.collisions[self.y+y][self.x+x] == 0:
            
            self.x += x
            self.y += y

    def droite(self):
        
        self.testCollisionsDecor(1,0)
        self.rect.x = self.x * self.size

    def gauche(self):
        
        self.testCollisionsDecor(-1,0)
        self.rect.x = self.x * self.size

    def haut(self):
        
        self.testCollisionsDecor(0,-1)
        self.rect.y = self.y * self.size

    def bas(self):
        
        self.testCollisionsDecor(0,1)
        self.rect.y = self.y * self.size


class Warrior(Player):
    """
    inflige des dégats au mechant si celui-ci est vivant\n
    incrémente le nombre de points d'expérience correspondant aux dégâts infligés\n
    Monte si nécessaire en niveau en fonction du nombre de points xp\n
    retire de la vie au méchant\n
    Si le guerrier monte en niveau il augement d'un point de force.
    """
    
    def __init__(self, nom, vie, xp, niveau, strength):
        
        super().__init__(nom, vie, xp, niveau)
        
        self.strength = strength
    
    def combat(self, opponent):
        
        attack_strenght = randint(1, 4)
        damage = int(attack_strenght * self.niveau * 2 - opponent.niveau)
        
        if opponent.hp - damage >= 0 and self.mana > 0:
            opponent.hp -= damage
            print("dégâts du chevalier sur le méchant est de ",damage)
        else:
            opponent.hp = 0
            print("lL'adversaire est mort.")
            self.increaseEXP(randint(10, 40), self.maxMana, 10)
            
class Wizard(Player):
    """
    Inflige des dégats au mechant si celui-ci est vivant et que le magicien dispose de mana.\n
    Incrémente le nombre de points d'expérience.\n
    Monte si nécessaire en niveau en fonction du nombre de points xp.\n
    Retire de la vie au méchant et diminue de 1 self.mana (consommation de magie)\n
    Si le méchant est mort augmenter self.maxMana de 10 du magicien.
    """
    
    def __init__(self, nom, mana, vie, xp, niveau):
        super().__init__(nom, vie, xp, niveau)
        self.maxMana = mana
        self.mana = mana
    
    def ajouterMana(self):
        #ajoute 1 en self.mana sans dépasser self.maxMana
        if self.mana + 1 <= self.maxHP:
            self.mana += 1
        else:
            print("Capacité max de mana déjà atteinte.")
    
    def retirerMana(self,mana):
        #retire mana à self.mana sans descendre en dessous de 0
        #retourne vrai si le magicien à lancé un sort
        #retourne faux si le magicien ne peut plus lancer de sort
        if self.mana - 1 >= 0:
            
            self.mana -= 1
            return True
        
        else:
            print("Plus de mana.")
            return False
            
    def combat(self,opponent):
        
        attack_strenght = randint(1, 1)
        damage = int(attack_strenght * self.niveau * 2 - opponent.niveau)
        print(damage)
        if attack_strenght == 1 and self.mana > 0:
            
            damage -= damage * 2
            self.currentHP -= damage
            print(damage)
        
        elif opponent.hp - damage > 0 and self.mana > 0 and attack_strenght > 1:
            opponent.hp -= damage
            self.mana -= 1
            print("dégâts du magicien sur le méchant est de ",damage)
        elif opponent.hp - damage <= 0 and self.mana > 0 and attack_strenght > 1:
            opponent.hp = 0
            print("L'adversaire est mort.")
            self.increaseEXP(randint(10, 40), self.maxMana, 10)
