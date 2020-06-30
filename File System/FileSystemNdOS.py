from os import path

#\n is not read as a new line and \t is not 
#read as a tab instead the full path of the file remains intact
#Each one of the slashes that tells us the different directories
#of path will be regarded by the compiler as and escape char
#\t= tab \r= return a new line. To get around it is to do a \\.
#To make a string literal you put the r letter so that when we print
#the full path of a file

stringPath= r"/home"

'''
#printing a path object will print ., .. is your parent directory! e.g. in Linux cd .. means go back one directory
print("The current directory I am on is: %s" %path.curdir)

print("The absolute path is: %s" %path.abspath(path.curdir))
print("The directory name is: %s" %path.dirname(path.curdir))
print("The directory base name is: %s" %path.basename(path.curdir))
'''
#I will replace curdir with string Path
print("The current directory I am on is: %s" %stringPath)
print("The absolute path is: %s" %path.abspath(stringPath))
print("The directory name is: %s" %path.dirname(stringPath))
print("The directory base name is: %s" %path.basename(stringPath))
print("The path is/isn\'t existing: %s" %path.exists(stringPath))
print("This is/isn\'t a directory: %s" %path.isdir(stringPath))
print("The file exists: %s" %path.isfile(stringPath))
