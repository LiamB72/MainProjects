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

file_path = 'Output\\file_Output.txt'

RECEIVER_IP = ""
RECEIVER_PORT = 5000

SENDER_IP = ""
SENDER_PORT = 5000



registeredUsers = {} #Create the dictionnary to register and associate the name and IP of the user
items = []
receiverNames = []
receiverIPs = []
name_bis = []
