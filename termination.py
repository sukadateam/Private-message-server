'''
1. This file only needs to activate once the kill code is understood/approved, and has been authorized to execute.
2. Before importing this file port: 8080, must be open, and if not, the process using it must be closed. No execptions.
3. This script cannot close open processes other than it's own. Since memory seperation on mac is a pain.
4. The host will not be able to recieve messages anymore after this file has been imported.
5. The host will be forced to send this message, 'SelfTermination', which will cause all clients to terminate.
'''
import socket
host = socket.gethostbyname(socket.gethostname())
port = 8080 #Takes over existing port.
v = socket.socket()
v.bind((host, port))
arr = bytes('SelfTermination', 'utf-8')
try:
    v.send(arr)
except BrokenPipeError:
    print('The server seems to be offline!')