# imports
import socket
import os
import keyboard
# Variables
port = 80

#keyboard.wait("esc")
# Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Starting Server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, port))
serversocket.listen(1)

clear()
print("-:-:-:-:-:PyRat Server:-:-:-:-:-")
clientsocket, addr = serversocket.accept()
print("Connection from: " + str(addr))
print("----- Press 's' to send or 'r' to receive -----")

def sendAction():
    while True:
        msg = input("Server: ")
        if msg == "r":
            reciveAction()
        if msg == "help":
            clear()
            print("-+-+-+-+-+HELP+-+-+-+-+-")
            print("Test Connection: 'test'")

            input("\nPress ENTER to continue")
            clear()
            print("-:-:-:-:-:PyRat Server:-:-:-:-:-")

        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
def reciveAction():
    while True:
        try:
            clientsocket.setblocking(False)
            msg = clientsocket.recv(4096)
            print("Client: ", msg.decode("UTF-8"))
        except socket.error:
            pass
        if keyboard.is_pressed("s"):
            try:
                serversocket.setblocking(True)
            except:
                pass
            sendAction()


def action():
    a = input("send or recive? (s/r)")
    if a == "s":
        sendAction()
    if a == "r":
        reciveAction()
reciveAction()
