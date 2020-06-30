from struct import *
strfile=r'/home/test.txt'
strformat='iid'

packed=pack(strformat,1,6,3.14159)
print(packed)
print("writing to file")
with open(strfile, "bw") as f:
    f.write(bytes(packed))

print("Reading from the file")

with open(strfile, "bw") as f:
    buffer=f.read()
    unpacked=unpack(strformat.buffer)
    print(unpacked)
