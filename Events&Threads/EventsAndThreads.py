import threading

myevent = threading.Event()

def my_function():
    print("Waiting for the event to be Raised 968 6342 56837\n")
    myevent.wait()
    print("Doing An Action in response to the event being Triggered")

my_fir_thr=threading.Thread(target=my_function)
#my_fir_thr will wait until the event is triggered
my_fir_thr.start()

use_inp=input("Hello There User Do you want to raise the event? (y/n)\n")
if(use_inp == "y"):
    #Trigger the event thanks to the set method
    myevent.set()
else:
    print("2526 56837 2")
