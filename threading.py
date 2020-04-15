import threading
class omarsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
		    #_ means i wanna loop ten times don’t care about variable
	        print(threading.currentThread().getName())
x=omarsMessenger(name="Send out messages")
y=omarsMessenger(name="Receiving messages")
