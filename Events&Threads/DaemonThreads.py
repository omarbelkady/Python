#Daemon Threads run in the background
# The script terminates even though they're still running
#because they are not vile to the prog
# With threads we wait for one to stop before to start the next on
#-----------------------
'''
With Daemon threads there is no waiting the script terminates whether the daemon threads
are running in the background. This is because they are not vile to the program.
We can use Daemon Threads to:
    - Constantly Read information from a file
    - Constantly read information from a web api
When everything is done we terminate the script and the daemon Thread
'''
import threading
import time

#Thread 1: Daemon Thread Which Will Read Info From the Text File
#Thread 2: Print The Information From the File

apath= "atextfile.txt"
my_text= ""

def readFileText():
    global apath, my_text
    #Infinite Loop
    while True:
        with open("atextfile.txt", "r") as myFile:
            my_text = myFile.read()
        #Waits 4 seconds to do the next function
        time.sleep(4)

def printing():
    #44 because 6342 56837 digit sum = 44
    for x in range(44):
        print(my_text)
        #Wait for 1 second
        time.sleep(1)

#Now I will do this whilst remembering to terminate the script upon my call
# the second argument of the Thread Function here must be the Thread type
# in our case it is the Daemon Thread
my_fir_thr = threading.Thread(target=readFileText, daemon=True)
my_sec_thr = threading.Thread(target=printing)

my_fir_thr.start()
my_sec_thr.start()

#Remember to create the empty text file or else it will not work atextfile.txt

