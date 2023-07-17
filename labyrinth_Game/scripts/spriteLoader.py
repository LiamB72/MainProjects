from scripts.variables import *

if debugMod:
    fenetre = pygame.display.set_mode((width, height))
else:
    fenetre = pygame.display.set_mode((width, 326))

img0 = pygame.image.load("img_dungeon\\0.gif")
img0_1 = pygame.image.load("img_dungeon\\0-1.gif")
img0_2 = pygame.image.load("img_dungeon\\0-2.gif")
img0_3 = pygame.image.load("img_dungeon\\0-3.gif")
img1_1 = pygame.image.load("img_dungeon\\1-1.gif")
img1_2 = pygame.image.load("img_dungeon\\1-2.gif")
img1_3 = pygame.image.load("img_dungeon\\1-3.gif")
img2_1 = pygame.image.load("img_dungeon\\2-1.gif")
img2_2 = pygame.image.load("img_dungeon\\2-2.gif")
img2_3 = pygame.image.load("img_dungeon\\2-3.gif")
img3_1 = pygame.image.load("img_dungeon\\3-1.gif")
img3_2 = pygame.image.load("img_dungeon\\3-2.gif")
img4 = pygame.image.load("img_dungeon\\4.gif")
imgKey = pygame.image.load("img_dungeon\\key.gif")


def b01():
    fenetre.blit(img0_1, (0, 60))


def b02():
    fenetre.blit(img0_2, (278, 60))


def b03():
    fenetre.blit(img0_3, (149, 60))


# background 3
def b11():
    fenetre.blit(img1_1, (0, 49))


def b12():
    fenetre.blit(img1_2, (298, 49))


def b13():
    fenetre.blit(img1_3, (120, 49))


# background 2
def b21():
    fenetre.blit(img2_1, (0, 22))


def b22():
    fenetre.blit(img2_2, (328, 22))


def b23():
    fenetre.blit(img2_3, (64, 22))


# background 1
def b31():
    fenetre.blit(img3_1, (0, 0))


def b32():
    fenetre.blit(img3_2, (384, 0))
