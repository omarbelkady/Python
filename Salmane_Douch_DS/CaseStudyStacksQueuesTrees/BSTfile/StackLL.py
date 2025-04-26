class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class StackLL:
    def __init__(self):
        self.top = None
    def push(self,toPush):
        new_node=Node(toPush)
        new_node.next=self.top
        self.top=new_node
    def isEmpty(self):
        return self.top == None
    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return None
        toRemove=self.top
        self.top=self.top.next
        return toRemove
    def peek(self):
        if self.isEmpty():
            print("Empty Stack")
            return None
        else:
            return self.top.data

