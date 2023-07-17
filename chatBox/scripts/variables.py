from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui,uic
from PyQt5.QtCore import QObject, pyqtSignal
import qdarkstyle
import sys
import socket
import os
import json

file_path = 'PyFolder\chatBox\Output\\file_Output.txt'

RECEIVER_IP = "127.0.0.1"
RECEIVER_PORT = 5000

SENDER_IP = "127.0.0.1"
SENDER_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((SENDER_IP, SENDER_PORT))

registeredUsers = {} #Create the dictionnary to register and associate the name and IP of the user
items = []
receiverNames = []
receiverIPs = []
name_bis = []
