from time import sleep
#from library import a function   from a library give me a book of functionalities

start = int(input("Please enter a number to start counting from:"))

#for counter in range(start, stop, step)
# start at the number stop at negative 1 and step down 1 number every time  [start,stop)  [-7, 6
for counter in range(start, -1, -1):
    print(counter)
    sleep(2) #run every second

list1=["Salma","Nidal","Aya","Imane","Omar"]
list2=["Salma", "Houda","Nisrine","Nisrine","Bouchra","Yousra","Aya", "Aya","Aya","Nisrine","Nisrine","Nisrine","Nisrine","Nisrine","Nisrine"]

for element in set(list2):
    print(element)


for x in list1:
    print(x)

while(x != 3):
    input(str("Name"))
    x = int(input("Number: "))

y=int(input("Please Enter a number"))
if(y != 6):
    print("Not 6")
else:
    print("Found")