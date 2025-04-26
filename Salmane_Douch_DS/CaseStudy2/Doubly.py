class Node:
    def __init__(self,isbn,title,author,year,copies):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.year=year
        self.copies=copies
        self.next=None
        self.prev=None
class Doubly:
    self.tail=None
    self.head=None

    def append(self,isbn,title,author,year,copies):
        new_node=Node(isbn,title,author,year,copies)
        if self.head ==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
    def insert_inorder(self,isbn,title,author,year,copies):
        new_node=Node(isbn,title,author,year,copies)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        if year == self.head.year:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
        elif year >self.tail.year:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        else:
            walker=self.head
            while(walker.year != None):
                walker=walker.next
            new_node.next=walker
            new_node.previous=walker.previous
            walker.previous.next=new_node
            walker.previous=new_node


    def __str__(self):

file = open("books_data.csv", "r")
L1=Doubly()
for line in file:
    list_line = line.strip().split(",")
    print(list_line)
def Load_data_from_file():
    path="books_data.csv"
    file=open(path,"r")
    for line in file:
        list_line=line.strip.split(",")#based on the delimtter
        l1.insert_inorder(list_line[0],list_line[1],list_line[2],list_line[3],list_line[4])
    file.close()
def __str__(self):
    print_str=""
    current=self.head
    while(current != None):
        print_str+=
def write_file_order():
    new_file=open("ordered.txt","w")
    walker=L1.head
    for j in range(L1.size):
        new_file.write(walker.title+", "+walker.year+"\n")
        walker=walker.next
    new_file.close()
write_file_order()