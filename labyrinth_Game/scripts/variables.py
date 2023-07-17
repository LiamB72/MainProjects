import pygame
import csv
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui, uic
import sys

NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLANC = (255, 255, 255)
CARRE = 18

width = 448
height = 640


unlockedKeys = 0

mapLayout = []
mapNb = 1

startTime = False
stopClock = 0
timeNow = 0
showMap = 0

### if will to remove debug mode please set "debugMod to False"

debugMod = False
difficulty = 1

if (difficulty == 1):
    d = 2
    x = 1
    y = 7
elif (difficulty == 2):
    d = 0
    x = 13
    y = 6
