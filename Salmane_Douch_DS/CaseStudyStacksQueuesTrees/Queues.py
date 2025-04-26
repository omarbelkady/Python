
from collections import deque
class Node:
    def __init(self):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.tail = None
        self.head = None
    def enqueue(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def dequeue(self):
        if self.head==None
            raise ValueError("queue empty")
        else:
            return_value = self.head.value
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return return_value


