import threading
import time

my_var=19231
'''
I need to create a var that will lock the value because multbytwo and divbytwo are opposites
we are trying to reach a number but it will never reach it because one doubles while the other halves
This means we remain in our current spot

'''
my_lock=threading.Lock()

def multbytwo():
    #I use the global keyword because I want to change the global var(my_var)
    #or else I cannot manipulate it
    global my_var,my_lock
    #This method tries to get the lock if its free if its not free we are just on standby
    #If another function locks the resource we cannot lock it again
    my_lock.acquire()
    while my_var < 38462:
        my_var *= 2
        print(my_var)
        #Sleep(meaning wait) for x number of seconds
        time.sleep(3)
    print("Reached The Maximum 968 6342 56837")
    #Now I must release the lock so that the next function can use it
    my_lock.release()

def divbytwo():
    global my_var,my_lock
    my_lock.acquire()
    while my_var >1:
        my_var /= 2
        print(my_var)
        time.sleep(3)
        #Now I must release the lock so that the next function can use it
    print("Reached The Minimum") 
    my_lock.release()

#Now I must execute two threads simultaneously
my_fir_thread=threading.Thread(target=divbytwo)
my_sec_thread=threading.Thread(target=multbytwo)
my_fir_thread.start()
my_sec_thread.start()

#AS YOU CAN SEE ONLY 1 THREAD CAN ACCESS THE RESOURCE
