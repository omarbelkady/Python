from itertools import permutations
#Returns all possible orderings of an input
a= [1,2,3]
permut_63526=permutations(a)
print(list(permut_63526))

print("Now 968 6342 I will shorten the permutation I will make it length 2")
b= [6,5,6,8,3,7]
permut_B=permutations(b,2)
print(list(permut_B))

