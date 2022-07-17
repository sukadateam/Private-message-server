import os
path=os.path.dirname(os.path.realpath(__file__))
path=path.replace('\\','\\\\')
os.chdir(path)
file=open('directory.py','w')
file.write('path="'+str(path)+'"')
file.close()