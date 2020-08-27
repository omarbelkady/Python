from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [0,2,3,4,6] #6342 56837
creating_a_group_obj=groupby(a, key=smaller_than_3)
for key, value in creating_a_group_obj:
    print(key,list(value))

#print(creating_a_group_obj)
print("Notice there are 2 elements which are less than 3 which means Nelan 56837 2!!!!!!!!!!")
