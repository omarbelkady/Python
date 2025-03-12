def bubble_sort2(mylist):
    n=len(mylist)
    for i in range(n-1): # for(int i=0;i<n-1;i++)
        swapped=False
        for j in range(n-i-1):  #for(int j=0;j<n-i-1;j++)
            #[13,41,4,15]        ascending order
            if(mylist[j]<mylist[j+1]):
                temp = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
                swapped=True
        if not swapped:
            break
    return mylist

def bubble_sort(mylist):
    n=len(mylist)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            #[13,41,4,15]        descending order
            if(mylist[j]>mylist[j+1]):
                temp = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
                swapped=True
        if not swapped:
            break

def selection_sort(mylist):
    n=len(mylist)
    #for(int i=0;i<n-1;i++)
    for i in range(n-1):
        min_index=i
        #for(int j=i+1;j<n;j++)
        for j in range(i+1,n):
            if(mylist[j]<mylist[min_index]):
                min_index=j
        if(min_index != i):
            temp= mylist[i]
            mylist[i]=mylist[min_index]
            mylist[min_index]=temp
    return mylist



list1=[243,22,43,21,2,1]
list2=["bob","anne","richard","donald","matthew","jason","brandon"]

list3=["bob","anne","richard","donald","matthew","jason","Brandon"]
'''
capitals 90 - 120   in ascii so that's why 
 motivation either convert:
 - everything lower case
 - everything upper case

 
 or use 
 build a function that comparison
 1. convert them both to upper case or lower case
 2. call it in the bubble or selection sort function 

try:
5. merge sort
6. quick sort
7. heap sort: 
            1. create a heap
            2. then add the elements to the heap
            3. traverse 
 '''
print(selection_sort(list1))
print(selection_sort(list2))
print(selection_sort(list3))

