#RT-WC: O(n^2)
#RT-BC: O(n)
#Class: Comp Sort




def func(arr):
    s=len(arr)
    for x in range(s):
        for y in range(s-x-1):
            if(arr[y] > arr[y+1]):
                tempvar=arr[y]
                arr[y]=arr[y+1]
                arr[y+1]=tempvar

arraySort=[192,31,4,24,42,5,25,32,59,92]
func(arraySort)
print("Here is the sorted List: ",arraySort)
