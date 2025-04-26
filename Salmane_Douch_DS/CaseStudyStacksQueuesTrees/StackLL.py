class Stack:
    class Node:
        def __init__(self,value):
            self.value=value
            self.next=None

    def __init__(self):
        self.head=None
        self.size=0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size==0

    def push(self,value):
        self.head=self.Node(value,self.head)
        self.size+=1

    def pop(self):
        if self.isEmpty():
            raise IsEmptyError("Stack empty")
        result = self.head.value
        self.head=self.head.next
        self.size-=1
        return result

    def top(self):
        if self.isEmpty():
            raise("Error Not Foudn Error")
        return self.head.value
    
