import socket
host=None
port=None
s=None
host1=None
port1=None
v=None
from settings import testExpermintalFeatures
import os
#host = '192.168.1.93' #For a lan connection, use the router assigned ip address from the host computer(host.py file ip).
#For a ota connection, use the hosts router public ip address. If no connection is made, then the host may need to open ports, and/or disable firewalls.
hostIP="127.0.0.1"

#Entering this command will kill the session!! Change to something memorable and easy to execute.
forceQuit='Exit'
import threading

##
def SetKillConnection():
    global host1, port1, v, hostIP
    host=hostIP
    port = 8081
    v = socket.socket()
    v.connect((host,port))
    v.listen(1)
    c, addr = v.accept()
    data = c.recv(1024)
    if data=="SelfTermination":
        KillConnection()

def KillConnection():
    global host1, port1, v
    s.close()
    os.system('clear')
    os.system('reset')
#
class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()
    def run(self):
        global host1, port1, v, hostIP
        host=hostIP
        port = 8081
        v = socket.socket()
        v.connect((host,port))
        v.listen(1)
        c, addr = v.accept()
        data = c.recv(1024)
        if data=="SelfTermination":
            KillConnection()
t1=MyThread()
def SetConnection():
    global host, port, s, hostIP
    host=hostIP
    port = 8080
    s = socket.socket()
def Main():
    global testExpermintalFeatures
    if testExpermintalFeatures == True:
        t1.start()
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
    Main()
