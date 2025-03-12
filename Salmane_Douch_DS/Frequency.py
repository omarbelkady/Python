def frequency(mylist: list)->dict:
    count={}
    for elem in mylist:
        count[elem]=count.get(elem, 0)+1
    return count


print(frequency([9,11,25,11,25,11,54,54,54,54]))