class Queues:
    class Node:
        def __init__(self,element,_next):
            self.element=element
            self._next=_next
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,element):
        new_node = self.Node(element,None)
        if self.isEmpty():
            self.head=new_node
        else:
            self.tail._next=new_node
        self.tail=new_node
        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            return("Empty Queue")
        result=self.head.element
        self.head=self.head._next
        self.size -=1
        return result
