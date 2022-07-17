#0.6.7
from platform import python_version
from ast import Bytes
from dis import show_code
from email.encoders import encode_7or8bit
from ftplib import error_reply
from io import BytesIO
from json import tool
from re import L
import sys, os
from os import stat
from os import remove, walk
from typing import Set
from venv import create
from xmlrpc.client import FastMarshaller
import zipfile
from numpy import True_, int32
from pandas import *
from barcode import EAN13
from barcode.writer import ImageWriter
import time
import qrcode
import ctypes #Expermintal
from screeninfo import get_monitors
#ctypes.CDLL('libfoo.so').your_function(arguemnts)
try:
    #Windows print
    #Pylance may show this as a problem if your using mac. It's only for windows. Hence the try and except.
    import win32api
    import win32print
except:
    pass
from io import BytesIO
startupCount=time.time()
memory_hash=''
n = list(sys.argv)
from zipfile import ZipFile
try:
    from count import backup_count
except:
    pass
try:
    from multiprocessing import Process
except:
    pass
from settings import quiteStartup
if quiteStartup == False:
    for i in range(100):
        print('')
try:
    from pyAesCrypt import decryptFile, encryptFile
except:
    print('Please manually install all required items in requirements.txt.')
    sys.exit()
password=None
try:
    from settings import *
except:
    print('Cannot Find settings.py File. File is required for startup.')
    sys.exit()
try:
    import get_directory
except:
    print('Cannot Find get_directory.py File. File is required for startup.')
    sys.exit()
try:
    import version_config
except:
    print('Cannot Find version_config.py File. File is required for startup.')
    sys.exit()
systemDetectedOperatingSystem=None
list1=[]
try:
    from history_desc import *
except:
    if quiteStartup == False:
        print('Could not find the required file: history_desc.py You may experience problems.')
if quiteStartup == False:
    print('This Project is hosted on github. github.com/sukadateam')
    print('If problems occur, try to check if a new version exists.')
    print('-or- Create/Mark An Issue On GitHub!\n\n')
if python_version() not in required_version and "-skipPythonCheck" not in n and skip_pythonCheck==False:
    print('Required python version:', required_version)
    print('Current python version:', python_version)
    sys.exit()
if skip_pythonCheck==True:
    n.append('-skipPythonCheck')
