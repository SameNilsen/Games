# Imports
import socket
import time
import random
import keyboard
import ipaddress
import time
import webbrowser
from PIL import ImageGrab

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
# Variables
lHost = "192.168.39.150"  # Server IP
port = 80  # Connection Port

# Connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
connected = False
while connected == False:
    try:
        s.connect((lHost, port))
        connected = True
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
#getInstructions()
# Functions
#print("----- Press 'Q' to write -----")

def send(msg):
    s.send(msg.encode("UTF-8"))



def reciveAction():
    while True:
        try:
            s.setblocking(False)
            msg = s.recv(4096)
            inst = msg.decode("UTF-8")
            print("Server:", inst)
        except:
            pass
        if keyboard.is_pressed("s"):
            try:
                s.setblocking(True)
            except:
                pass
            sendAction()

def sendAction():
    while True:
        # Instructions
        mld = input("Client: ")
        if mld == "r":
            reciveAction()
        send(mld)

def leik():
    webbrowser.open("https://youtu.be/NUYvbT6vTPs", new=1)

def screenshot():
    sc = ImageGrab.grab()
    sc.siz
    #sc.show()


def action():
    while True:
        try:
            s.setblocking(False)
            msg = s.recv(4096)
            inst = msg.decode("UTF-8")
            #print("Server:", inst)
            if inst == "leik":
                #print("hahaha")
                time.sleep(5)
                leik()
        except:
            pass
        """
        if keyboard.is_pressed("Q"):
            mld = input("Client: ")
            send(mld)
        """
action()
