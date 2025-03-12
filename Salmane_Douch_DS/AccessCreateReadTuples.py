'''
1. create the tuple
2. print the first element
3. print the last element
4. print the length of the tuple
'''

#1
mytuple=(1,2,3,4,5)
for i in mytuple:
    print(i)
print(mytuple[0])
print(mytuple[-1])
print(len(mytuple))
mytuple=("apple","banana","oranges","lemon","cherry")
print("Tuple slicing")
v,w,x,y,z=mytuple
print("The element in the tuple \n1:",v,"\n2:",w,"\n3.",x,"\n4.",y,"\n5.",z)
print("Slicing the tuple")
for i in range(0,4,2):
    print(mytuple[i])
def found_or_not_found(list,elem):
    found=False
    for i in list:
        if(i==elem):
            found=True
            break
    if(found):
        print(f"{elem} is in the list")
    else:
        print(f"{elem} is not in ")