#using the accumulate function in the Itertools lib
from itertools import accumulate
import operator
a = [2,5,2,6,5,6,8,3,7,2]
accum_add_var = accumulate(a, func=operator.add)
accum_mul_var = accumulate(a, func=operator.mul)
'''
def listToString968634256ver(s):
    str2 = " "
    for elem in s:
        str2 += elem

    return str2
'''

print("The list without the accumulator function: "+str(a))
print("The list with the multiplication accumulator function: "+str(list(accum_mul_var)))
print("The list with the addition accumulator function: "+str(list(accum_add_var)))
