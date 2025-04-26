class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stacklst:
    def __init__(self):
        self._L=[]
    def push(self,value):
        self._L.append(value)
    def pop(self):
        if not self._L:
            print("empty stack")
        return self._L.pop()
    def peek(self):
        if not self._L:
            print("Empty stack")
            return None
        else:
            return self._L[len(self._L)-1]
# queues ll
class QueuesLL:
    def __init__(self):
        self.front=None
        self.rear=None

    def append(self,value):
        new_node = Node(value)
        if(self.front is None):
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def __dequeue(self):
        if(self.front == None):
            return None
        else:
            todequeu=self.front
            self.front=self.front.next
            return todequeu.value

def printNumbers(n):
    if n == 0:
        return 0
    else:
        return printNumbers(n-1)
        print(n)

def sumOfNumbers(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n+sumOfNumbers(n-1))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


    def addNode(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.addNode(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.addNode(data)
        else:
            self.data=data
    # Insert a node
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, current, value):
        if current is None:
            return Node(value)
        if value < current.value:
            current.left = self._insert(current.left, value)
        elif value > current.value:
            current.right = self._insert(current.right, value)
        return current

    # Search for a value
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    # Inorder traversal
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current.value, end=" ")
            self._inorder(current.right)

    # Preorder traversal
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, current):
        if current:
            print(current.value, end=" ")
            self._preorder(current.left)
            self._preorder(current.right)

    # Postorder traversal
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, current):
        if current:
            self._postorder(current.left)
            self._postorder(current.right)
            print(current.value, end=" ")

    # Find minimum value
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, current):
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.value

    # Find maximum value
    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, current):
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.value

    # Delete a node
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, current, value):
        if current is None:
            return None
        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            # Case 1: No child
            if current.left is None and current.right is None:
                return None
            # Case 2: One child
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Case 3: Two children
            else:
                min_val = self._find_min(current.right)
                current.value = min_val
                current.right = self._delete(current.right, min_val)
        return current
