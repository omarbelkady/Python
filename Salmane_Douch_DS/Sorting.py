def bubble_sort(L):
    n=len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            if(L[j]>L[j+1]):
                L[j],L[j+1]=L[j+1],L[j]

L=[64,12,4,5,6,15]

bubble_sort(L)
for i in range(len(L)):
    print(L[i])

def selection_sort(L):
    n=len(L)
    for i in range(n-1):
        min_index = i
        for j in range(n):
            if(L[j]<L[min_index]):
                min_index=j
    if(min_index!=i):
        L[i],L[min_index]=L[min_index],L[i]
    return L

selection_sort(L)
for i in range(len(L)):
    print(L[i])
