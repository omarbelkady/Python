import threading
def ording_func():
    #46 is the sum: 6+3+4+2+5+6+8+3+7+2
    for x in range(46):
        print("ONE")



#As you can see I cannot execute function 1 and two at the same time simply by calling them
# another_func cannot start until the ording_func is finished executing Thanks to 
# Threading though both functions can execute concurrently


def regular_fun():
    print("2526 LO83S C AND PINTOS")

'''
Create a New Object of the thread class and we pass in the worker function to the thread
As you can see we are not calling the function because there aren't a set of parenthesis
to tell the compiler that this is the function we want to use

Threads allows us to execute two functions at the same time which work in parallel
'''
my_thread= threading.Thread(target=ording_func)
my_secnd_thread = threading.Thread(target=regular_fun)
'''IF I do not tell the function to wait after it finished looping through the first thread 
to finish it will not do it. The Threads will run in parallel
'''
my_thread.start()
#Do not execute the my_secnd_thread until my_thread has finished
my_thread.join()
my_secnd_thread.start()
