# File Organizer 


## Fast and Simple File organization tool
With school starting again and always downloading from the internet, I wanted to find a simple way to organize my downloads folder. 
Using the power of python, I was able to develop off of an existing script from [GeeksforGeeks](https://www.geeksforgeeks.org/junk-file-organizer-python/).

Instead of having a defined dictionary with only certain folders created, I thought it was better to have an individualized folder for each type of extension. For example:
- Instead of having a Code folder that accepted .py, .js, etc..
- I wanted there to be a folder for .py code, .js code, and so on.

The way this script works is:
username@user: python file_organizer.py 'Directory you want to organize'

After running, it will output: 
Would you like to keep this program running in the background? Y/N -->

The user then can choose y or n

If the user chooses 'y', the script will run in the background and update the directory very 20 seconds. If a new file is detected, then the file will be moved to the appropriate folder if one doesn't exist. Since it is running in the background, their is no exit, you can just press CTRL+C to quit the script.

If the user chooses 'n', the script will run once. It will scan the current directory and all its files/folders and move those files to the appropriate folder.

### Enjoy organizing your files!! 

