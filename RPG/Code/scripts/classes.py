from scripts.importedModules import *

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
        
        self.nom     = stats[0]
        self.currentHP     = stats[1]
        self.maxHP  = stats[2]
        self.exp      = stats[3]
        self.niveau  = stats[4]
        
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
            
    def increaseEXP(self, a0:int, stat):
        """
        Increases the experience points of the player by a0 amount (int)\n
        If player has increase in LV, it increased a stat given.
        """
        if self.exp < self.requiredEXP:
            self.exp += a0
        
        else:
            self.exp = (self.exp + self.a0) - self.requiredEXP
            self.requiredEXP += 100
            stat += 1
            
    
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
    s̴i̴ ̴l̴e̴ ̴m̴é̴c̴h̴a̴n̴t̴ ̴e̴s̴t̴ ̴m̴o̴r̴t̴ ̴a̴u̴g̴m̴e̴n̴t̴e̴r̴ ̴l̴a̴ ̴f̴o̴r̴c̴e̴ ̴d̴e̴ ̴1̴ ̴d̴u̴ ̴g̴u̴e̴r̴r̴i̴e̴r̴\n
    Si le guerrier monte en niveau il augement d'un point de force.
    """
    
    def __init__(self, nom, vie, xp, niveau, strength):
        
        super().__init__(nom, vie, xp, niveau)
        
        self.strength = strength
    
    def StrengthIncrease(self):
        
        self.strength += 1
    
    def combat(self, opponent):
        
        attackStrength = randint(1, 4)
        
        damagePoints = attackStrength * self.niveau * self.strength - opponent.niveau
        if opponent.currentHP - damagePoints > 0:
            print(f"Damage Inflit to {opponent}: {damagePoints}")
            opponent.currentHP -= damagePoints
            
        elif opponent.currentHP - damagePoints <= 0:
            
            self.increaseEXP(randint(10, 40), self.strength)