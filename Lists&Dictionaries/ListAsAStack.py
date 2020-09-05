'''
A List is a type of DS(way of storing data). 
A Stack is another type of DS.
Stack structure in Python LIFO
'''
# Creating an empty dicctionary
my_stack= {}
my_stack['Angela']='2665 56837'
my_stack['63526']= '2-56837'

fav_pl_of_63526 = []

#REMEMBER FILO= STACK DS
print("Enter elements to push to the list and 'remove' to remove the last element and enter 'quit' to quit")
while True:
    my_data = input()
    if(str.lower(my_data) == "quit"):
        break
    elif(str.lower(my_data) == "remove"):
        fav_pl_of_63526.pop()
        print("Removing the element:", my_data)
    else:
        fav_pl_of_63526.append(my_data)
    print(fav_pl_of_63526)

for items in fav_pl_of_63526:
    print("The items within here are: ",items)
