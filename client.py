import socket
host=None
port=None
s=None
im
forceQuit='Exit'
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
    while message != forceQuit:
        SetConnection()
        global host, port, s
        try:
            s.connect((host,port))
        except ConnectionRefusedError:
            print('Could not resolve connection failure. You might of/be, (1)Entered the wrong password, (2)Assigned the wrong port, or (3)To cute for me')
            message=forceQuit
            break
        if firstMessage==False:
            message=input('Speak Your Mind: ')
        if firstMessage==True:
            message=input('Enter Password: ')
            firstMessage=False
        arr = bytes(message, 'utf-8')
        try:
            s.send(arr)
        except BrokenPipeError:
            print('The server seems to be offline!')
            message=forceQuit
if __name__ == '__main__':
    Main()
