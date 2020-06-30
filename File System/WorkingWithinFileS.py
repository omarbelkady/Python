import os
syspath=r"/home"

#this outputs a list/array of files within your directory
print(os.listdir(syspath))
"""
for roots, dirs, files in os.walk(syspath):
    #walk will literally loop through the entire directory structure
    #it will determine what is a file, directory or a root
    for dir in dirs:
        print("Directory = %s" %dir)
    for roots in files:
        print("File = %s" %file)
    for file in files:
        print("File = %s" %file)
"""

"""
Here's a better way to write the above lines of code
"""

#Get the root. next command jumps to the next iterator in the group
myRoot=next(os.walk(syspath))[0]
print("Roots: %s"%myRoots)

#Get the directories only
myDirs=next(os.walk(syspath))[1]
print("Directories: %s"%myDirs)

#Get the Files only
myFiles=next(os.walk(syspath))[2]
print("Files: %s"%myFiles)
