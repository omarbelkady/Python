class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class StackLL:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,value):
        new_node=Node(value)
        self.size+=1
        if(self.top==None):
            self.top=new_node
        else:
            new_node.next= self.top
            self.top=new_node
    def pop(self):
        if self.top is None:
            raise ValueError("STack is empty")
        else:
            return_value = self.top.value
            self.top=self.top.next
            self.size-=1
            return return_value
    def peek(self):
        if self.top==None:
            raise ValueError("Stack is Empty")
        else:
            return self.top.value


