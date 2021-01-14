# File Organizer 


## Fast and Simple File organization tool using python3
With school starting again and always downloading from the internet, I wanted to find a simple way to organize my downloads folder. 
Using the power of python, I was able to develop off of an existing script from [GeeksforGeeks](https://www.geeksforgeeks.org/junk-file-organizer-python/) and I also implemented an event watcher using the library **watchdog**. Got the source code idea from: [Python Hosted](https://pythonhosted.org/watchdog/quickstart.html#quickstart).

Started off by creating a dictionary with Directories depending on the type of extension. For example: If we had Code (.py, .cpp, etc..) and Documents (.pdf, .doc, etc..) files in a directory, the script would run, scan the the files, scan the current directory, create Directories (if non existent) and put those files in the appropriate place.

The way this script works is:
username@user: python file_organizer.py 'change'

Change --> put in your diretory path. If I want to organize my Downloads directory, the path would be: /Users/username/Downloads
- Script would look like: username@user: python file_organizer.py /Users/username/Downloads

This script takes in the systems argument (change) to automatically locate the path and scan the directory and organize. No need to hardcode the path in the .py code, unless you want to only run the script for that directory all the time.

After running, it will output: 
Would you like to keep this program running in the background? Y/N -->

If the user chooses 'y', the script will run in the background and update the directory very 20 seconds (can be changed). If a new file is detected, then the file will be moved to the appropriate folder if one doesn't exist. Along with moving the file, using watchdog, it will also inform you of any action going on in the directory. It will print out the appropriate message based on the event.

If the user chooses 'n', the script will run once. It will scan the current directory and all its files/folders and move those files to the appropriate folder.

For more information on the functionality of the script, please look at the python file and read through the comments. 

### Enjoy organizing your files!! 

#### Feel free to change and use as you want.

**Disclaimer**

This does use some libraries that are only available for python3, so if you don't have python3 in your environment, it would be great if you installed it, and installed any libraries you might be missing when running the script.
