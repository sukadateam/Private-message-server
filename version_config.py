from settings import program_version
from directory import path
import os
os.chdir(path)
file=open('version.py','w')
file.write('setup_version = \''+program_version+"'")
file.close()