path= "bst_file.txt"
file = open("bst_file.csv","r")
for line in file:
    print(line.strip().split(","))

class Node:
    def __init__(self, key,value):
        self.key=key
        self.id=id
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,key,value):
        if key <= root.key
            if root.left is None:
                root.left = Node(key,value)
            else:
                self.insert(root.left, key,value)
        else:
            if root.right is None:
                root.right = Node(key, value)
            else:
                self.insert(root.right, key, value)
    def apppend(self,key,value):
        if self.root is None:
            self.root=Node(key,value)
        else:
            self.insert(self.root,key,value)
    def search(self,key):
        if self.root is None:
            return("Not found")
        else:
            if(self.root.key < key):
                self.root =



bst1 = BST()
for line in file:
    print(line.strip().split(""))
    key, name, price = line.strip().split(",")
    key=int(key)
    value =(name,float(price))


