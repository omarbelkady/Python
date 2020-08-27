from itertools import combinations, combinations_with_replacement
#c++
n = [6,3,5,2,6]
#the first argument is the list/array name and the 2nd argument is length you want
combinat = combinations(n,2)
print(list(combinat))

'''
NOW IF WE WANT THE COMBINATIONS TO REPEAT LIKE 66
I IMPORT THE LIBRARY combinations_with_replacement
'''

a= [2,5,6,3,7]
combin = combinations(a,2)
print(list(combin))
print("Above is Combinations\n")
combinati_with_repl=combinations_with_replacement(a,2)
print(list(combinati_with_repl))
print("Above is Combinations With Replacement")
