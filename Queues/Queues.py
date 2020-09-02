import queue

#How to Create a queue
my_q= queue.Queue()
#A queue takes a number and then uses it goes back and uses another number which I
# I haven't used and uses and pops the number out of the list everytime it uses itONCE
my_numbers=[2,56,837,4700,63527]
#Each thread will take one of the numbers and process the numbers for many diff
# We want multiple threads to obtain data concurrently from a source
'''
reasons: e.g:
    * port check
    * factorial calc
'''
# Next it will go to the next element which hasn't been processed yet
for nums in my_numbers:
    my_q.put(nums)

print(my_q.get())#prints 2
#.get method gets the first element and works out to FIFO

#To Create a LIFO queue
q= queue.LifoQueue()
numbers= [1,2,3,4,5,6,7]
for my_nums in numbers:
    q.put(my_nums)
print(q.get())#outputs 7
