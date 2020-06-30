from struct import *
#Store as bytes data

#packing function format:packed_data=pack(format,listofvalues)
packed_data=pack('iif',6,19,4.73) #iif=2 integers and 1 float
print(packed_data)
print(calcsize('i'))#memory required to store an integer
print(calcsize('f))#memory required to store a float
print(calcsize('iif')) #memory required to store 2 integers and a float prints out 12 since i=4bytes and f=4bytes
#packed data is computer readable code
#unpack is human readable code
#original_info=unpack('format', filename)
original_info=unpack('iif',packed_data)
print(original_info)
