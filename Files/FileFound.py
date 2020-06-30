import os

syspath=r"/home"
#this outputs a list/array of files within your directory
print(os.listdir(syspath))

def CreateOrFound(myFile):
    if os.path.exists(myFile):
        print("This file is already in our directory")
        return
    
    #Write(w) mode deletes the contents of the file and writes what you told it
    #Append(a) mode overwrites your file and saves it. It is simply keeping your old version and appends to it. 
    
    mine=open(myFile,'w')
    try:
        mine.write("Hello There Everyone.\r\n I just created a new line for ya, bounce!")
        #For good coding practice. Because we create a file and shove it in memory. So now
        #I free up memory by using the flush() command
        mine.flush()
        
    except Exception as e:
        print(e)
    finally:
        if mine is not None:
            #None means not been assigned and not There
            mine.close()
CreateOrFound(syspath)
