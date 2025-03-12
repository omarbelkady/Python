def numberOfDigits(num):
    num = abs(num)
    count = 0
    if(num==0):
        return 1
    else:
        while(num>0):
            num = num//10
            count = count + 1
    return count
