import socket
#Temp vars. These do not hold any value yet.
#Used to allow global functions to operate
host=None
port=None
s=None
host1=None
port1=None
v=None
#End of Temp vars.
from settings import testExpermintalFeatures
from DestroyClient import *
import os
#host = '192.168.1.93' #For a lan connection, use the router assigned ip address from the host computer(host.py file ip).
#For a ota connection, use the hosts router public ip address. If no connection is made, then the host may need to open ports, and/or disable firewalls.
hostIP="127.0.0.1"

#Entering this command will kill the session!! Change to something memorable and easy to execute.
forceQuit='Exit'

def SetConnection():
    global host, port, s, hostIP
    host=hostIP
    port = 8080
    s = socket.socket()
def Main():
    preMessage()
def preMessage():
    global host, port, s
    SetConnection()
    s.connect((host,port))
    arr = bytes('LoginAttempt', 'utf-8')
    s.send(arr)
    SendMessages()
def SendMessages():
    message=''
    firstMessage=True
    while message != forceQuit:
        SetConnection()
        global host, port, s
        try:
            s.connect((host,port))
        except ConnectionRefusedError:
            print('Could not resolve connection failure. You might of\n (1)Entered the wrong password\n (2)Assigned the wrong port\n (3)Been to cute for me to handle!')
            message=forceQuit
            break
        if firstMessage==False:
            message=input('Speak Your Mind: ')
        elif firstMessage==True:
            message=input('Enter Password: ')
            firstMessage=False
        arr = bytes(message, 'utf-8')
        try:
            s.send(arr)
        except BrokenPipeError:
            print('The server seems to be offline!')
            message=forceQuit
    #os.system('clear') #May remove
if __name__ == '__main__':
    if testExpermintalFeatures == True:
        from DestroyClient import *
    DestroyClient.listen()
    Main()
