my_List = [2, 3, 5, 6, 5, 6]
 
mapEx = map(lambda i: (i * 3)+2, my_List)
 
print(list(mapEx))
# [8, 11, 17, 20, 17, 20]
 
secList = [34, 54, 7, 2, 9, 23, 89, 43, 78]

filterMe = filter(lambda i: i > 10, secList)
 
print(list(filterMe))
# [34, 54, 23, 89, 43, 78]
