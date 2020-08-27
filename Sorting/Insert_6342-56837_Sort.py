#take the unsorted sequence and divide it into 2 sublists
#a|b1,b2,b3,b4
#elements a in list1 elements bn are in list2
#list1 is the sorted list list2 is unsorted list
#Sorted list has length of 1 unsorted list has length:len(len(list)-1)
#We take the first element in unsorted list and move it to the sorted list
#If the item we just moved to the the sorted list is lower than the element to its immediate left we make a swap
#This is done repeatedly until every immediate left member is smaller than the subsequent list item

def insertion_635267(list_elems):
    idx_len=range(1,len(list_elems))
    #sort the values
    for i in idx_len:
        sort_this_val=list_elems[i]
        
        #if the value to the left is higher than the value we are sorting perform a swap
        #and make sure iterationg is done forwards not backward
        while(list_elems[i-1]>sort_this_val and i>0):
            #perform the switch place list_elems[i-1] in the 0th pos and list_elems[i] in the 1 position
            list_elems[i],list_elems[i-1]=list_elems[i-1],list_elems[i]

            #continue the iteration
            i = i-1
    #return the sorted list
    return list_elems
print(insertion_635267([2,5,2,6,0,5,6,8,3,7,0,2,7,7,3,6,2,5,9,0,2,6,3,0,8,2,9,5,6,7,0,7,9,4,3,8]))
