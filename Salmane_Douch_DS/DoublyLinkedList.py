class Node:
    def __init__(self, id, name,gpa,major):
        self.id=id
        self.name=name
        self.gpa=gpa
        self.major=major
        self.next=None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return(self.size)
    def add__at__the__beginning(self, student_id, name, gpa, major):
        new_node=Node(student_id,name,gpa, major)
        if(self.head is None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node

        self.size+=1

    def append_node(self, student_id, name, gpa, major):
        newNode=Node(student_id, name, gpa, major)

        #empty LL
        if(self.head==None):
            self.head=newNode
            self.tail=newNode
        #LL not empty
        else:
            self.tail.next=newNode
            newNode.previous=self.tail
            self.tail=newNode
        self.size+=1
    def pop_last_element(self):
        if(self.head == None):
            raise ValueError("LL empty")
        elif(self.head==self.tail):
            toDelete=self.head
            self.head=None
            self.tail=None
        else:
            toDelete=self.tail
            self.tail = self.tail.previous
            self.tail.next=None
        self.size -=1
        return toDelete
    def update_major(self, student_id, newMajor):
        walker=self.head
        while(walker.next != None):
            if(walker.id==student_id):
                walker.major=newMajor
                return
            walker=walker.next
        print("Student with id: "+str(student_id)+" not found")
    def traverse(self):
        if(self.head==None):
            print("Empty LL")
        else:
            walker=self.head
            while(walker != None):
                print(f"ID is: {walker.id}, Name is: {walker.name}, GPA is: {walker.gpa}, and its major is: {walker.major}")
                walker=walker.next
'''
to implement:
- sort
- create ll from file
- fill ll from file
'''



#instantiation
new_ll=LinkedList()
new_ll.add__at__the__beginning(78555, "ahmed",3.75, "CS")
new_ll.append_node(58555, "Sara", 3.66, "GE")
new_ll.traverse()
new_ll.pop_last_element()
new_ll.traverse()