# =======================================================
# LIBRARIES USED
import os, sys, time
import collections, constants
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
# =======================================================


# ====================================================================================
# DICTIONARY FOR DRIECTORIES BASED ON THEIR TYPES
# FEEL FREE TO ADD OR MODIFY TO YOUR USE
TYPE_DIR ={   
    "HTML": ["html5", "html", "htm", "xhtml"], 
    "IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg", 
               "heif", "psd"], 
    "VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng", 
               "qt", "mpg", "mpeg", "3gp"], 
    "DOCUMENTS": ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods", 
                  "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox", 
                  "rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt", 
                  "pptx"], 
    "ARCHIVES": ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z", 
                 "dmg", "rar", "xar", "zip"], 
    "AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3", 
              "msv", "ogg", "oga", "raw", "vox", "wav", "wma"], 
    "PLAINTEXT": ["txt", "in", "out"], 
    "PDF": ["pdf"], 
    "Code": ['py','css','js','html', 'cpp', 'ipynb', "html5", "html", "htm", "xhtml"], 
    "XML": ["xml"], 
    "EXE": ["exe"], 
    "SHELL": ["sh"] 
    }
# ====================================================================================

# ====================================================================================
# THIS PATH IS BASED ON THE ARGUMENT GIVEN ON THE TERMINAL
# IT CAN BE HARDCODED WITH A DIRECT PATH
# JUST REPLACE sys.argv[1] WITH YOUR path --> '/Path/to/directory'
SYS_PATH = os.path.normpath(sys.argv[1])
PATHTOBEOBSERVED = SYS_PATH
# ====================================================================================

# ====================================================================================
# THESE FUNCTIONS WERE CREATED TO HANDLE THE EVENTS OF WHAT WAS GOING ON IN THE DIR.
# IF SOMETHING IS ADDED/MOVED/DELETED/CREATED IT WILL NOTIFY YOU ON THE TERMINAL
# THESE ARE USED USING THE WATCHDOG LIBRARIES
def on_created(event):
	print(f'\t\t[Created] -- [{event.src_path}]')
def on_deleted(event):
	print(f'\t\t[Deleted] -- [{event.src_path}] ')
def on_modified(event):
	print(f'\t\t[Modified] -- [{event.src_path}]')
def on_moved(event):
	print(f'\t\t[Moved] -- [{event.src_path}] to [{event.dest_path}]')
# ====================================================================================


# =======================================================================================================================
# THESE FUNCTIONS HANDLE THE MOVEMENT OF FILES AND ORGANIZATION TO THEIR APPROPRIATE DIRECTORIES
def move_file(file_name, dir_type):#take in file name, directory type
	#Create the location of the directory and added it to the Path
	dir_loc = os.path.join(SYS_PATH, dir_type)
	#If no such directory exist in path, make directory
	if not os.path.exists(dir_loc):
		os.mkdir(dir_loc)
	#Move file to that directory based of their extension
	shutil.move(file_name, dir_loc)

def organize():# MAIN FUNCTION
	#Create a List format of type: file type: dir type
	file_types = {file_type:dir_name for dir_name, file_types in TYPE_DIR.items() for file_type in file_types}

	#Read all files
	all_files = [f for f in os.listdir(SYS_PATH) if os.path.isfile(os.path.join(SYS_PATH, f))]

	#Iterate through the files
	for file_name in all_files:
		#Split the file 
		splitted_text = file_name.split('.')
		if len(splitted_text) > 1:
			ext = splitted_text[-1].lower()
			#If the extension split is in the type in our Directory Dict move the file to the appropriate Directory
			if ext in file_types:
				move_file(os.path.join(SYS_PATH, file_name), file_types[ext])
			else: #If a file extension is unknown, let user know
				print(f'\t\t[ERROR] Unknown File: {splitted_text[-1]}')
# =======================================================================================================================

# =======================================================================================================================
if __name__ == '__main__':
	# THE IDEA IS TO HAVE THIS PROCESS AUTOMATED
	# THEREFORE, ASK THE USER IF THE PROGRAM SHOULD BE RUNNING IN THE BACKGROUND
	# THIS MEANS THAT EVERY 20 SECONDS (CAN BE CHANGED), THE PROGRAM WILL RUN AND MOVE ANY FILES THAT MIGHT HAVE
	# BEEN ADDED TO THE DIRECTORY. NO NEED TO WORRY ABOUT HAVING TO RUN THE PROGRAM OVER AND OVER
	ask = input('\n\t Would you like to keep this program runnning in the background? (Y/N) --> ')
	ask = ask.lower()

	#IF USER CHOOSES YES
	if ask == 'y':
		# ************************************************************************************************************
		# THIS PART OF THE CODE IS TO HANDLE THE EVENTS THAT ARE GOING ON IN THE DIRECTORY
		# THIS MEANS THAT IF YOU RUN THE PROGRAM AND LEAVE IT RUNNING, ONCE IT ORGANIZES THE FILES TO THE DIR, IF USER
		# DECIDES TO ADD MORE FILES, IT WILL HANDLE THOSE EVENTS AND LET THE USER KNOW THAT THOSE FILES WERE ADDED TO 
		# THE PATH. IT WILL PRINT OUT THE APPROPRIATE MESSAGE BASED ON THE EVENT, USING THE FUNCTIONS CREATED ABOVE
		# FOR MORE INFORMATION ON HOW THIS WORKS
		# https://pythonhosted.org/watchdog/quickstart.html#quickstart
		patterns = '*'
		ignore_patterns = ''
		ignore_directories = False
		case_sensitive = True
		my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

		my_event_handler.on_created = on_created
		my_event_handler.on_deleted = on_deleted
		my_event_handler.on_modified = on_modified
		my_event_handler.on_moved = on_moved

		path = PATHTOBEOBSERVED

		my_observer = Observer()
		my_observer.schedule(my_event_handler, path, recursive = True)
		# ************************************************************************************************************
		# THIS STARTS THE OBSERVER
		my_observer.start()
		try:
			while True: # WE CREATE AN INFINITE LOOP TO KEEP RUNNING IN THE BACKGROUND
				print('\t\t[To Quit] Press CTRL + C') # TO QUIT THE PROGRAM
				organize() # CALL OUR MAIN FUNCTION
				time.sleep(20) # THIS CAN BE MODIFIED TO RUN AT A LONGER PERIOD OF TIME
		except KeyboardInterrupt: # IF USER PRESSES CTRL + C
			my_observer.stop() # STOP THE OBSERVER, EXIT THE PROGRAM
		my_observer.join()
		# ************************************************************************************************************
	if ask == 'n': # IF USER CHOOSES NO, JUST RUN ONCE AND ORGANIZE SUCH FILES IN THE DIRECTORY
		print('\t===========================================')
		print('\t\t\t RUNNING ONCE')
		print('\t===========================================')
		organize()
# =======================================================================================================================