if python_version() in required_version or "-skipPythonCheck" in n:
    from pyAesCrypt import decryptFile, encryptFile
    if "resetCollections" not in locals() or "resetCollections" not in globals():
        resetCollections=False
    if "auto_filter_profanity_speedBoost" not in locals() or "auto_filter_profanity_speedBoost" not in globals():
        auto_filter_profanity_speedBoost=False
    #Used for history file.
    from datetime import date
    today=date.today()
    d1 = today.strftime("%m/%d/%Y")
    #The Alphabet
    alphabet='abcdefghijklmnopqrstuvwxyz'
    from settings import *
    import random, shutil
    try:
        from directory import path
        if quiteStartup == False:
            print('Set path:', path)
        os.chdir(path)
    except ModuleNotFoundError:
        if quiteStartup == False:
            print('custom_database is not setup. Please setup with .bat or .sh file to enable this program.')
        exit()
    import_type='None'
    if quiteStartup == False:
        print('Python Version:', python_version())
    try:
        if dont_load_save==False:
            if quiteStartup == False:
                print('Please wait. Importing save file...')
            from data_save import *
            import_type='data_save'
        if dont_load_save==True:
            if quiteStartup == False:
                print('Please wait. Importing default file...')
            from data import *
            import_type='data'
    except Exception as ErrorMessage:
        print(ErrorMessage)
        try:
            from data import *
            import_type='data'
        except:
            if quiteStartup == False:
                print('Cannot Load Save File or Default file. This program cannot run without it.')
            exit()
    if import_type=="data":
        if quiteStartup == False:
            print('Import type: Default')
    if import_type=="data_save":
        if quiteStartup == False:
            print('Import type: Save file')
    #On some devices this import line may say could not import, but it will if the package is installed on a compatible python version.
    try:
        import pyAesCrypt
    except:
        if quiteStartup == False:
            print("Couldn't import pyAesCrypt")
    if os.path.exists('libfoo.so')==False:
        print('\nTo compile a shared .so file from hello.cpp run:\ng++ -c -o library.o hello.cpp\ng++ -shared -o libfoo.so library.o\n')
    def GetScreenHeight():
        for m in get_monitors():
            return int(m.height)
        if debug==True:
            print("Could not retrieve screen Height")
        return False
    def GetScreenWidth():
        for m in get_monitors():
            return int(m.width)
        if debug==True:
            print("Could not retrieve screen Width")
        return False
    def assignBarcodesToItemsWithout():
        #Adds called function to history.
        history.create_history('Run', 'assignBarcodesToItemsWithout()', hide=debug)
        for i in range(len(row)):
            if (row[i])[0] == "tools":
                if ((row[i])[1])[2]=='':
                    a=True
                    while a==True:
                        abc=''
                        #Generates the new Barcode/Serial
                        for x in range(8):
                            abc+=random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')
                        #Checks to see if new Barcode/Serial exists. If so repeat, if not assign it.
                        if check.barcode(abc)==True:
                            #Assigns the new Barcode/Serial
                            ((row[i])[1])[2]=abc
                            a=False
    def BrokenTool(input):
        #Marks a tool as broken.
        for i in range(len(row)):
            if (row[i])[0]=="tools":
                if save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)==input:
                    try:
                        #Changes a Value to True
                        ((row[i])[1])[6]=True
                    except Exception as ErrorHandle:
                        if debug==True:
                            #Prints the error if one occurs.
                            print(ErrorHandle)
        return False
    class print_instructions:
        def help():
            print('Branches:\n  print_instructions.print()\n  print_instructions.createBarcode()')
        def print(file_name, rmFileAfterPrint=False):
            history.create_history('Run', 'print_instructions.print()', hide=debug)
            if printer_debug==True:
                print('Sending Print Command...')
            #For Linux and macOS
            if systemDetectedOperatingSystem !="windows":
                print_cmd = 'lpr -P %s %s'
                os.system(print_cmd % (printer_name, file_name))
            #For Windows :)
            if systemDetectedOperatingSystem == "windows":
                win32api.ShellExecute(
                    0,
                    "print",
                    file_name,
                    '/d:"%s"' % win32print.GetDefaultPrinter(),
                    ".",
                    0
                )
            #Remove File So It doesn't mess things up when trying to create one.
            if rmFileAfterPrint==True:
                if printer_debug==True:
                    print("Removing Old File...")
                os.remove(file_name)
        def printAllToolsBarcodes():
            #This Process will only go as fast as the printer.
            for i in range(len(row)):
                if (row[i])[0]=="tools":
                    print_instructions.createBarcode(str(((row[i])[1])[2]), qr_code=True)
                    print_instructions.print(file_name="barcode.png")
        def createBarcode(barcode1, file_name='barcode', qr_code=False, barcode=False):
            history.create_history('Run', 'print_instructions.createBarcode()', hide=debug)
            #File is saved at png.
            if os.path.exists(file_name+'.png')==True:
                os.remove(file_name+'.png')
            if qr_code==True and barcode==True:
                if printer_debug==True:
                    print("Please only select EITHER qr_code or barcode.")
            else:
                if qr_code==True:
                    qr = qrcode.QRCode(
                        version=1,
                        box_size=10,
                        border=5)
                    qr.add_data(str(barcode1))
                    qr.make(fit=True)
                    img = qr.make_image(fill='black', back_color='white')
                    img.save(str(file_name)+'.png')
                elif barcode==True:
                    if isinstance(barcode1, int)==True:
                        from barcode import EAN13
                        my_code = EAN13(barcode)
                        my_code.save(str(file_name))
                    else:
                        if printer_debug==True:
                            print('Barcodes must be numbers.')
    class setupDatabaseWithSpreadSheet:
        def help():
            print('Branches:\n  setupDatabaseWithSpreadSheet.run()\n  setupDatabaseWithSpreadSheet.getAll()')
        def run(hide=False):
            #Imports a compatible spread sheet and imports it into the database.
            history.create_history('Run', 'setupDatabaseWithSpreadSheet.run()', hide=hide)
            toolType, toolName, serialNumber, modelNumber, purchaseDate, loanedTo = setupDatabaseWithSpreadSheet.getAll()
            for i in range(len(toolType)):
                list3=[toolType[i], toolName[i], serialNumber[i], modelNumber[i], purchaseDate[i], loanedTo[i]]
                for x in range(len(list3)):
                    if type(list3[x]) == float:
                        list3[x]=" "
                        print(list3[x])
                #Adds the new data to the database.
                data_base.edit.add_row(data_base='tools', new_row=[str(list3[0]).encode(encoding='UTF-8',errors='strict'), str(list3[1]).encode(encoding='UTF-8',errors='strict'),str(list3[2]).encode(encoding='UTF-8',errors='strict'), str(list3[3]).encode(encoding='UTF-8',errors='strict'), str(list3[4]).encode(encoding='UTF-8',errors='strict'), str(list3[5]).encode(encoding='UTF-8',errors='strict'), False], split=False)
            assignBarcodesToItemsWithout()
        def getAll(hide=False):
            #Grabs all the data from the spread sheet.
            history.create_history('Run', 'setupDatabaseWithSpreadSheet.getAll()', hide=hide)
            data=read_csv("tools.csv")
            toolType=data['Tool Type'].tolist()
            toolName=data['Tool Name'].tolist()
            serialNumber=data['Serial Number'].tolist()
            modelNumber=data['Model Number'].tolist()
            purchaseDate=data['Purchase Date'].tolist()
            loandedTo=data['Loaned out to'].tolist()
            return toolType, toolName, serialNumber, modelNumber, purchaseDate, loandedTo
    class logic:
        class gate:
            def help():
                history.create_history('Run', 'logic.gate.help()', hide=debug)
                print('Branches:\n  logic.gate.not_gate()\n  logic.gate.and_gate()\n  logic.gate.or_gate()')
            def xor_gate(input1, input2):
                history.create_history('Run', 'logic.gate.xor_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    try:
                        return ctypes.CDLL('libfoo.so').xor_gate(input1, input2)
                    except:
                        print(errors.MissingCPP())
                else:
                    if input1 == 0 and input2 == 0:
                        return 0
                    elif input1 == 1 and input2 == 1:
                        return 0
                    elif input1 == 0 and input2 == 1:
                        return 1
                    elif input1 == 1 and input2 == 0:
                        return 1
                    elif input1 == False and input2 == False:
                        return False
                    elif input1 == True and input2 == True:
                        return False
                    elif input1 == False and input2 == True:
                        return True
                    elif input1 == True and input2 == False:
                        return True
                    else:
                        return "None"
            def not_gate(input1):
                history.create_history('Run', 'logic.gate.not_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    if (type(input1)) == int:
                        try:
                            return ctypes.CDLL('libfoo.so').not_gate(input1)
                        except:
                            print(errors.MissingCPP())
                    if (type(input1)) == bool:
                        try:
                            return ctypes.CDLL('libfoo.so').not_gateBool(str(input1))
                        except:
                            print(errors.MissingCPP())
                if UtilizeCPPCode==False:
                    if input1==1:
                        return 0
                    if input1==0:
                        return 1
                    if input1==True:
                        return False
                    if input1==False:
                        return True
            def and_gate(input1, input2):
                history.create_history('Run', 'logic.gate.and_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    if type(input1) == int and type(input2) == int:
                        try:
                            return ctypes.CDLL('libfoo.so').and_gate(input1, input2)
                        except:
                            print(errors.MissingCPP())
                    else:
                        #If input(s) are not integers :)
                        if input1 == False and input2 == False:
                            return False
                        if input1 == True and input2 == True:
                            return True
                        if input1 == True and input2 == False:
                            return False
                        if input1 == False and input2 == True:
                            return False
                if UtilizeCPPCode==False:
                    if input1 == 0 and input2 == 0:
                        return 0
                    if input1 == 1 and input2 == 1:
                        return 1
                    if input1 == 1 and input2 == 0:
                        return 0
                    if input1 == 0 and input2 == 1:
                        return 0
                    if input1 == False and input2 == False:
                        return False
                    if input1 == True and input2 == True:
                        return True
                    if input1 == True and input2 == False:
                        return False
                    if input1 == False and input2 == True:
                        return False
            def or_gate(input1, input2):
                history.create_history('Run', 'logic.or_gate()', hide=debug)
                if input1 == 0 and input2 == 0:
                    return 0
                if input1 == 1 or input2 == 1:
                    return 1
                if input1 == False and input2 == False:
                    return False
                if input1 == True or input2 == True:
                    return True
    class safe_exit:
        def help():
            print('Branches:\n  safe_exit.close()\n  safe_exit.RmExcessFiles()')
        def close(create_backup=True, encryption_passw=None, hide=False, random_name=False, backup_name=None):
            history.create_history('Run', 'safe_exit.close()', hide=debug)
            print('Safe Exit Protocol In Action! DO NOT CLOSE APPLICATION!')
            safe_exit.RmExcessFiles()
            if create_backup==True:
                try:
                    if backup.create(password=encryption_passw, hide=hide, random_name=random_name, backup_name=backup_name) != "WrongPassword":
                        print('Application Safely Closed. App will force quit in 5 seconds.')
                        time.sleep(5)
                except:
                    pass
            exit()
        def RmExcessFiles():
            history.create_history('Run', 'safe_exit.RmExcessFiles()', hide=debug)
            #Clean files and folders.
            try: shutil.rmtree('collections')
            except: pass
            try: os.remove('hash.txt')
            except: pass
            try: os.remove('hash_other.txt')
            except: pass
    class save_in_txtFile:
        def help():
            print('Branches:\n  save_in_txtFile.remove_files()\n  save_in_txtFile.itemsNotSignedOut()\n  save_in_txtFile.students()\n  save_in_txtFile.logs()\n  save_in_txtFile.students()\n  save_in_txtFile.tools()')
        def remove_files(hide=False):
            history.create_history('Run', 'save_in_txtFile.remove_files()', hide=debug)
            os.chdir(path)
            if os.path.exists('collections')==True:
                os.chdir('collections')
                history.create_history('Null', 'Remove Files In Collections Folder', hide=hide)
                #Remove any and all files created by this class.
                file=['student_logs.txt', 'users.txt', 'tools.txt']
                for i in range(len(file)):
                    try:
                        os.remove(file[i])
                    except:
                        if debug==True:
                            print('Could Not Locate:', file[i])
                os.chdir(path)
            else:
                if hide==False:
                    print('Folder does not exist.')
        def itemsNotSignedOut():
            history.create_history('Run', 'save_in_txtFile.itemsNotSignedOut()', hide=debug)
            notSignedOutItem=[]
            check.signed_out_item()
        def students():
            history.create_history('Run', 'save_in_txtFile.students()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('student.txt')
            except:
                pass
            if OnlyAllowKnownStudents==False:
                file=open('student.txt','w')
                file.write("OnlyAllowKnownStudents is set to False.")
                file.close()
                os.chdir(path)
            if OnlyAllowKnownStudents==True:
                file=open('student.txt','w')
                for i in range(len(students)):
                    file.write('Student: '+students[i])
                file.close()
            os.chdir(path)
        def logs():
            global path, Output_file_MaxLength
            history.create_history('Run', 'save_in_txtFile.logs()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('student_logs.txt')
            except:
                pass
            #Save all logs of students that currently have items signed out.
            file=open('student_logs.txt','w')
            fileWrite=False #Used to determine if anything was exported to the text file.
            for i in range(len(lists)):
                if (lists[i])[0]=="logs":
                    for x in range(len((lists[i])[1])):
                        serial_Temp=serial= save_in_txtFile.decode((((lists[i])[1])[x])[0], displaySpace=False)
                        serial = save_in_txtFile.decode((((lists[i])[1])[x])[0], displaySpace=False)
                        student = save_in_txtFile.decode((((lists[i])[1])[x])[1], displaySpace=False)
                        tool_name=get.tool_name(serial_Temp)
                        file.write('Item: '+display.space(str(tool_name), max_length=Output_file_MaxLength, hide=True)+' Serial: '+display.space(serial, max_length=35, hide=True)+' Student: '+display.space(student, max_length=35, hide=True)+'\n')
                        fileWrite=True
            if fileWrite==False: #If nothing was writen to the log file. Make a not.
                file.write('There doesn\'t seem to be anything here. If you feel that this is incorrect or data loss has occured. Please mark and issue on GitHub and attempt to do a restore from a backup file. Backups are stored in the backup folder: '+str(path))
            file.write('\n\n#'+str(Output_file_MaxLength)+' character max length.')
                #Save Item name, Serial, And student name.
                #Search tools with serial to find item name.
            file.close()
            os.chdir(path)
        def users():
            history.create_history('Run', 'save_in_txtFile.users()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('users.txt')
            except:
                pass
            if len(known_users)>0:
                #Save all users in a text file. Do not write passwords.
                file=open('users.txt','w')
                for i in range(len(known_users)):
                    a, b = save_in_txtFile.decode(known_users[i], max_length=25)
                    c, d = save_in_txtFile.decode(permissions[i], max_length=25)
                    file.write(str(a)+': '+str(c)+'\n')
                file.close()
            else:
                print('There are no users.')
            os.chdir(path)
        def tools(max_length=20, showIfShort=False):
            #max_length argument is now outdated. To use var, set DecodeMethod to False.
            global Output_file_MaxLength
            history.create_history('Run', 'save_in_txtFile.tools()', hide=debug)
            try:
                os.chdir('collections')
            except:
                pass
            try:
                os.remove('tools.txt')
            except:
                pass
            #Save all tools in a text file.
            file=open('tools.txt','w')
            DecodeMethod=True #Default is True
            if DecodeMethod==True:
                for i in range(len(row)):
                    if (row[i])[0]=="tools":
                        part, part1 = save_in_txtFile.decode(((row[i])[1])[2], max_length=Output_file_MaxLength)
                        part2, part3 = save_in_txtFile.decode(((row[i])[1])[1], max_length=Output_file_MaxLength)
                        part4, part5 = save_in_txtFile.decode(((row[i])[1])[3], max_length=Output_file_MaxLength)
                        part6, part7 = save_in_txtFile.decode(((row[i])[1])[4], max_length=Output_file_MaxLength)
                        part8, part9 = save_in_txtFile.decode(((row[i])[1])[5], max_length=Output_file_MaxLength)
                        part10, part11 = save_in_txtFile.decode(((row[i])[1])[0], max_length=Output_file_MaxLength)
                        part12, partn=display.space(str(check.signed_out_item(str(((row[i])[1])[2]))), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        try:
                            part13, partn =display.space(str(((row[i])[1])[6]), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        except:
                            part13 = False
                        if part3==True or part5==True or part7==True or part9==True or part11==True:
                            part1, part17=display.space(str(True), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        if showIfShort==False:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'Broken: '+str(part13)+'\n\n')
                        if showIfShort==True:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'Broken: '+str(part13)+'  Shortenend: '+str(part1)+'\n\n')
            #Depreciated
            if DecodeMethod==False:
                for i in range(len(row)):
                    if (row[i])[0]=="tools":
                        #Item Returned, True/False
                        part, part1=display.space(str(((row[i])[1])[2]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part2, part3=display.space(str(((row[i])[1])[1]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part4, part5=display.space(str(((row[i])[1])[3]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part6, part7=display.space(str(((row[i])[1])[4]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part8, part9=display.space(str(((row[i])[1])[5]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part10, part11=display.space(str(((row[i])[1])[0]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        #Partn is just a placeholder and is not used. It handles the Return of return_ShortenNotice from display.space()
                        part12, partn=display.space(str(check.signed_out_item(str(((row[i])[1])[2]))), hide=True, max_length=max_length, return_ShortenNotice=True)
                        if part3==True or part5==True or part7==True or part9==True or part11==True:
                            part1, part17=display.space(str(True), hide=True, max_length=max_length, return_ShortenNotice=True)
                        if showIfShort==False:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'\n\n')
                        if showIfShort==True:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'  Shortenend: '+str(part1)+'\n\n')
            file.write('\n\n#'+str(max_length)+' character max length.')
            file.close()
            os.chdir(path)
        def decode(input, max_length=10, displaySpace=True):
            if displaySpace==True:
                if str(input)[0:2]=="b'":
                    part, part1 = display.space(str(input)[2:len(input)+2], hide=True, max_length=max_length, return_ShortenNotice=True)
                else:
                    part, part1 = display.space(str(input), hide=True, max_length=max_length, return_ShortenNotice=True)
                return part, part1
            elif displaySpace==False:
                if str(input)[0:2]=="b'":
                    part = str(input)[2:len(input)+2]
                else:
                    part = str(input)
                return part
            else:
                if debug==True:
                    print('displaySpace is a bool. It can only be assined True or False.')
    class display:
        def help():
            print('Branches:\n  display.space()\n  display.database()\n  display.settings()')
        def space(var, max_length=10, hide=False, return_ShortenNotice=False):
            #return ctypes.CDLL('yes.so').xor_gate(input1, input2)
            history.create_history('Run', 'display.space()', hide=debug)
            #Works with display.database to create a nice table to display.
            if isinstance(var, str)==True:
                length=len(var)
                if hide==False: print('Input length:',length)
                notice=False
                if length<max_length:
                    #Add spaces to fit
                    if hide==False: print('Total spaces to add:', max_length-length)
                    for i in range(max_length-length):
                        var+=' '
                    if hide==False: print('Final Length:',len(var))
                    if return_ShortenNotice==True:
                        return var, notice
                    else:
                        var
                if length>max_length:
                    #Shorten to fit
                    var=var[0:max_length]
                    if hide==False: print('Final Length:',len(var))
                    notice=True
                    if return_ShortenNotice==True:
                        return var, notice
                    else:
                        return var
                if return_ShortenNotice==True:
                    return var, False
                else:
                    return var
            else:
                if hide==False: print(errors.not_str())
        def database(data_base=None, database=None, hide=False):
            history.create_history('Run', 'display.database()', hide=debug)
            #Only works for column_row
            #Prints a asked database to the screen in a nice format.
            if data_base==None:
                database=None
            if data_base != None:
                #Check to see if database exists
                column_count=0
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        column_count=len((data_bases[i])[4])
                        break
                if hide==False:
                    print('Column_count='+str(column_count))
                #Print the column names.
                list3=''
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        for x in range(column_count):
                            list3+=display.space(((data_bases[i])[4])[x], hide=True)
                        break
                print(list3)
                #Look for items in row var that corresponds with the database and display them.
                for i in range(len(row)):
                    if (row[i])[0]==data_base:
                        list3=''
                        for x in range(column_count):
                            list3+=(display.space(((row[i])[1])[x], hide=True))
                        print(list3)
        def settings():
            history.create_history('Run', 'display.settings()', hide=debug)
            #Shows all settings on the screen.
            settings1=['UtilizeCPPCode','darkModeApp','clearHistoryOnStartup','clearHistoryOnStartup','clearHistoryOnStartup', 'AskForEncryptionPassword','printer_name', 'printer_debug','quiteStartup','encryptBackups','resetCollections','retain_backup_time','backup_startNumber','retain_backup_time','setup_backup_response','allowed_backupPermissions', 'skip_missing_settings','allowedPassword_chars', 'min_length', 'max_length','strict_password','auto_filter_profanity_speedBoost', 'quit_ifIncorrect', 'allowed_digists_forHistory', 'multi_process', 'auto_filter_profanity', 'skip_history_copy', 'auto_error_record', 'assign_digit_forHistory', 'app_version_control', 'set_operating_system', 'allow_windows_version', 'auto_history_record', 'show_incorrect_settings', 'do_not_remove', 'fail_safe', 'required_version', 'program_version', 'drive_letter', 'drive_name', 'system', 'profanity_filter', 'disable_filter_admin', 'global_password', 'dont_load_save', 'optimize_on_startup']
            for i in range(len(settings1)):
                try:
                    print(settings1[i]+'='+str(globals()[settings1[i]]))
                except:
                    print(settings1[i]+'='+'N/A')
    class math1:
        def pi(accuracy=1000000):
            history.create_history('Run', 'math1.pi()', hide=debug)
            # Initialize denominator
            k = 1
            # Initialize sum
            s = 0
            for i in range(accuracy):
                # even index elements are positive
                if i % 2 == 0:
                    s += 4/k
                else:
                    # odd index elements are negative
                    s -= 4/k
                # denominator is odd
                k += 2
            return s
        def distance(speed=None, time=None):
            history.create_history('Run', 'math1.distance()', hide=debug)
            return speed/time
        def force(mass=None, acceleration=None):
            history.create_history('Run', 'math1.force()', hide=debug)
            return mass*acceleration
    class backup:
        def help():
            print('Branches:\n  backup.reset_count()\n  backup.clear_all()\n  backup.create()')
        def reset_count():
            history.create_history('Run', 'backup.reset_count()', hide=debug)
            try: os.remove('count.py')
            except: pass
            file=open('count.py','w')
            file.write('backup_count='+str(backup_startNumber))
            file.close()
        def clear_all():
            history.create_history('Run', 'backup.clear_all()', hide=debug)
            #Clear all files
            try: shutil.rmtree('backups')
            except: pass
            os.mkdir('backups')
            backup.reset_count()
        def create(backup_name=None, random_name=False, password=None, hide=False, ForceEncryption=False):
            history.create_history('Run', 'backup.create()', hide=debug)
            try:
                password=password.get()
            except:
                pass
            #Allow backwards compadibilty.
            backup_name=None
            random_name=None
            global backup_count
            #Display new backup name.
            if hide==False:
                print('Current #:', backup_count)
            #Get a name
            backup_name=str(backup_count)
            #Create the backup.
            save.all(hide=hide)
            if encryptBackups==True or ForceEncryption==True:
                #Encrypt Files
                try:
                    if encrypt.all(password) != 1:
                        #Backup Certian Files
                        list2=['hello.cpp','libfoo.so','custom_database.py','history_desc.py','vars_to_save.py','data_save.aes','history.aes', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                        try: os.chdir('backups')
                        except: pass
                        zipObject= ZipFile(backup_name+'.zip', 'w')
                        try: os.chdir(path)
                        except: pass
                        for i in range(len(list2)):
                            try:
                                zipObject.write(list2[i])
                            except:
                                pass
                        try: os.chdir('backups')
                        except: pass
                        zipObject.close()
                        try: os.chdir(path)
                        except: pass
                        decrypt.all(password)
                    else:
                        pass
                except:
                    print('Wrong Password.')
                    return 'WrongPassword'
            #Don't encrypt.
            elif encryptBackups==False and ForceEncryption==False:
                #Backup Certian Files
                list2=['custom_database.py','history_desc.py','vars_to_save.py','data_save.py','history.py', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                try: os.chdir('backups')
                except: pass
                zipObject= ZipFile(backup_name+'.zip', 'w')
                #Move to main folder to copy files
                try: os.chdir(path)
                except: pass
                for i in range(len(list2)):
                    try:
                        zipObject.write(list2[i])
                    except:
                        pass
                #Move to backup folder to zip the files
                try: os.chdir('backups')
                except: pass
                #Put the zip in the folder
                zipObject.close()
                #Move back to main folder
                try: os.chdir(path)
                except: pass
            #Remove encrypted files from main folder
            if os.path.exists('data_save.py')==True and os.path.exists('data_save.aes')==True:
                os.remove('data_save.aes')
            if os.path.exists('history.txt')==True and os.path.exists('history.aes')==True:
                os.remove('history.aes')
            #Update count.py file.
            backup_count+=1
            try: os.remove('count.py')
            except: pass
            file=open('count.py','w')
            file.write('backup_count='+str(backup_count))
            file.close()
            #Remove shown hashes
            try: os.remove('hash_other.txt')
            except: pass
            try: os.remove('hash.txt')
            except: pass
    class backup_older:
        def clear_all():
            history.create_history('Run', 'backup_older.clear_all()', hide=debug)
            try:
                shutil.rmtree('backups')
                os.makedirs('backups')
            except:
                pass
        def remove(backup_name=None, hide=False):
            history.create_history('Run', 'backup_older.remove()', hide=debug)
            #Check if function is called without using backup_name
            if backup_name != None:
                #Check to see if backup with the name ___ exists.
                try:
                    if user_permission in allowed_backupPermissions:
                        try:
                            os.chdir('backups')
                            if os.path.exists(backup_name.lower()+'.zip')==True:
                                os.remove(backup_name.lower()+'.zip')
                                os.chdir(path)
                        except:
                            if hide==False:
                                print(errors.FileDoesNotExist())
                    else:
                        os.chdir(path)
                        if hide==False:
                            print(errors.incorrect_perm())
                except NameError:
                    if hide==False:
                        print(errors.NotSignedIn())
        def create(backup_name=None, password=None, random_name=False, hide=False):
            history.create_history('Run', 'backup_older.create()', hide=debug)
            #Create random name if asked to
            if random_name==True:
                backup_name=''
                for i in range(16):
                    backup_name+=random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')
            #Check if function is called without using backup_name
            if backup_name != None:
                os.chdir('backups')
                if os.path.exists(backup_name+'.zip') == True:
                    os.chdir(path)
                    if hide==False:
                        print(errors.BackupNameExists())
                else:
                    pass
                    #If backups with the name ___ does not exist. Create a backup.
                    user, perm = users.return_login_cred()
                    if perm in allowed_backupPermissions:
                        #Check for profanity.
                        if profanityFilter.filter(backup_name.lower())==1:
                            print(errors.profanityDetected(var=backup_name, user=user_logged))
                        else:
                            #If no profanity is found then create the backup.
                            os.chdir(path)
                            save.all(hide=hide)
                            #Encrypt certian files.
                            if encrypt.all(password) != 1:
                                #Files to backup
                                list2=['custom_database.py','history_desc.py','vars_to_save.py','data_save.aes','history.aes', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                                try: os.chdir('backups')
                                except: pass
                                zipObject= ZipFile(backup_name.lower()+'.zip', 'w')
                                try: os.chdir(path)
                                except: pass
                                for i in range(len(list2)):
                                    try:
                                        zipObject.write(list2[i])
                                    except:
                                        pass
                                try: os.chdir('backups')
                                except: pass
                                zipObject.close()
                                try: os.chdir(path)
                                except: pass
                                decrypt.all(password)
                    else:
                        os.chdir(path)
                        if hide==False:
                            print(errors.incorrect_perm())
                os.chdir(path)
                if backup_name == None:
                    if hide==False:
                        print(errors.cannot_call_func())
            #Remove shown hashes
            try: os.remove('hash_other.txt')
            except: pass
            try: os.remove('hash.txt')
            except: pass
    def check_settingsImproved(hide=False):
        history.create_history('Run', 'check_settingsImproved()', hide=debug)
        found=False
        settings1=['UtilizeCPPCode','clearHistoryOnStartup','clearHistoryOnStartup','clearHistoryOnStartup', 'AskForEncryptionPassword', 'printer_name', 'printer_debug','quiteStartup','encryptBackups','resetCollections','retain_backup_time','backup_startNumber','retain_backup_time','setup_backup_response','allowed_backupPermissions', 'skip_missing_settings','allowedPassword_chars', 'min_length', 'max_length','strict_password','auto_filter_profanity_speedBoost', 'quit_ifIncorrect', 'allowed_digists_forHistory', 'multi_process', 'auto_filter_profanity', 'skip_history_copy', 'auto_error_record', 'assign_digit_forHistory', 'app_version_control', 'set_operating_system', 'allow_windows_version', 'auto_history_record', 'show_incorrect_settings', 'do_not_remove', 'fail_safe', 'required_version', 'program_version', 'drive_letter', 'drive_name', 'system', 'profanity_filter', 'disable_filter_admin', 'global_password', 'dont_load_save', 'optimize_on_startup']
        types=[bool, bool, bool, bool, bool, str, bool, bool, bool, bool, int, int, int, bool, list, bool, str, int, int, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, bool, bool, str, str, str, str, str, bool, bool, bool, bool, bool]
        for i in range(len(settings1)):
            skip=False
            if skip_missing_settings==True:
                if settings1[i] in locals() or settings1[i] in globals():
                    skip=True
            if skip==False:
                if isinstance(globals()[settings1[i]], types[i]) == False:
                    found=True
                    if fail_safe==True:
                        if types[i]==str:
                            globals()[settings1[i]]=''
                        if types[i]==bool:
                            globals()[settings1[i]]=False
                        if types[i]==int:
                            globals()[settings1[i]]=10
                        if types[i]==list:
                            globals()[settings1[i]]=[]
                    if hide==False:
                        print(str(settings1[i]))
        if found==True:
            if hide==False:
                print("1 or More settings are incorrect.")
            exit()
        check_settings(hide=hide)
    def check_settings(hide=False):
        history.create_history('Run', 'check_settings()', hide=debug)
        #Checks settings.py to make sure all settings are correct and will not cause a proplem.
        #If one or more items come back as a problem they will be listed,
        error_found1=False
        #Check to see if max is bigger/smaller than min
        if max_length<min_length+1:
            error_found1=True
        if show_incorrect_settings==True:
            if hide==False:
                print('\nUnknown answers:')
        list2=['7', '8','10','11']
        found=True
        for i in range(len(list2)):
            if allow_windows_version != list2[i]:
                found=False
            if allow_windows_version == list2[i]:
                found=True
                break
        if found==False:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  allow_windows_version must be set to 7, 8, 10, or 11')
            error_found1=True
        if len(drive_letter)>1 or len(drive_letter)<1:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  drive_letter must be 1 character')
            error_found1=True
        if isinstance(allowed_digists_forHistory, int):
            if allowed_digists_forHistory>30 or allowed_digists_forHistory<1:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  allowed_digists_forHistory can only be upto 30 and no less than 1.')
                error_found1=True
        if isinstance(min_length, int)==True:
            if min_length<5 or min_length+1>max_length:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  min_length cannot be less than 5 and/or cannot be bigger than max_length')
                error_found1=True
        if isinstance(max_length, int)==True:
            if max_length-1<min_length or max_length>99:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  max_length cannot be bigger than 99 and/or cannot be smaller than min_length')
                error_found1=True
        if error_found1==False:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  None')
        if quit_ifIncorrect == True:
            if error_found1==True:
                if hide==False:
                    print()
                exit()
    class profanityFilter:
        def disable():
            history.create_history('Run', 'profanityFilter.disable()', hide=debug)
            #Redirect
            profanityFilter.deactivate()
        def enable():
            history.create_history('Run', 'profanityFilter.enable()', hide=debug)
            #Redirect
            profanityFilter.activate()
        def activate():
            history.create_history('Run', 'profanityFilter.activate()', hide=debug)
            #Enables profanity filter
            global profanity_filter
            profanity_filter=True
        def deactivate():
            history.create_history('Run', 'profanityFilter.deactivate()', hide=debug)
            #Disables profanity filter
            global profanity_filter
            profanity_filter=False
        def setup():
            history.create_history('Run', 'profanityFilter.setup()', hide=debug)
            #Called on startup if enabled to setup the filter.
            global profanity_filter, auto_filter_profanity_speedBoost, list1
            #Check profanity.txt to see if input matches.
            if profanity_filter==True and auto_filter_profanity_speedBoost==False:
                with open("profanity.txt", encoding="ascii") as file_in:
                    for line in file_in:
                        list1.append(line.replace('\n',''))
            if profanity_filter==True and auto_filter_profanity_speedBoost==True:
                with open("shorter_profanity.txt") as file_in:
                    for line in file_in:
                        list1.append(line.replace('\n',''))
        def filter(var, manual=False, hide=False, test=False, record=True):
            history.create_history('Run', 'profanityFilter.filter()', hide=debug)
            #Give this function a string to check.
            #If a match is found 1 is returned. If none, 0 is returned.
            global auto_filter_profanity
            if test==True:
                auto_filter_profanity=True
            if auto_filter_profanity==True or manual==True:
                global list1
                if isinstance(var, str) == True:
                    var=var.lower()
                    for i in range(len(list1)):
                        if str(var) == list1[i]:
                            if record == True:
                                errors.profanityDetected(var=var, user=user_logged)
                            return 1
                    return 0
                else:
                    if hide == False:
                        print('(Error) . This will not be recorded. Input must be a string.')
            if auto_filter_profanity==False:
                if debug==True:
                    if hide==False:
                        print('Profanity filter is off.')
                return 0
    def encrypt_check():
        history.create_history('Run', 'encrypt_check()', hide=debug)
        #Check to see if save file is encrypted.
        #Return 1 if encrypted, if not return 0.
        try:
            open('data_save.aes', 'r')
            open('history.aes', 'r')
            return 1
        except:
            pass
        return 0
    class history:
        def get_description(code=None, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Print description of selected history item in terminal if message is found.
            if code!=None:
                for i in range(len(history_id)):
                    if history_id[i]==str(code):
                        if hide==False:
                            print('Code: '+str(code))
                            print('Message: '+history_description[i])
        def add_description(code=None, description=None):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Create a description for history if requested.
            #This is automatically called if used.
            if code != None and description != None:
                if isinstance(code, str)==True and isinstance(description, str)==True:
                    history_id.append(str(code))
                    history_description.append(str(description))
        def check_forDuplicate(user, usage, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Prevents duplicate items to be recorded.
            file=open('history.txt').read()
            a=len(file)
            a3=len(user)+len(usage)+2
            last_object=(file[a-a3: a])
            current_object=(usage+': '+user)
            if debug==True and hide==False:
                print('Current:', current_object)
                print('Last:', last_object)
            if str(current_object)==str(last_object):
                if debug==True:
                    if hide==False:
                        print('Match Found. Skipping write to history file.')
                return 1
            else:
                if debug==True:
                    if hide==False:
                        print('No match found. Writing to history file.')
                return 0
        def assign_letter(count, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Not in use yet.
            global allowed_digists_forHistory
            count=int(count)
            a=''
            for i in range(allowed_digists_forHistory-len(str(count))):
                a+='0'
            a+=str(count)
            count+=1
            save.all(hide=hide)
            return a
        def clear():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Clears history file
            try:
                os.chdir(path)
            except:
                pass
            history.delete()
            history.create()
            try:
                os.remove('history_desc.py')
            except:
                pass
            file=open('history_desc.py', 'w')
            file.write('history_id=[]\nhistory_description=[]\ncount=1')
            file.close()
        def delete():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Removes history file
            try:
                os.remove('history.txt')
            except:
                pass
        def create():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Creates history file
            global d1
            ah=open('history.txt','w')
            ah.write('File created: '+d1)
            ah.close()
        def create_history(user, usage, manual_record=False, add_desc=False, desc=None, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Adds items to history file
            if auto_history_record==True or manual_record==True:
                if user==None:
                    user='Null'
                global d1, count
                try:
                    open('history.txt','r')
                except:
                    history.create()
                allow=True
                if skip_history_copy==True:
                    if history.check_forDuplicate(user=user, usage=usage, hide=hide) == 1:
                        allow=False
                if allow==True:
                    if add_desc==True:
                        if assign_digit_forHistory==False:
                            if debug==True:
                                if hide==False:
                                    print('assign_digit_forHistory needs to be enabled for history to add a description.')
                        if desc!=None and assign_digit_forHistory==True:
                            abc=history.assign_letter(count, hide=hide)
                            history.add_description(code=abc, description=desc)
                            ah=open('history.txt','a')
                            ah.write('\n('+d1+')'+' '+str(usage)+': '+str(user)+' : ('+str(abc)+')')
                            ah.close()
                            count+=1
                            save.all(hide=hide)
                        if desc==None:
                            if hide==False:
                                print('Please give a description to write history.')
                    if add_desc==False:
                        ah=open('history.txt','a')
                        ah.write('\n('+d1+')'+' '+str(usage)+': '+str(user))
                        ah.close()
    class optimize():
        def determ(letter=None, set=None, test=False):
            for i in range(26):
                if letter == alphabet[i]:
                    if test == False:
                        return 0
                    if test == True:
                        a=globals()[set]
                        a=a[i]
                        return a
        def run(save_optimizations=True, hide=False):
            global data_bases, opto_data, opto_row, row, opto_lists, lists, debug, user_permission, user_logged
            history.create_history(None, 'Optimize', hide=hide)
            try:
                user_logged=None
                user_permission=None
                opto_data=optimize.count(var='data_bases')
                data_bases=optimize.list_org(var='data_bases')
                opto_row=optimize.count(var='row')
                row=optimize.list_org(var='row')
                opto_lists=optimize.count(var='lists')
                lists=optimize.list_org(var='lists')
                if debug == True:
                    if hide==False:
                        print('Save file optimized.')
            except:
                if debug == True:
                    if hide==False:
                        print('An error occured.')
            if save_optimizations==True:
                if hide==False:
                    print('All data saved.')
                save.all(hide=hide)
        def count(var):
            #Count items in lists and get a rough count.
            opto=[]
            alphabet='abcdefghijklmnopqrstuvwxyz '
            for i in range(26):
                opto.append(0)
            count=0
            letter=''
            rcount=len(globals()[var])
            while letter != " ":
                letter = alphabet[count]
                for i in range(rcount):
                    if (((globals()[var])[i])[0])[0] == letter:
                        opto[count]+=1
                count+=1
            return opto
        def list_org(var):
            #Creates a list of alphabet count. Hard to explain. It makes opto_ row, list, and data
            org=[]
            max=len(globals()[var])
            current=0
            alphabet='abcdefghijklmnopqrstuvwxyz '
            count=0
            while current < max:
                for i in range(max):
                    if (((globals()[var])[i])[0])[0] == alphabet[count]:
                        org.append((globals()[var])[i])
                        current+=1
                count+=1
            return org
    def check_data(hide=False):
        history.create_history('Run', 'check_data()', hide=debug)
        #Also remove data sets that are not apart of a database.
        print('\n')
        global import_type
        check=[False, False]
        #Check data_bases var
        for i in range(len(data_bases)):
            try:
                if (data_bases[i])[0] != None:
                    if (data_bases[i])[1] != None:
                        if (data_bases[i])[2] != None:
                            if (data_bases[i])[3] == "column_row":
                                if isinstance((data_bases[i])[4], list) == True:
                                    check[0]=True
                            if (data_bases[i])[3] == "list":
                                check[0]=True
            except:
                check[0]=False
                break
        #Write down all current databases.
        known_databases=[]
        for i in range(len(data_bases)):
            known_databases.append((data_bases[i])[0])
        #Row check. Check to see if database and list are present for each, and if set databases doesn't exist.
        for i in range(len(row)):
            try:
                if (row[i])[0] != None:
                    if (row[i])[0] in known_databases:
                        if isinstance((row[i])[1], list) == True:
                            check[1]=True
            except:
                check[1]=False
                break
        if hide==False:
            print('True = Working | False = Broken')
            print('Database Check:',check[0])
            print('Rows Check:',check[1])
    def list_count(data_base=None, database=None):
        history.create_history('Run', 'list_count()', hide=debug)
        if data_base == None:
            data_base=database
        for i in range(len(data_bases)):
            if (data_bases[i])[0]==data_base:
                return len((data_bases[i])[4])
    def check_input(var):
        history.create_history('Run', 'check_input()', hide=debug)
        global denied_inputs
        for i in range(len(denied_inputs)):
            if var==denied_inputs[i]:
                return True
        if var not in denied_inputs:
            return False
    def exit():
        history.create_history('Run', 'exit()', hide=debug)
        safe_exit.RmExcessFiles()
        print('Application Closed')
        sys.exit()
    class restore:
        def remove_old_backups(TempChange_retain_backup_time=None, hide=False):
            history.create_history('Run', 'restore.remove_old_backups()', hide=debug)
            if TempChange_retain_backup_time != None:
                if isinstance(TempChange_retain_backup_time, int)==True:
                    temp=retain_backup_time
                    retain_backup_time=TempChange_retain_backup_time
                else:
                    if hide==False:
                        print('TempChange_retain_backup_time Must be a(n) interger.')
            #Removes backups older than set retain_backup_time=
            #Uses a numbering scheme to calculate age.
            #Search for all files in the backups folder and put the names in a list
            f = []
            for (dirpath, dirnames, filenames) in walk('backups'):
                f.extend(filenames)
                break
            #Remove .zip from all files names in list
            for i in range(len(f)):
                try:
                    f[i]=f[i].replace('.zip','')
                except:
                    f.pop(i)
            #Find the highest number in list
            highest=0
            for i in range(len(f)):
                try:
                    if int(f[i])>highest:
                        highest=int(f[i])
                except:
                    pass
            #Remove old backups.
            try:
                os.chdir('backups')
                for i in range(len(f)):
                    if int(f[i])<highest-retain_backup_time+1:
                        try:
                            os.remove(f[i]+'.zip')
                        except:
                            pass
                retain_backup_time=temp
                os.chdir(path)
            except:
                return False
        def all(beta=False, backup_name=None, password=None, hide=False, restoreFile=['app.py','history_desc.aes','settings.py','data_save.aes','history.aes'], removeFile=['app.py','history_desc.py', 'settings.py','data_save.py','history.txt']):
            history.create_history('Run', 'restore.all()', hide=debug)
            #Restore everything from a backup.
            if beta == True:
                if password==None:
                    if hide==False:
                        print('A password is neeeded to restore from a backup.')
                if password != None:
                    if check.encyption_password(password)==0:
                        if hide==False:
                            print('Incorrect Password')
                    if check.encyption_password(password)==1:
                        #Search for all files in the backups folder and put the names in a list
                        f = []
                        for (dirpath, dirnames, filenames) in walk('backups'):
                            f.extend(filenames)
                            break
                        #Remove .zip from all files names in list
                        for i in range(len(f)):
                            try:
                                f[i]=f[i].replace('.zip','')
                            except:
                                f.pop(i)
                        #Find the highest number in list
                        highest=0
                        for i in range(len(f)):
                            try:
                                if int(f[i])>highest:
                                    highest=int(f[i])
                            except:
                                pass
                        #Display on screen what the latest backup is.
                        if highest != 0:
                            if hide==False:
                                print('Latest Backup:',str(highest)+'.zip')
                            #Extract all files to restore folder after creating the folder
                            if os.path.exists('restore')==False:
                                os.mkdir('restore')
                            with zipfile.ZipFile('backups/'+str(highest)+'.zip', 'r') as zip_ref:
                                zip_ref.extractall('restore')
                            #Replace all item in removeFile var to root
                            for i in range(len(removeFile)):
                                #Remove files in root
                                try:
                                    os.remove(removeFile[i])
                                except:
                                    if hide==False:
                                        print('File '+removeFile[i]+' in backup could not be found')
                            #Add files to root from restore folder
                            for i in range(len(restoreFile)):
                                try:
                                    os.chdir('restore')
                                except:
                                    pass
                                try:
                                    shutil.copy(restoreFile[i],path)
                                except:
                                    if hide==False:
                                        print('Could not restore file:',restoreFile[i])
                            os.chdir(path)
                            decrypt.all(password)
                            shutil.rmtree('restore')
                        if highest==0:
                            print('No backups detected.')
            if beta==False:
                print('This function has not been implemented yet.\nA restore plan is in the works. Restore will not work until a complete backup plan is created. For now a temporary backup method has been added. You can run the app from a backup if needed.')
    class info:
        def operating_system():
            global system
            return system
        def python_version():
            return sys.version[0:len(required_version)]
        def app_version():
            global program_version
            return program_version
    class get:
        def tool_name(serial):
            #NO NOT ADD history.create_history() HERE. PERFORMANCE WILL DRAMATICALLY DECREASE!
            for i in range(len(row)):
                if (row[i])[0]=="tools":
                    a = save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)
                    c = save_in_txtFile.decode(serial, displaySpace=False)
                    if a==c:
                        a = save_in_txtFile.decode(((row[i])[1])[1], displaySpace=False)
                        return a
            return "CouldNotReturn"
        def try_password(password):
            history.create_history('Run', 'get.try_password()', hide=debug)
            if system=='windows':
                global drive_letter
                try:
                    pyAesCrypt.decryptFile(drive_letter+':/hash.aes',drive_letter+':/hash.txt',password)
                    pyAesCrypt.encryptFile(drive_letter+':/hash.txt',drive_letter+':/hash.aes',password)
                    return 1
                except:
                    return 0
            else:
                try:
                    pyAesCrypt.decryptFile('hash.aes','hash.txt',password)
                    pyAesCrypt.encryptFile('hash.txt','hash.aes',password)
                    return 1
                except:
                    return 0
        def get_other_hash(password):
            history.create_history('Run', 'get.get_other_hash()', hide=debug)
            if system=="windows":
                try:
                    decrypt.hash(password)
                    global drive_letter
                    file=open(drive_letter+':/hash_other.txt','r').read()
                    os.remove(drive_letter+':/hash_other.txt')
                    return file
                except ValueError:
                    print('Incorrect Password!')
            else:
                try:
                    decrypt.hash(password)
                    file=open('hash_other.txt','r').read()
                    os.remove('hash_other.txt')
                except ValueError:
                    print('Incorrect Password')
        def get_hash():
            history.create_history('Run', 'get.get_hash()', hide=debug)
            try:
                password = get.password()
                decrypt.hash(password)
                global drive_letter
                if system=='windows':
                    file=open(drive_letter+':/hash.txt','r').read()
                    os.remove(drive_letter+':/hash.txt')
                else:
                    file=open('hash.txt','r')
                    os.remove('hash.txt')
                return file
            except ValueError:
                global global_password
                if global_password==True:
                    get.get_other_hash(password)
        def new_hash(passw=None, normal=False, memory_float=False, other=False):
            history.create_history('Run', 'get.new_hash()', hide=debug)
            get.random_hash(single=normal, memory_float=memory_float)
            get.encrypt_hash(passw, other=other)
            password=None
        def encrypt_hash(passw=None, other=False):
            history.create_history('Run', 'get.encrypt_hash()', hide=debug)
            global drive_letter, global_password
            if passw != None:
                password=passw
            if passw == None:
                try:
                    password=get.password()
                except:
                    password=passw
            if other == False:
                if system=='windows':
                    pyAesCrypt.encryptFile(drive_letter+':/hash.txt', drive_letter+':/hash.aes', password)
                    os.remove(drive_letter+':/hash.txt')
                else:
                    pyAesCrypt.encryptFile('hash.txt','hash.aes',password)
                    os.remove('hash.txt')
            if other == True:
                if global_password==True:
                    if system=="windows":
                        pyAesCrypt.encryptFile(drive_letter+':/hash_other.txt', drive_letter+':/hash_other.aes', password)
                        os.remove(drive_letter+':/hash_other.txt')
                    else:
                        pyAesCrypt.encryptFile('hash_other.txt', 'hash_other.aes', password)
                        os.remove('hash_other.txt')
        def random_hash(length=100, normal=True, single=False, memory_float=False):
            history.create_history('Run', 'get.random_hash()', hide=debug)
            if isinstance(length, int) == False:
                print(errors.not_int())
            if isinstance(length, int) == True:
                ah=''
                for i in range(length): 
                    ah+=random.choice('ajfygweuoichwgbuieucr73rwecb638781417983b 623v9923 r t72344y 23uc3u2b4n9832 4b2c794y 237bc2423nc482b3c427 rfgshdfuw38263872guihfef86w4t878whryfeg48tg34hf7w')
                if memory_float==True:
                    global memory_hash
                    memory_hash=ah
                if normal==True: 
                    global drive_letter
                    if system=="windows": file=open(drive_letter+':/hash.txt','w')
                    else: file=open('hash.txt', 'w')
                    file.write(ah)
                    file.close()
                    if single==False:
                        if system=="windows": file=open(drive_letter+':/hash_other.txt','w')
                        else: file=open('hash_other.txt','w')
                        file.write(ah)
                        file.close()
                if normal==False:
                    return ah
    class decrypt:
        def hash(password):
            global drive_letter
            try:
                if system=='windows':
                    pyAesCrypt.decryptFile(drive_letter+':/hash.aes',drive_letter+':/hash.txt',password)
                    return open(drive_letter+':/hash.txt','r').read()
                else:
                    pyAesCrypt.decryptFile('hash.aes','hash.txt',password)
                    return open('hash.txt','r').read()
            except:
                try:
                    if system=="windows":
                        pyAesCrypt.decryptFile(drive_letter+':/hash_other.aes',drive_letter+':/hash_other.txt',password)
                        return open(drive_letter+':/hash_other.txt','r').read()
                    else:
                        pyAesCrypt.decryptFile('hash_other.aes','hash_other.txt',password)
                        return open('hash_other.txt','r').read()
                except:
                    if memory_hash != '':
                        return memory_hash
                    else:
                        return False
        def history(password):
            try:
                pyAesCrypt.decryptFile('history.aes','history.txt',password)
                os.remove('history.aes')
            except:
                return 0
        def data(password):
            try:
                pyAesCrypt.decryptFile('data_save.aes','data_save.py',password)
                os.remove('data_save.aes')
            except:
                return 0
        def cache(password):
            pyAesCrypt.decryptFile('cache.aes','cache.py',password)
            os.remove('cache.aes')
        def opt(password):
            pyAesCrypt.decryptFile('opt.aes','opt.py',password)
            os.remove('opt.aes')
        def history_desc(password):
            try:
                pyAesCrypt.decryptFile('history_desc.py','history_desc.aes',password)
                os.remove('history_desc.aes')
            except:
                return 0
        def all(password):
            #decrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
            if os.path.exists('history.aes')==True or os.path.exists('data_save.aes')==True:
                if decrypt.hash(password) != False:
                    d_password=decrypt.hash(password)
                    if decrypt.history_desc(d_password) == 0 and decrypt.history(d_password) == 0 and decrypt.data(d_password) == 0:
                        return 1
                try:
                    global drive_letter
                    if system=="windows": os.remove(drive_letter+':/hash.txt')
                    else: os.remove('hash.txt')
                except:
                    pass
                try:
                    if system=="windows": os.remove(drive_letter+':/hash_other.txt')
                    else: os.remove('hash_other.txt')
                except:
                    pass
            else:
                print('Cannot decrypt. Encrypted files do not exist.')
    class encrypt:
        def history(password):
            global fail_safe
            failed=False
            if fail_safe==True:
                try:
                    open('history.aes','r')
                    print('Existing file found. Cannot encrypt.')
                    failed=True
                except:
                    pass
                try:
                    open('history.txt','r')
                except:
                    failed=True
            if failed == False:
                global do_not_remove
                pyAesCrypt.encryptFile('history.txt','history.aes',password)
                if do_not_remove==False:
                    os.remove('history.txt')
        def data(password):
            global fail_safe
            failed=False
            if fail_safe==True:
                try:
                    open('data_save.aes','r')
                    print('Existing file found. Cannot encrypt.')
                    failed=True
                except:
                    pass
                try:
                    open('data_save.py','r')
                except:
                    failed=True
            if failed == False:
                global do_not_remove
                pyAesCrypt.encryptFile('data_save.py','data_save.aes',password)
                if do_not_remove==False:
                    os.remove('data_save.py')
        def cache(password):
            global do_not_remove
            pyAesCrypt.encryptFile('cache.py','cache.aes',password)
            if do_not_remove==True:
                os.remove('cache.py')
        def opt(password):
            global do_not_remove
            pyAesCrypt.encryptFile('opt.py','opt.aes',password)
            if do_not_remove==True:
                os.remove('opt.py')
        def history_desc(password):
            global do_not_remove
            pyAesCrypt.encryptFile('history_desc.py','history_desc.aes',password)
            if do_not_remove==True:
                os.remove('history_desc.py')
        def all(password):
            try:
                d_password=decrypt.hash(password)
                #encrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
                encrypt.data(d_password)
                encrypt.history(d_password)
                encrypt.history_desc(d_password)
                #encrypt.cache(d_password)
                #encrypt.opt(d_password)
                global drive_letter
                try:
                    if system=="windows":
                        os.remove(drive_letter+':/hash.txt')
                    else:
                        os.remove('hash.txt')
                except:
                    pass
                try:
                    if system=="windows":
                        os.remove(drive_letter+':/hash_other.txt')
                    else:
                        os.remove('hash_other.txt')
                except:
                    pass
            except ValueError:
                return 1
    class save:
        def all(hide=False, side_tiltForce=None):
            if disable_save==False:
                history.create_history(None, 'Save', hide=hide)
                from vars_to_save import list
                file=open('data_save.py','w')
                file.write('# -*- coding: utf-8 -*-\n')
                for i in range(len(list)):
                    file.write(list[i]+'='+str(globals()[list[i]])+'\n')
                file.write('\n')
                file.close()
                if advanced_history==True:
                    file=open('history_desc.py', 'w')
                    file.write('history_id='+str(history_id))
                    file.write('\nhistory_description='+str(history_description))
                    file.write('\ncount='+str(count))
            if disable_save==True:
                history.create_history(user='True', usage='Skip Save', manual_record=auto_error_record, hide=hide)
    class clear:
        def normal():
            os.system('clear')
    class check:
        def signed_out_item(barcode, hide=False):
            #Check to see if item has been signed out already.
            for i in range(len(lists)):
                #Find the database logs
                if (lists[i])[0]=='logs':
                    for x in range(len((lists[i])[1])):
                        if hide==True:
                            print((((lists[i])[1])[x])[0])
                        if (((lists[i])[1])[x])[0]==barcode:
                            #If found
                            return True
            #If not found
            return False
        def barcode(barcode):
            #Check to see if barcode exists.
            for i in range(len(row)):
                #Find the database tools
                if (row[i])[0]=="tools":
                    if save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)==barcode:
                        #If found
                        return False
            #If not found
            return True
        def encyption_password(password):
            if decrypt.hash(password=password)==False:
                #Returns 1 if password does not match
                return 1
            else:
                #Returns 0 if password Matches
                return 0
        def data_format(data_base=None):
            #Returns database type.
            num=check_data(data_base)
            #Call to return data_base type.
            if num == False:
                global data_bases
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        return (data_bases[i])[3]
            if num == True:
                print(errors.cannot_call_func('check.data_format()'))
        def data_base_exists(data_base=None):
            #Check to see if database exists,
            if isinstance(data_base, str) == False and data_base != None:
                print(errors.not_str())
            if isinstance(data_base, str) == True or data_base==None:
                if data_base != None:
                    global data_bases
                    found=False
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            found = True
                    return found
                if data_base == None:
                    print(errors.cannot_call_func('check.data_base_exists()'))
    class users:
        def disable(user=None, hide=False):
            history.create_history('Run', 'users.disable()', hide=debug)
            num=check_input(user)
            #Disables a user
            if num == False:
                global known_users, active_users
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Disable user', hide=hide)
                        active_users[i]=False
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.disable()'))
        def enable(user=None, hide=False):
            history.create_history('Run', 'users.enable()', hide=debug)
            num=check_input(user)
            #Enables a user
            if num == False:
                global known_users, active_users
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Enable user', hide=hide)
                        active_users[i]=True
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.disable()'))
        def create(new_user=None, new_password=None, new_permission=None, hide=False):
            history.create_history('Run', 'users.create()', hide=debug)
            global known_users, passwords, permissions
            num1=check_input(new_user)
            num2=check_input(new_password)
            try:
                new_user=new_user.lower()
                new_permission=new_permission.lower()
            except:
                pass
            if new_permission not in allowed_users:
                if hide==False:
                    print(errors.incorrect_perm())
                    return 'IncorrectPerm'
            if profanityFilter.filter(new_user)==1:
                if hide==False:
                    print(errors.profanityDetected(new_user, user=user_logged))
            if profanityFilter.filter(new_password.lower())==1:
                if hide==False:
                    print(errors.profanityDetected(new_password, user=user_logged))
            if num1 == False and num2 == False and new_permission in allowed_users and profanityFilter.filter(new_user)==0 and profanityFilter.filter(new_password.lower())==0:
                if password_restrictions.check_password(new_password) == 1 or strict_password==False:
                    skip=False
                    for i in range(len(known_users)):
                        if known_users[i]==new_user:
                            skip=True
                            print(errors.user_exists())
                            return False
                    if skip == False:
                        if isinstance(new_user, str) == True:
                            if isinstance(new_password, str) == True:
                                if isinstance(new_permission, str) == True or new_permission==None:
                                    history.create_history(new_user, 'Created user', hide=hide)
                                    known_users.append(new_user)
                                    passwords.append(new_password)
                                    permissions.append(new_permission)
                                    active_users.append(True)
                        if isinstance(new_user, str) == False:
                            if hide==False:
                                print('new_user must be str')
                        if isinstance(new_permission, str) == False:
                            if hide==False:
                                print('new_permission must be str')
                        if isinstance(new_permission, str) == False and new_permission != None:
                            if hide==False:
                                print('new_password must be str or None') 
                else:
                    if hide==False:
                        print(errors.doesNotObeyRestrictions())
                        print('Password Min Lnegth:',min_length)
                        print('Password Max Length:',max_length)
                        print('Password can only contain:',allowedPassword_chars)
                        return "PasswordDoesNotMeetReq"
            if num1 == True or num2 == True:
                print(errors.cannot_call_func('users.create()'))
        def remove(user=None, hide=False):
            history.create_history('Run', 'users.remove()', hide=debug)
            print(type(user))
            print('User:'+user+':')
            num=check_input(user)
            if num == False:
                user=user.lower()
                found=False
                global known_users, passwords, permissions
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Removed user', hide=hide)
                        known_users.pop(i)
                        passwords.pop(i)
                        permissions.pop(i)
                        active_users.pop(i)
                        found=True
                        break
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
                    return "UserNotFound"
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.remove()'))
        def show_all():
            history.create_history('Run', 'users.show_all()', hide=debug)
            global known_users
            for i in range(len(known_users)):
                print('User: '+known_users[i])
                print('Permission: '+permissions[i])
        def change_permissions(user=None, new_permission=None, hide=False):
            history.create_history('Run', 'users.change_permission()', hide=debug)
            num1=check_input(user)
            num2=check_input(new_permission)
            if num1 == False and num2 == False:
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change permission', hide=hide)
                        permissions[i]=new_permission
            if num1 == True or num2 == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_permissions()'))
        def change_name(user=None, new_name=None, hide=False):
            history.create_history('Run', 'users.change_name()', hide=debug)
            num1=check_input(user)
            num2=check_input(new_name)
            if profanityFilter.filter(new_name)==1:
                if hide==False:
                    print(errors.profanityDetected(var=new_name, user=user_logged))
            if num1 == False and num2 == False and profanityFilter.filter(new_name)==0:
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user+' to '+new_name, 'Change name', hide=hide)
                        known_users[i]=new_name
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num1 == True or num2 == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_name()'))
        def change_password(user=None, new_password=None, hide=False):
            history.create_history('Run', 'users.change_password()', hide=debug)
            global passwords
            num=check_input(user)
            if profanityFilter.filter(new_password)==1:
                if hide==False:
                    print(errors.profanityDetected(var=new_password, user=user_logged))
            if num == False and profanityFilter.filter(new_password)==0:
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change password', hide=hide)
                        passwords[i]=new_password
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_password()'))
        def return_users():
            #DO NOT ADD history.create_history() HERE. FOR SECURITY REASONS.
            global known_users
            return known_users
        def login_request(user=None, password=None, hide=False):
            history.create_history('Run', 'users.login_request()', hide=debug)
            #Will return True if credentials are correct, if not will return False
            user=str(user)
            password=str(password)
            if user != None and password != None or password==None:
                global known_users, passwords, user_logged, user_permission, profanity_filter, disable_filter_admin
                if isinstance(user, str)==True and isinstance(password, str)==True or password == None:
                    if user in known_users:
                        for i in range(len(known_users)):
                            if known_users[i]==user:
                                if passwords[i] != password:
                                    if hide==False:
                                        print('Password is incorrect.')
                                if passwords[i]==password:
                                    if active_users[i]==True:
                                        user_logged=known_users[i]
                                        user_permission=permissions[i]
                                        if user_permission=="admin":
                                            if disable_filter_admin==True:
                                                profanity_filter=False
                                        return True
                                    if active_users[i]==False:
                                        if hide==False:
                                            print('User is not active.')
                if hide==False:
                    if isinstance(user, str) == False:
                        print(errors.not_str())
                    if isinstance(password, str) == False and password != None:
                        print(errors.not_str())
                    if user not in known_users:
                        print(errors.user_not_found())
                try:
                    if user_logged==False:
                        return False
                except:
                    pass
            if user == None:
                if hide==False:
                    print(errors.cannot_call_func('users.login_request()'))
        def logout(hide=False):
            history.create_history('Run', 'users.logout()', hide=debug)
            global user_logged, user_permission, profanity_filter, disable_filter_admin
            try:
                #If no users is logged in, user_permission will cause an error.
                if user_permission=="admin":
                    if disable_filter_admin==True:
                        profanity_filter=True
                user_permission=None
                user_logged=None
            except:
                #Handles the error and prints a message and/or return(s) it
                if debug==True or hide==False:
                    print("No user signed in.")
                return "UserNotSignedIn"
        def return_login_cred():
            history.create_history('Run', 'users.return_login_cred()', hide=debug)
            try:
                global user_logged, user_permission
                if user_logged==None:
                    return 'UserNotSignedIn', 'UserNotSignedIn'
                else:
                    return user_logged, user_permission
            except:
                return 'UserNotSignedIn', 'UserNotSignedIn'
    class data_base:
        def help():
            print('Branches:\n  data_base.edit\n  data_base.empty\n  data_base.show\n  data_base.remove\n  data_base.create')
        class edit:
            def help():
                print('Branches:\n  data_base.edit.search_rows()\n  data_base.edit.check_owner()\n  data_base.edit.add_row_term()\n  data_base.edit.add_item()\n  data_base.edit.remove_row()\n  data_base.edit.add_column()\n  data_base.edit.remove_column()')
            def search_rows(data_base=None, id=None, database=None):
                if data_base == None:
                    data_base=database
                if isinstance(data_base, str) == True and isinstance(id, str) == True:
                    for i in range(len(row)):
                        if (row[i])[0] == data_base:
                            if ((row[i])[1])[1]==id:
                                return 1
                    return 0
            def check_owner(data_base=None, user_perm=None, database=None):
                if data_base == None:
                    data_base=database
                #Returns 1 is owner matches the database.
                if isinstance(data_base, str) == True and isinstance(user_perm, str) == True:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[2] == user_perm:
                            return 1
                    return 0
            def add_row_term():
                data=input('Database: ')
                bra=False
                try:
                    for i in range(len(data_bases)):
                        if bra == True:
                            break
                        if (data_bases[i])[0]==data:
                            aa=input('Enter row/list with spaces between each: ')
                    data_base.edit.add_row(data_base=data, new_row=aa)
                except:
                    pass
            def add_item(data_base=None, item_to_add=None, create_if_notExist=True, database=None, hide=False):
                if data_base == None:
                    data_base=database
                try:
                    history.create_history(item_to_add, 'Add item', hide=hide)
                except:
                    pass
                #Used for the list types.
                global data_bases, lists
                num1=check_input(data_base)
                num2=check_input(item_to_add)
                pass_it=False
                try:
                    if profanityFilter.filter(item_to_add[0])==1:
                        print(errors.profanityDetected(var=item_to_add[0], user=user_logged))
                        pass_it=True
                        try:
                            if profanityFilter.filter(item_to_add[1])==1:
                                print(errors.profanityDetected(var=item_to_add[1], user=user_logged))
                                pass_it=True
                        except:
                            pass
                except:
                    pass
                if check.data_base_exists(data_base='logs')==True:
                    letter_spot=optimize.determ(letter=data_base[0])
                    if num1 == False and num2 == False:
                        if create_if_notExist == True:
                            failed=True
                            for i in range(len(lists)):
                                if (lists[i])[0] == data_base:
                                    failed=False
                                    break
                                failed=True
                            if failed==True:
                                lists.append([data_base,[]])
                        data_base=data_base.lower()
                        for i in range(len(data_bases)):
                            if (data_bases[i+letter_spot])[0] == data_base:
                                if (data_bases[i+letter_spot])[3]=="list":
                                    for x in range(len(lists)):
                                        if (lists[x])[0]==data_base:
                                            (lists[x])[1].append(item_to_add)
                                            break
                    if num1==True or num2==True and pass_it==False:
                        if hide==False:
                            print(errors.cannot_call_func('data_base.edit.add_item()'))
                else:
                    if hide==False:
                        print(errors.database_does_not_exist())
            def remove_item(data_base=None, item_to_remove=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(item_to_remove, 'Remove item', hide=hide)
                #Used for the list types.
                num1=check_input(data_base)
                num2=check_input(item_to_remove)
                global data_bases, lists
                letter_spot=optimize.determ(letter=data_base[0], set='opto_data')
                if num1 == False and num2 == False:
                    data_base=data_base.lower()
                    for i in range(len(data_bases)):
                        if (data_bases[i+letter_spot])[0]==data_base:
                            if (data_bases[i+letter_spot])[3]=="list":
                                for x in range(len(lists)):
                                    if (lists[x])[0]==data_base:
                                        try:
                                            (lists[x])[1].remove(item_to_remove)
                                            print(lists)
                                        except:
                                           pass
                                        break
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.remove_item()'))
            def add_row(data_base=None, new_row=None, split=True, database=None, hide=False):
                if data_base == None:
                    data_base=database
                if isinstance(new_row, str)==True:
                    history.create_history(new_row, 'Add row', hide=hide)
                #You can add as many objects to a row as you please, but it may not fit in your assinged constraints. No problems will occur though.
                if split==True:
                    new_row=new_row.split()
                #print(new_row)
                num1=check_input(data_base)
                num2=check_input(new_row)
                if num1 == False and num2 == False:
                    data_base=data_base.lower()
                    if isinstance(new_row, list) == True:
                        row.append([data_base,new_row])
                        #print("Added new row!")
                    if isinstance(new_row, list) == False:
                        print(errors.not_list())
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.add_row()'))
            def remove_row(data_base=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                num1=check_input(data_base)
                if num1 == False:
                    data_base=data_base.lower()
                    history.create_history(data_base, 'Remove row', hide=hide)
                    global row
                    rows=[]
                    rows_count=0
                    a=0
                    #Gather sets that correspond with called data_base
                    try:
                        for i in range(len(row)):
                            if (row[i-a])[0]==data_base:
                                rows.append(row[i-a])
                                row.pop(i-a)
                                a+=1
                                rows_count+=1
                    except:
                        pass
                    #Print known sets on screen.
                    for i in range(len(rows)):
                        print('#'+str(i)+' : '+str(rows[i]))
                    try:
                        a=input('Choose a set to delete: ')
                        try:
                            a=a.replace('#','')
                        except:
                            pass
                        a=int(a)
                    except ValueError:
                        print('Please enter the corresponding number #?')
                    #If input is correct then ask user if they wish to remove it.
                    if isinstance(a, int) == True:
                        if rows_count-1 >= a:
                            print('Remove:',rows[a])
                            choice = input('Are you sure(y/n): ').lower()
                            if choice == "yes" or "y":
                                rows.pop(a)
                            elif choice == "no" or "n":
                                print('No changes have occured.')
                            else:
                                print('Invalid response.')
                        if rows_count <= a:
                            print('That item does not exist.')
                    for i in range(len(rows)):
                        row.append(rows[i])
                if num1 == True:
                    print(errors.cannot_call_func('data_base.edit.remove_row()'))
                #Must be column_row
            def add_column(data_base=None, column_name=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(column_name, 'Add column', hide=hide)
                letter_spot=optimize.determ(letter=data_base[0], set='opto_data')
                num1=check_input(data_base)
                num2=check_input(column_name)
                global debug, data_bases
                if profanityFilter.filter(column_name) == 1:
                    print(errors.profanityDetected(var=column_name, user=user_logged))
                else:
                    found=False
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            found=True
                            break
                    if found==False:
                        print(errors.database_does_not_exist())
                    if num1 == False and num2 == False and found==True:
                        data_base=data_base.lower()
                        if debug==True:
                            print("Adding column at",data_base,"with name",column_name.lower())
                        for i in range(len(data_bases)):
                            if (data_bases[i+letter_spot])[0] == data_base:
                                if (data_bases[i+letter_spot])[3]=="column_row":
                                    (data_bases[i+letter_spot])[4].append(column_name.lower())
                    if num1 == True or num2 == True:
                        print(errors.cannot_call_func('data_base.edit.add_column()'))
            def remove_column(data_base=None, column=None, remove_row=False, database=None, hide=False):
                if data_base == None:
                    data_base=database
                try:
                    history.create_history(column, 'Remove Column', hide=hide)
                    num1=check_input(data_base)
                    num2=check_input(column)
                    found=False
                    letter_spot=optimize.determ(letter=data_base[0])
                    if num1 == False and num2 == False:
                        data_base=data_base.lower()
                        global data_bases, debug, row
                        for i in range(len(data_bases)):
                            if (data_bases[i+letter_spot])[0]==data_base:
                                if debug==True:
                                    print('Database Found!')
                                found=True
                                if (data_bases[i+letter_spot])[3] == "column_row":
                                    if debug==True:
                                        print("Correct data_base type!")
                                    if column in (data_bases[i+letter_spot])[4]:
                                        print("Removed: "+str(column))
                                        a=len((data_bases[i+letter_spot])[4])
                                        for e in range(a):
                                            if ((data_bases[i+letter_spot])[4])[e] == column:
                                                print(e)
                                                break
                                        (data_bases[i+letter_spot])[4].remove(column)
                                        print(data_bases[i+letter_spot])
                                        rows=[]
                                        rows_count=0
                                        a=0
                                        #Gather sets that correspond with called data_base
                                        try:
                                            for i in range(len(row)):
                                                if (row[i-a])[0]==data_base:
                                                    rows.append(row[i-a])
                                                    row.pop(i-a)
                                                    a+=1
                                                    rows_count+=1
                                        except:
                                            pass
                                        #Remove or Empty column(s) in row(s)
                                        if remove_row==False:
                                            for i in range(rows_count):
                                                ((rows[i])[1])[e]=None
                                        if remove_row==True:
                                            for i in range(rows_count):
                                                ((rows[i])[1]).pop(e)
                                        print(rows)
                    if num1 == True or num2 == True:
                        print(errors.cannot_call_func('data_base.edit.remove_column()'))
                    if found==False and data_base != None:
                        print(errors.database_does_not_exist())
                except:
                    pass
                #Goes through all lists for the column and changes it to equal None.
                #Must be column_row
            #Used for my carpentry app.
            class app:
                def rmBrokenTools():
                    a=0
                    for i in range(len(row)):
                        if (row[i-a])[0]=="tools":
                            try:
                                if ((row[i-a])[1])[6]==True:
                                    ((row[i-a])[1]).pop()
                                    a+=1
                            except:
                                pass
                    return "DONE"
                def remove_row(data_base=None, name=None, database=None, hide=False):
                    if data_base == None:
                        data_base=database
                    found=False
                    if isinstance(name, str) == True and isinstance(data_base, str) == True:
                        global row
                        for i in range(len(row)):
                            if (row[i])[0] == data_base:
                                if ((row[i])[1])[2] == name:
                                    row.pop(i)
                                    found=True
                                    break
                    else:
                        if hide==False:
                            print(errors.not_st())
                    return found
                def remove_item(data_base=None, barcode=None, database=None):
                    if data_base == None:
                        data_base=database
                    if isinstance(data_base, str) == True and isinstance(barcode, str) == True:
                        global lists
                        for i in range(len(lists)):
                            if (lists[i])[0]==data_base:
                                for x in range(len((lists[i])[1])):
                                    if (((lists[i])[1])[x])[0]==barcode:
                                        ((lists[i])[1]).pop(x)
                                        return True
                        return False
                    else:
                        print(errors.not_str())
                def show_tools(data_base=None, database=None):
                    if data_base == None:
                        data_base=database
                    if isinstance(data_base, str) == True:
                        for i in range(len(row)):
                            print('Item:',((row[i])[1])[0],' | Serial:',((row[i])[1])[1])
        class empty:
            def help():
                print('Branches:\n  data_base.empty.all()\n  data_base.empty.one()')
            #Clear all info in 1 or more databases.
            def all(hide=False):
                #Reset all data compiled for databases.
                history.create_history(None, 'Reset all databases', hide=hide)
                global lists, row
                lists=[]
                row=[]
            def one(data_base=None, recall=False, database=None):
                if data_base == None:
                    data_base=database
                #Empty all data compiled for one database.
                if recall==False:
                    num1=check_input(data_base)
                    if num1 == False:
                        a=0
                        global row, lists
                        for i in range(len(row)):
                            if (row[i-a])[0]==data_base:
                                row.pop(i-a)
                                a+=1
                        a=0
                        for i in range(len(lists)):
                            if (lists[i-a])[0]==data_base:
                                lists.pop(i-a)
                                a+=1
                    if num1 == True:
                        print(errors.cannot_call_func('data_base.empty.one()'))
        class retrieve:
            def databases():
                return data_bases
        class show:
            def help():
                print('Branches:\n  data_base.show.show_column()\n  data_base.show.show_row()\n  data_base.show.show_lists()\n  data_base.show.all_in_database()\n  data_base.show.all_data_bases()\n  data_base.show.info()')
            def show_column(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                if num == False:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if (data_bases[i])[3]=="column_row":
                                print((data_bases[i])[4])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_column()'))
            def show_row(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                #Must be column_row type
                global row
                if num == False:
                    for x in range(len(row)):
                        if (row[x])[0]==data_base:
                            print((row[x])[1])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_row()'))
            def show_lists(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                global lists
                if num == False:
                    for x in range(len(lists)):
                        if (lists[x])[0]==data_base:
                            print(lists[x])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_lists'))
            def all_in_database(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                global data_bases, row, debug, sets, rows, type
                sets=[]
                rows=[]
                type=None
                if num == False:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3] == 'list':
                                if debug==True:
                                    print('(System) List found')
                                type='list'
                                break
                            if (data_bases[i])[3] == 'column_row':
                                if debug==True:
                                    print('Data base found!')
                                type='column_row'
                                break
                    if type == "column_row":
                        if multi_process==False:
                            for x in range(len((data_bases[i])[4])):
                                sets.append(((data_bases[i])[4])[x])
                            for n in range(len(row)):
                                if (row[n])[0] == data_base:
                                    rows.append((row[n])[1])
                            print(sets)
                            for i in range(len(rows)):
                                print(rows[i])
                    if type == "list":
                        for i in range(len(lists)):
                            if (lists[i])[0]==data_base:
                                print((lists[i])[1])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.all()'))
            def all_data_bases():
                global data_bases
                print('Known databases:')
                for i in range(len(data_bases)):
                    print('  ',(data_bases[i])[0])
            def info(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                global data_bases, type
                if num == False:
                    type=None
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3] == 'list':
                                if debug==True:
                                    print('(System) List found')
                                    type='list'
                                    break
                            if (data_bases[i])[3] == 'column_row':
                                if debug==True:
                                    print('Data base found!')
                                    type='column_row'
                                    break
                    if type == "column_row":
                        print('Database Name:',(data_bases[i])[0])
                        print('Database status:',(data_bases[i])[1])
                        print('Database access:',(data_bases[i])[2])
                        print('Database type:',(data_bases[i])[3])
                    if type == "list":
                        print('Database Name:',(data_bases[i])[0])
                        print('Database status:',(data_bases[i])[1])
                        print('Database access:',(data_bases[i])[2])
                        print('Database type:',(data_bases[i])[3])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.info()'))
        class remove:
            def help():
                print('Branches:\n  data_base.remove.all()\n  data_base.remove.one_set()\n  data_base.remove.reset_to_standard()')
            def all(hide=False):
                history.create_history(None, 'Remove All', hide=hide)
                global data_bases, row, lists
                data_bases=[]
                lists=[]
                row=[]
            def one_set(data_base=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(None, 'Remove One Set', hide=hide)
                num=check_input(data_base)
                global data_bases, row, lists
                if num == False:
                    found=False
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            data_bases.pop(i)
                            found=True
                            break
                    for x in range(len(row)):
                        try:
                            if (row[x-1])[0]==data_base:
                                row.pop(x-1)
                        except IndexError:
                            pass
                    for x in range(len(lists)):
                        try:
                            if (lists[x-1])[0]==data_base:
                                lists.pop(x-1)
                        except:
                            pass
                if found == False and num == False:
                    print(errors.database_does_not_exist())
                if num == True:
                    print(errors.cannot_call_func('data_base.remove.one()'))
            def reset_to_standard(hide=False):
                history.create_history(None, 'Reset to Standard', hide=hide)
                try:
                    os.remove('data_save.py')
                except:
                    pass
        class create:
            def help():
                print('Branches:\n  data_base.create.database()')
            def database(data_base=None, database=None, status=True, type=None, owner='all', columns=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(data_base, 'Create Database', hide=hide)
                found1=False
                found2=False
                found3=False
                print(data_base)
                #Check to see if database already exists.
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        if hide==False:
                            print('That database already exists.')
                        found1=True
                        break
                if type not in allowed_types:
                    if hide==False:
                        print('An incorrect data type has been entered.')
                    found2=False
                if type in allowed_types:
                    found2=True
                for i in range(len(data_base)):
                    if data_base[i] in alphabet:
                        found3=True
                    if data_base[i] not in alphabet:
                        found3=False
                        if hide==False:
                            print('Database name can only consist of lowercase letters.')
                        break
                #Check database for profanity.
                if profanityFilter.filter(data_base)==1:
                    if hide==False:
                        print(errors.profanityDetected(var=data_base, user=user_logged))
                else:
                #If database doesn't exist continue on creating it.
                    if found3 == True and found2 == True and found1 == False:
                        if hide==False:
                            print('Database created!')
                        num1=check_input(data_base)
                        num2=check_input(type)
                        if num1 == False and num2 == False:
                            if isinstance(owner, str) == True and isinstance(type, str) == True and isinstance(owner, str) == True and isinstance(status, bool) :
                                if columns==None or isinstance(columns, list) == True:
                                    if type == "list":
                                        data_bases.append([data_base, status, owner, 'list'])
                                    if type == "column_row":
                                        if columns==None:
                                            data_bases.append([data_base, status, owner, 'column_row', []])
                                        if columns != None:
                                            data_bases.append([data_base, status, owner, 'column_row', columns])
                            if isinstance(status, bool) == False:
                                print(errors.not_bool(item='status'))
                            if columns != None and isinstance(columns, list) == False:
                                print(errors.not_list(item='columns'))
                            if isinstance(owner, str) == False:
                                print(errors.not_str(item='owner'))
                            if isinstance(data_base, str) == False:
                                print(errors.not_str(item='type'))
                            if isinstance(type, str) == False:
                                print(errors.not_str(item='data_base'))
                        if num1 == True and num2 == True:
                            print(errors.cannot_call_func('data_base.create.datebase()'))
    class password_restrictions:
        def help():
            print('Branches:\n  password_restrictions.check_password()\n  password_restrictions.set_min_length()\n  password_restrictions.set_max_length()')
        def check_password(password):
            pass_1=0
            if len(password)>min_length-1 and len(password)-1<max_length:
                for i in range(len(password)):
                    if password[i] in allowedPassword_chars:
                        pass_1=1
                    else:
                        print('Incorrect Item:',password[i])
                        return 0
            return pass_1
        def set_min_length(value=None, hide=False):
            global min_length
            history.create_history(str(value), 'Set min length', hide=hide)
            num=check_input(value)
            #Check if value is a number
            if num==False and isinstance(value, int) == True:
                #Assign new value
                 min_length=value
            if isinstance(value, int) == False:
                print(errors.not_int(item='value'))
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_min_length()'))
        def set_max_length(value=None, hide=False):
            global min_length, max_length
            history.create_history(str(value), 'Set max length', hide=hide)
            num=check_input(value)
            #Check if value is a number
            if num == False and isinstance(value, int) == True:
                #Check to see if value is bigger than min_length
                if value>min_length:
                    #Assign new value
                    max_length=value
                else:
                    print('')
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_max_length()'))
    class errors:
        def help():
            print('Branches:\n  errors.MissingCPP()\n  errors.FileDoesNotExist()\n  errors.NotSignedIn()\n  errors.BackupNameExists()\n  errors.profanityDetected()\n  errors.doesNotObeyRestrictions()\n  errors.database_does_not_exist()\n  errors.cannot_call_func()\n  errors.incorrect_perm()\n  errors.user_exists()\n  errors.user_not_found()\n  errors.not_list()\n  errors.not_str()\n  errors.not_bool()\n  errors.not_int()')
        def MissingCPP():
            global UtilizeCPPCode
            UtilizeCPPCode=False
            return ("Missing CPP File. Compile the file 'hello.cpp' as a shared library or import the libfoo.so file to the app root folder.") 
        def FileDoesNotExist(var):
            history.create_history(var, 'FileDoesNotExist', manual_record=auto_error_record, hide=debug)
            print('(Error) File does not exist.')
        def NotSignedIn():
            history.create_history('None', 'NotSignedIn', manual_record=auto_error_record, hide=debug)
            print('(Error) No user is signed in to allow this function to work.')
        def BackupNameExists():
            history.create_history('admin', 'BackupNameExists', manual_record=auto_filter_profanity, hide=debug)
            print('(Error) A backup with the same name already exists.')
        def profanityDetected(var, user):
            try:
                history.create_history(user, 'profanityDetected', manual_record=auto_error_record, add_desc=True, desc=user+' tried to use a curse word known as: '+var, hide=debug)
            except:
                print(errors.cannot_call_func('<Null>'))
            print('Not Alllowed: ',var)
        def doesNotObeyRestrictions():
            history.create_history('doesNotObeyRestrictions', 'Error', manual_record=auto_error_record, hide=debug)
            return('(Error) Password given does not meet the requirments.')
        def database_does_not_exist():
            history.create_history('database_does_not_exist', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) Database requested could not be found.'
        def cannot_call_func(var):
            history.create_history('cannot_call_func', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The function '+var+' that was called is missing 1 or more required variables.'
        def not_list(item=None):
            history.create_history('not_list', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A list was expected, but was not given.'
            if item != None:
                return '(Error) A list was expected, but was not given. Item: '+str(item)
        def user_not_found():
            history.create_history('user_not_found', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The user specified was not found.'
        def not_str(item=None):
            history.create_history('not_str', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A string was expected, but was not given.'
            if item != None:
                return '(Error) A string was excepted, but was not given. Item: '+str(item)
        def user_exists():
            history.create_history('user_exists', 'Error', manual_record=auto_error_record, hide=debug)
            return('(Error) This user already exists.')
        def not_bool(item=None):
            history.create_history('not_bool', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A bool was expected, but was not given.'
            if item != None:
                return '(Error) A bool was expected, but was not given. Item: '+str(item)
        def not_int(item=None):
            history.create_history('not_int', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A int was expected, but was not given.'
            if item != None:
                return '(Error) A int was expected, but was not given. Item: '+str(item)
        def incorrect_perm():
            history.create_history('incorrect_perm','Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The permission requested is not allowed.'
    if profanity_filter==True:
        profanityFilter.setup()
    if allow_windows_version == "11":
        allow_windows_version="10"
        #Windows 11 still thinks it's windows 10. I know, it's weird.
    if optimize_on_startup==True:
        optimize.run(hide=debug)
        #Optmize on startup if setting is set to True.
    if app_version_control==True and "-skipVersionCheck" not in n:
        #Checks what version the app was setup at.
        from version import setup_version
        if program_version != setup_version:
            try:
                open('history.txt','r')
            except:
                history.create()
            ah=open('history.txt','a')
            ah.write('\n('+d1+')'+' Program Version Control: Incorrect Version')
            ah.close()
            print('(Error) This program was setup on a different version.\nTo disable this prompt goto settings and set app_version_control to False.')
            exit()
    if system != 'windows' and system != "macos" and system != "linux":
        if quiteStartup == False:
            print('Invalid setting. system=')
        history.create_history(usage='Invalid Setting', user='system=Error()', hide=debug)
    from sys import platform
    if platform == "linux" or platform == "linux2":
        if quiteStartup == False:
            print('OS: Linux Distro.')
        systemDetectedOperatingSystem='linux'
        #Linux
        if system != "linux" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='linux', hide=debug)
            exit()
    elif platform == "darwin":
        if quiteStartup == False:
            print('OS: Mac OS')
        systemDetectedOperatingSystem='macos'
        # OS X
        if system != "macos" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='macos')
            exit()
    elif platform == "win32":
        if quiteStartup == False:
            print('OS: Windows')
        systemDetectedOperatingSystem='windows'
        # Windows
        if system != "windows" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='windows', hide=debug)
            exit()
    if setup_backup_response==True:
        if os.path.exists('count.py')==False:
            file=open('count.py','w')
            file.write('backup_count='+str(backup_startNumber))
            file.close()
            backup_count=backup_startNumber
    if quiteStartup == False:
        print('Cleaning Up Junk Files...')
    if clearHistoryOnStartup == True:
        try:
            os.remove('history.txt()')
            history.create()
        except:
            pass
    try:
        os.remove('barcode.png')
    except:
        pass
    if os.path.exists('backups')==False:
        os.mkdir('backups')
    try:
        os.remove('hash.txt')
    except:
        pass
    if os.path.exists('history_desc.py')==False:
        history.clear()
    try:
        from history_desc import history_id, history_description, count
    except:
        history.clear()
    if os.path.exists('data_save.py')==True:
        try:
            os.remove('data_save.aes')
        except:
            pass
    if os.path.exists('history.txt')==True:
        try:
            os.remove('history.aes')
        except:
            pass
    if resetCollections==True:
        if os.path.exists('collections')==True:
            shutil.rmtree('collections')
    if os.path.exists('collections')==False:
        os.mkdir('collections')
    try:
        abcd=open('data_save.aes', 'r').read()
        if abcd=="":
            os.remove('data_save.aes')
    except:
        pass
    try:
        abcd=open('history.aes', 'r').read()
        if abcd=="":
            os.remove('history.aes')
    except:
        pass
    if quiteStartup==False:
        print('Checking Settings...')
    check_settingsImproved(hide=logic.gate.not_gate(show_incorrect_settings))
    if quiteStartup == False and profanity_filter==True:
        print('Setting Up Profanity Filter...')
    profanityFilter.setup()
    if quiteStartup == False:
        print('\nSystem Started Correctly!')
    if time.time()-startupCount<.01:
        if quiteStartup == False:
            print('Est StartUp Time:', str(round(time.time()-startupCount, 2))+'<')
    else:
        if quiteStartup == False:
            print('Est StartUp Time:', round(time.time()-startupCount, 2))
    try:
        if "-release" in n:
            c=''
            beta=''
            while True:
                print("(1)Beta\n(2)Full\n")
                c=input('Is this a Beta or Full release: ')
                if c == "1" or c=="2":
                    break
            if c=="1":
                c="Beta"
                beta=input('What beta version is this: Ex: 1, 2, 3: ')
            if c=="2":
                c='Full'
            version_in=input('Enter the Version: Ex: 0.2.7 or hit enter: ')
            if version_in=="":
                version_in=program_version
            if beta != '':
                backup_name=version_in+' '+c+' '+beta
            else:
                backup_name=version_in+' '+c
            list2=['DestroyClient.py', 'client.py', 'termination.py', 'encrypt.py', 'UpdateProgram.py', 'count.py', 'custom_database.py','data.py','get_directory.py','files_to_backup.py','history_desc.py','patch_notes.txt','profanity.txt','requirements.txt','settings.py','shell.py','vars_to_save.py','version_config.py']
            beta1=input('Would you like to compress the save file also: ')
            if beta1=="yes" or beta1=='y':
                list2.append('data_save.py')
            #Backup Certian Files
            zipObject= ZipFile(backup_name+'.zip', 'w')
            for i in range(len(list2)):
                try:
                    zipObject.write(list2[i])
                except:
                    print('Could\'t find:',list2[i])
            zipObject.close()
        if "-v" in n:
            from settings import program_version
            print('Current Version: '+program_version)
            ex=True
        if "-info" in n:
            print('Created By Brandon Robinson.')
            print('GitHub: github.com/sukadateam')
            ex=True
        if "-reset" in n:
            list2=['version.pyc','directory.pyc','history_desc.pyc','count.py','data_save.py','version.py', 'directory.py','history.txt','hash_other.aes','hash.aes','hash_other.txt','hash.txt','settings.pyc','app.pyc','data.pyc']
            for i in range(len(list2)):
                try:
                    os.remove(list2[i])
                except:
                    print(list2[i],'not found')
            backup.clear_all()
            history.clear()
            try:
                shutil.rmtree('__pycache__')
            except:
                pass
            print('Exiting...')
            ex=True
    except:
        pass
    if "-help" in n:
        print('Current Arguments:\n  -skipVersionCheck (Bypasses Application Version Check)\n  -v (Prints Progam Version)\n  -info (Prints Import Info)\n  -reset (Resets Application)\n  -skipPythonCheck (Ignore Python Version)')
    if dontCloseAfterEmptyStart==True:
        input('Hit enter to Continue: ')
    #You may set a Normal level password
    #You can set a global password if need be. Basically a backup.
    #To trick the system in thinking it's running on another os, systemDetectedOperatingSystem='your os'. windows, macos, linux
    #Test bench
    #<--Indent to here