"""
Programme réalisé par BERGE Liam, TG1 | Project Start: 19/11/2023 | Latest Edit: 23/11/2023
"""

from data.scripts.importedModules import *
from data.scripts.classes import Player

NB_TILES = 666
TITLE_SIZE=32 
largeur=8     
hauteur=8     
tiles=[]      
clock = pygame.time.Clock()

mapTiles=[[ 23, 24, 24, 24, 24, 24, 24, 25],
          [189,189,171, 47, 47, 47, 47, 48],
          [ 46, 47,187, 47, 47, 47, 47, 48],
          [ 46,118,217,120, 47, 47, 47, 48],
          [ 46,141,142,143, 47, 47, 47, 48],
          [ 46,164,165,166, 47, 47, 47, 48],
          [506,507,507,507,507,507,507,508],
          [529,486,486,486,486,486,486,531]]

decorationTiles=[[  0,  0,253,  0,  0,  0,  0,  0],
                 [  0,  0,  0,  0,  0,  0,  0,  0],
                 [184,  0,  0,138,  0,278,279,  0],
                 [  0,  0,  0,  0,  0,276,277,  0],
                 [  0,  0,  0,  0,  0,299,300,  0],
                 [186,  0,  0,  0,  0,  0,  0,  0],
                 [  0,  0,  0,  0,  0,  0,  0,  0],
                 [  0,  0,  0,  0,  0,  0,  0,  0]]

# 0 = NoCollision; 1 = Collisio
collisionsTiles= [[  1,  1,  1,  1,  1,  1,  1,  1],
                  [  1,  0,  0,  0,  0,  0,  0,  1],
                  [  1,  0,  0,  1,  0,  0,  0,  1],
                  [  1,  0,  0,  0,  0,  0,  0,  1],
                  [  1,  0,  0,  0,  0,  1,  1,  1],
                  [  1,  0,  0,  0,  0,  0,  0,  1],
                  [  1,  0,  0,  0,  0,  0,  0,  1],
                  [  1,  1,  1,  1,  1,  1,  1,  1]]




#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, hauteur*TITLE_SIZE))
pygame.display.set_caption("Dungeon")
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/images/'+str(n)+'.png'))


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        
        for x in range(largeur):
            
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
            
            if (decorationTiles[y][x]>0):
                
                fenetre.blit(tiles[decorationTiles[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))



def afficheScore(score):
    """
    affiche le score
    """
    #exemple bidon
    #scoreAafficher = font.render(str(score), True, (0, 255, 0))
    #fenetre.blit(scoreAafficher,(120,250))
    pass



fenetre.fill((0,0,0))   #efface la fenetre
chargetiles(tiles)  #chargement des images


perso =  Player([1,1],TITLE_SIZE, "data/images/perso.png", collisionsTiles, ["Hero", 10, 256, 0, 1])
perso2 = Player([3,3],TITLE_SIZE, "data/images/perso.png", collisionsTiles, ["Villain_1", 32, 32, 0, 1])
perso3 = Player([3,5],TITLE_SIZE, "data/images/perso.png", collisionsTiles, ["Villain_2", 128, 128, 0, 5])

aventuriers = pygame.sprite.Group()
aventuriers.add(perso)

mechants = pygame.sprite.Group()
mechants.add(perso2)
mechants.add(perso3)



loop=True

while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            
            if event.key == pygame.K_z:
                perso.haut()
                
            elif event.key == pygame.K_s:
                perso.bas()
                
            elif event.key == pygame.K_d:
                perso.droite()
                
            elif event.key == pygame.K_q:
                perso.gauche()
                
            elif event.key == pygame.K_BACKSPACE:
                loop = False
                
    col = pygame.sprite.collide_rect(perso, perso2)
    col2 = pygame.sprite.collide_rect(perso, perso3)
    
    if col:
        mechants.remove(perso2)
    if col2:
        mechants.remove(perso3)


    fenetre.fill((0,0,0))
    
    afficheNiveau(mapTiles)   #affiche le niveau
    
    aventuriers.update()
    aventuriers.draw(fenetre)
    
    mechants.update()
    mechants.draw(fenetre)
    
    pygame.display.update() #mets à jour la fentre graphique
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

