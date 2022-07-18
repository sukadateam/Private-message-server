'''Used universally between both the client and host.
Neither client nor host can edit this file. Only the end user.
You cannot edit this file midway; during the program operation(s). Shutdown is required.
'''
testExpermintalFeatures=False

#User Settings --(FOR USERS)--

#Required python version to run program.
required_version=['3.10.0','3.10.1','3.10.2','3.10.3','3.10.4']
#Application version. Just for show.
program_version='0.6.7'
#Drive letter to store hash.aes file on root directory. Letter must be Uppercase. Windows only.
drive_letter='E'
#Drive name to store hash.aes file on root directory. Linux only. Setting is not required to be changed.
drive_name='Computer'
#Operating System or OS. Can be macos, windows or linux. Must be lowercase.
system='macos'
#Filters bad words that people should not be using.
profanity_filter=True
#A backup password in case the other is forgotten.
global_password=True
#App version control --(Disable if needed)--
app_version_control=False
#Only allow set operating system. Change system variable to your choice.
set_operating_system=False
#Allowed windows versions. You can choose 7, 8, 10, 11. Only works if system setting is set to windows.
allow_windows_version='10'
#min and max password lengths, and allowed characters
min_length=5 #Cannot be smaller than 5
max_length=25 #Cannot be bigger than 99
allowedPassword_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*()# '
#What is the name of your printer? For macOS. Windows uses default.
printer_name='iDPRT_SP310'














































#Developer Settings --(NOT USER SETTINGS!)-- Developer Settings

#Skip python check.
skip_pythonCheck=True
#Enable automated history_file for functions
auto_history_record=True
#Don't load save file. True: Skip save file -- False: Load defualt file not save file.
dont_load_save=False
#Automatically optimize on start up. USE AT YOUR OWN RISK. Currently in development phase.
optimize_on_startup=False
#If a prior task is equal to the current task, system will then ignore the task given.
skip_history_copy=True
#Enable automated history_file for functions. 
auto_error_record=True
#Quit app if one or more settings are incorrect. For safety purposes do not disable.
quit_ifIncorrect=False
#Record a more informed description of a item in history.txt
advanced_history=True
#Automatically check inputs for profanity. May use more CPU power than normal.
auto_filter_profanity=True
#Attempt to speed up the search on inputs by using a smaller version of profanity.txt. Only works if auto_filter_profanity is set to True.
auto_filter_profanity_speedBoost=False
#An attempt to use more than one cpu core. #Currently Not Functional.
multi_process=False
#Assign Digit number to history item for a more depth look into the item. And create a database to handle all the data for each assigned item.
assign_digit_forHistory=True
#How many digits are allowed to be used to store history. Max 30.
allowed_digists_forHistory=8
#Will still check for incorrect settings if quit_ifIncorrect is True, but won't display anything.
show_incorrect_settings=False
#Will deny the program from saving. No matter what. Will cause problems for long term.
disable_save=False
#Passwords have to meet the requirments set above.
strict_password=True
#If True system will not remove files after encrypt and decrypt. Will remove files if set to False.
do_not_remove=True
#Do not disable failsafe unless needed! Trust me. Don't disable it.
fail_safe=True
#Disable profanity filter for admin.
disable_filter_admin=False
#After ? startups. Remove backups from ? long ago.
retain_backup_time=25 #Startups
#Clear collections folder on app startup.
resetCollections=True
#If a setting is missing, not present, or not there, skip it.
skip_missing_settings=True
#Backups goes in order of numbers and this var changes where it starts. Only works on first backup.
backup_startNumber=1
#Allowed permissions to create, remove, edit backups.
#User must be signed in to create a backup.
allowed_backupPermissions=['admin','teacher']
#Setup backup response. Do not disable if using backup. Used for debugging.
setup_backup_response=True
#If custom_database.py is not started from an import. Do not close it.
dontCloseAfterEmptyStart=False
#If True, Encrypt Important files with given password. Else: Backup with no password.
encryptBackups=False
#Keep the terminal hush hush on startup. Only major errors will show.
quiteStartup=False
#Print in the terminal if prints fail and what printer it is using.
printer_debug=True #Default True
#Clears history file after each startup.
clearHistoryOnStartup=False

#Settings coming soon. Do not change unless your a dare devil.
#DarkMode For app.py.
darkModeApp=False
#Gives the app some color. darkModeApp and colorMode cannot be set to True at the same time.
colorMode=True
#Speeds up computation. May Not ever be fully functional :(
UtilizeCPPCode=True
#Limits the amount of characters in a given string when writen to a text file.
Output_file_MaxLength=35


#Remove if you aren't using my custom application.
#Settings for application.
show_background=True
button_color='white'
option_color='white'
bg_color='#80a8e8'
text_color='#000000'
button_height=2
button_width=15
text_font=30
entry_background_color='White'
entry_text_color='Black'
OnlyAllowKnownStudents=False
secretsAllowed=False
side_tilt=200
AskForEncryptionPassword=False
if colorMode==True:
    bg_color='red'
    text_color='blue'
    button_color="orange"
    option_color='green'
if darkModeApp==True:
    bg_color='#231F20'
    text_color='#000000'
    button_color="grey"
    option_color='white'