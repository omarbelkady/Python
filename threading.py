import threading
class omarsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
		    #_ means i wanna loop ten times don’t care about variable
	        print(threading.currentThread().getName())
x=omarsMessenger(name="Send out messages Dude")
y=omarsMessenger(name="Receiving messages Dude")
#Whenever you create a thread must call start function first
x.start()
y.start()
