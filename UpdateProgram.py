#Terminal Version to download and install updates. A Visual version will release after this project is done.

#This Program utilizes the system terminal to download, sync, and install updates.
#If your terminal is blocked for security reasons. You may need to install updates manually.
#Please make sure git is installed. This script won't work without it.

#Import required moduels
from ast import arguments
import os #For file editing
import sys #Argmunent sending
import shutil #For folder deleting
import subprocess as sp
from custom_database import exit, clear, path #Used to close the app.

#Clear the system afer imports are finished.
clear()
#Remove Old UpdateFolder if it exists.
try:
    shutil.rmtree(
        "UpdateFolder"
)
except:
    #Folder doesn't exist
    pass
#Grab the latest source code and store it in a file called UpdateFolder
os.system('git clone https://github.com/sukadateam/database UpdateFolder')

#Check to see if the folder exists and all the needed items are present
#If any requirements are missing then terminate proccess and return an Error.
#Do Not Attempt to install to prevent data corruption!
output = sp.getoutput('cd UpdateFolder\ncd database\nls')
print ('\n\nFiles Downloaded\n',output)

#Search for command file. Used to determine what needs to be updated.
try:
    from UpdateCommands import UpdateRequirments, UpdateDatabase, UpdateSaveFile, UpdateApplication, UpdateSettings
except:
    clear()
    print('UpdateCommands.py File seems to be missing or misplaced. Please check and try again.')
    exit()
print(
    "\n!Files downloaded!"
    "\nUpdate Settings:\n  UpdateRequirments: ",
    UpdateRequirments,'\n  UpdateDatabase:    ',
    UpdateDatabase,'\n  UpdateSaveFile:    ',
    UpdateSaveFile,'\n  UpdateApplication: ',
    UpdateApplication,'\n  UpdateSettings: ',
    UpdateSettings
    )

print("\nPre-install checks in progress...")
#Check to ensure all file required are present.
allChecksPass=True
if UpdateRequirments==True:
    if os.path.exists('requirements.txt') == True:
        print('  UpdateRequirments Test: Passed')
    else:
        print('  UpdateRequirments Test: Failed')
        allChecksPass=False
if UpdateDatabase==True:
    if os.path.exists('custom_database.py') == True:
        print('  UpdateDatabase Test: Passed')
    if os.path.exists('custom_database.py') == False:
        print('  UpdateDatabase Test: Failed')
        allChecksPass=False
if UpdateApplication==True:
    if os.path.exists('app.py') == True:
        print('  UpdateApplication Test: Passed')
    if os.path.exists('app.py') == False:
        print('  UpdateApplication Test: Failed')
        allChecksPass=False
if UpdateSettings==True:
    if os.path.exists('settings.py') == True:
        print('  UpdateSettings Test: Passed')
    if os.path.exists('settings.py') == False:
        print('  UpdateSettings Test: Failed')
        allChecksPass=False
#Save file does not need to be checked. As it wasn't downloaded.
if allChecksPass==False:
    print("One or more tests have failed. Continue? ")
    UserInput=input('Yes or No: ').lower()
    if UserInput=="no" or UserInput=="n":
        UserInput=input('Remove the downloaded content: ')
        if UserInput==True:
            shutil.rmtree(
                "UpdateFolder"
            )
        #Exits the program and terminates the proccess.
        print("!Program will now terminate!")
        os._exit(1)
    print("Problems May Occur!")

#Update Given Prerequisites
InputVars=[UpdateDatabase, UpdateApplication, UpdateSettings, UpdateRequirments]
InputFiles=['custom_database.py', 'app.py', 'settings.py', 'requirements.txt']
for i in range(len(InputVars)):
    #If given var is equal to true then go ahead and apply the update to it's corresponding file.
    if InputVars[i]==True:
        #Saves the current version just incase if update fails as temp.py.
        os.rename(InputFiles[i], 'temp.py')
        #Removed the current app.py file.
        try:
            os.remove(InputFiles[i])
        except:
            pass
        #Copies the new *.py file.
        shutil.copyfile(
            path+'/UpdateFolder/database/'+InputFiles[i],
            path+'/'+InputFiles[i]
        )
        #If an error did occur revert back to old version.
        try:
            if i==0:
                import custom_database
            elif i==1:
                sys.argv.append('--test')
                import app
            elif i==2:
                import settings
        except Exception as error:
            print('An Error Has Occured in the update proccess. Info is displayed below.')
            print(error)
            try:
                os.remove(InputFiles[i])
            except:
                pass
            #Restores temp.py back to orginal name.
            os.rename('temp.py', InputFiles[i])
        print(InputFiles[i]+" has been updated.")
print('Application fully updated! Please close any tabs of this program and restart!')