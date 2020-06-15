a=50 #1 1 0 0 1 0----2+16+32=50
b=25#0 1 1 0 0 1----1+8+16=25
c=a&b#comparison of a & b when the same 1 and when you have 2 zeros then zero:010000
print(c) 

#-------BINARY LEFT SHIFT-----
x=240   #11110000
y=x << 2 #1111000000
print(y)

#------BINARY RIGHT SHIFT-----
d=x >> 2 #111100 32+16+8+4=60
print(d)
