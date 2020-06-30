from struct import *
#import everything from the struct package 

myStringFile=r"/home/test.txt"
mySelectedFormatForStruct= 'iid'
#format iid: integer, integer, decimal


#with a structure we have 2 main ideas: packed and unpacked
#pack: packing it down to store it within a box
#unpack: take it out of the box and do something with it


#pack function(format, data1, data2, data3, etc.)
mypack=pack(mySelectedFormatForStruct,1,5,3.141592)
print(mypack)
