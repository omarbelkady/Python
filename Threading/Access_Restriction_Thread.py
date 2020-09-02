#Multiple threads can access the resource but not an unlimited number ofthreads
import threading
import time

#Step 1 define a semaphore
my_semi_phore = threading.BoundedSemaphore(value=4)

'''
Step 2: define a function that will gain access to the resource
which takes in a thread number as an argument so that we know
which thread is trying to access which resource
'''
def access_the_resource(thread_val):
    print("The {}nth thread is trying to access the resource".format(thread_val))
    '''
    acquire the semaphore if we haven't had 4 accesses already or if it hasn't 
    been 4 times acquired without have been released we will be granted access 
    automatically to the resource
    '''
    my_semi_phore.acquire()
    print("The {}nth thread was granted access".format(thread_val))
    #acquire the resource for 4 seconds then print sth to the console
    time.sleep(4)
    print("The thread number:{} is now being released".format(thread_val))
    #Release the thread
    my_semi_phore.release()

for thread_val in range(1,25):
    #I specify the target function as the resource accessor
    #I have to supply as the 2nd parameter the thread number using the args keyword
    my_iter_num = threading.Thread(target=access_the_resource, args=(thread_val,))
    my_iter_num.start()
    time.sleep(2)
