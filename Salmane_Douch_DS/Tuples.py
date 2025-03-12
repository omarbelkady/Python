x=(14745, "Hanaa Talei", 2007)
print(type(x))
print(x[1])
#x[1]+=" "
print(x)
#error


# how can it be done
y=x
y=list(y)
y[1]+=" "
y=tuple(y)
x=y
#now x is modified
print(x)