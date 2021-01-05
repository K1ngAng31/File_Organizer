# ==========================
#  	LIBRARIES USED
import os
import collections
from pprint import pprint
import sys
import time
# ==========================


# ============================
# FUNCTION WHERE WORK IS DONE
# ============================
def organize():
	SYS_ARG_PATH = os.path.normpath(sys.argv[1]) #input path for directory to organize
	# If you want to hardcode a path you can change sys.argv[1] --> 'to your path'

	# File type to folder
	DIRECTORIES = collections.defaultdict()
	for name_of_file in os.listdir(SYS_ARG_PATH):
	    if not os.path.isdir(os.path.join(SYS_ARG_PATH, name_of_file)):
	        type_of_file = name_of_file.split('.')[-1]
	        DIRECTORIES.setdefault(type_of_file, []).append(name_of_file)

	# pprint(DIRECTORIES)

	# Move all files into their folder
	for name_folder, items_in_folder in DIRECTORIES.items():
	    folder_path = os.path.join(SYS_ARG_PATH, name_folder)
	    # If the file does not exist, create new directory
	    if not os.path.exists(folder_path):
	        os.mkdir(folder_path)

	    for folder_item in items_in_folder:
	    	# Get the file name
	        source = os.path.join(SYS_ARG_PATH, folder_item)
	        # Move the file to appr. folder
	        destination = os.path.join(folder_path, folder_item)
	        # This will print full path of file moving from and to
	        # print(f'Moving {source} to {destination}')
	        # Rename the new dir
	        os.rename(source, destination)

# ============================
# 	  MAIN
# ============================
if __name__ == '__main__':
	ask = input("Would you like to keep this program running in the background? Y/N --> ")
	ask = ask.lower()
	if ask == 'y':
		#This will keep script running
		#Every 20 seconds it will scan for new files and if new file is in the 
		# directory, it will move it to its appropriate place
		while True:
			organize()
			time.sleep(20)
	if ask == 'n':
		print('=================================================')
		print('\t\tRUNNING ONCE')
		print('=================================================')
		organize()



		# ========================================
		# To Exit when running in the background
		# press ctrl + c
		# ========================================





