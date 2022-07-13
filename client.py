import socket
from functions import *
host=None
port=None
s=None

def SetConnection():
    global host, port, s
    #host = '192.168.1.93' #For a lan connection, use the router assigned ip address from the host computer(host.py file ip).
    host=socket.gethostbyname(socket.gethostname())
    #For a ota connection, use the hosts router public ip address. If no connection is made, then the host may need to open ports, and/or disable firewalls.
    port = 8080
    s = socket.socket()
def Main():
    SendMessages()
def SendMessages():
    message=''
    firstMessage=True
    while message != "!EMEXIT!":
        SetConnection()
        global host, port, s
        s.connect((host,port))
        if firstMessage==False:
            message=input('Speak Your Mind: ')
        if firstMessage==True:
            message=input('Enter Password: ')
            firstMessage=False
        arr = bytes(message, 'utf-8')
        s.send(arr)
if __name__ == '__main__':
    Main()