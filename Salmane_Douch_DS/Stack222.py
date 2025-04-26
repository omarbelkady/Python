class Node:
    def __init__(self,name, id):
        self.name=name
        self.id=id
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
    def __isempty__(self):
        return False
    def push(self,new_node):
        node=Node(new_node)
        if node is None:
            print("Stack Overflow")
            return
        node.next=self.head
        self.head=node
    def pop(self):
        if self.__isempty__():
            return
        else:
            temp=self.head
            self.head=self.head.next
            del temp
    def peek(self):
        if not self.__isempty__():
            return self.head.data
        else:
            print("Empty")
            return float('-inf')