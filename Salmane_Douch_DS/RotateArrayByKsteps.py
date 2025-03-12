def rotate_ary(numbers, k):
    k %=len(numbers)
    return numbers[-k:]+numbers[:-k]
print(rotate_ary([1,2,3,4,5,6,7],4))
