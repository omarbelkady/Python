#divisors add up to the number not including itself
def perfectNumber(num):
    if(num<2):
        return False
    else:
        divisors_sum=1
        for i in range(2, int(num**0.5)+1):
            if(num%i==0):
                divisors_sum=divisors_sum+i
                if(i != num//i):
                    divisors_sum = (divisors_sum+(num//i))
    return divisors_sum == num
print(perfectNumber(6))#123             1+2+3=6
print(perfectNumber(28)) #1 2 4 7 14    1+2+4+7+14=28    sum of divisors excluding itself is the number
print(perfectNumber(12)) #1 2 3 4 6   1+2+3+4+6=16

