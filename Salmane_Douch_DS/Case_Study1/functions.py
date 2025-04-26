from Salmane_Douch_DS.SingleLinkedList import new_ll


class Node:
    def __init__(self,vehicle,make,model,year,price,mileage):
        self.vehicle=vehicle
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.mileage=mileage
        self.next=None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __setitem__(self, key, value): #help
        self.key=value
    def append(self,vehicle_id, make, model,year, price,mileage):
        new_node=Node(vehicle_id,make,model,year,price,mileage)
        if self.head is None:
            self.head=new_node
        else:
            walker=self.head
            while(walker.next != None):
                walker=walker.next
            walker.next=new_node
    def sort(self):
        if self.head is None:
            return

        swapped=True
        while(swapped):
            swapped=False
            walker=self.head
            while(walker.next != None):
                next_node=walker.next
                if((walker.year>next_node.year) or
                        (walker.year>next_node.year and walker.price>next_node.price)):
                    (walker.vehicle,walker.make,walker.model,walker.year,walker.price,
                     walker.mileage)=(next_node.vehicle, next_node.make,next_node.model,next_node.year,
                                      next_node.price,next_node.mileage)
                swapped=True
            walker=walker.next
    def display(self):
        walker=self.head
        if(walker==None):
            return
        print(f"{'ID':<5} {'Make':<15} {'Model':<15} {'Year':<5} {'Price':<10} {'Mileage':<10}")
        print("-" * 65)
        while(walker):
            print(f"{walker.vehicle}:<5 {walker.make:<15} {walker.model:<15} {walker.year:<5} {walker.price:<10} {walker.mileage:<10}")
            walker=walker.next

    def create_ll_from_file(filename):
        try:
            with open(filename, "r") as file1:
                lines=file1.readlines()
            new_ll=LL()
            for line in lines:
                data_in_ll=line.strip().split(",")
                vehicle_id,make,model,year,price,mileage=(
                    int(data_in_ll[0]),data_in_ll[1],data_in_ll[2],data_in_ll[3],data_in_ll[4],data_in_ll[5]
                )
                new_ll.append(vehicle_id,make,model,year,price,mileage)

            new_ll.sort()
            return new_ll
        except FileNotFoundError:
            print(f"File '{filename}' not found ")
            return None
        except Exception as e:
            print(f"Error of {e}")
            return None
    def reverse(self):
        previous = None
        walker = self.head
        while walker:
            next_node = walker.next
            walker.next = previous
            previous = walker
            walker=walker.next
        self.head = previous
    def pop(self,idx):
        if(idx ==0):
            self.head.previous=None
            self.head=self.head.next
        elif idx==self.size-1
            self.tail=self.tail.previous
            self.tail.next=None
        else:
            walker = self.head
            for i in range(idx):
                walker = walker.next
            walker.prev.next=walker.next
            walker.next.previous=walker.previous
'''
len, 
append, 
insert, 
pop,   remove a given value using index
search, 
remove,   traverse loop
sort  
print
str
'''

