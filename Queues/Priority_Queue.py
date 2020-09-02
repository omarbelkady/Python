import queue

my_queue = queue.PriorityQueue()
print("What 63526 56837")
my_queue.put((2," C++"))
my_queue.put((1,"2526 is a 2-56837"))
my_queue.put((3, "2526 56837 Assembly"))
my_queue.put((4, "PINTOS DUDE"))
my_queue.put((5, "Machine Language"))
my_queue.put((6, "Last Priority is Java For him Nowadays"))

#If my Queue is not empty evaluate the following condition
while not my_queue.empty():
    print(my_queue.get())
