myList=[13,36,29,33,22,200,255]

myStringFile=r"/home/test.txt" 

#I create a buffer and I use the bytes function which will take the list of numbers and turn them into a list
#of bytes
buffer= bytes(myList)
print(buffer)

#Now I will take the output and write it to a file. bw stands for binary write mode
with open(myStringFile,'bw') as l:
    #I write the buffer to the disk
    l.write(buffer)

#Now I will read the file back
print("File has been written, I will read it back!")

#now I will open it as binary read
with open(myStringFile,'br') as l:
    #read a maximum of 16 bytes
    buffer=l.read(16)
    print("length of Buffer: %d" %len(buffer))
    
    for jhat in buffer:
        print(int(jhat))

#the benefit of using a binary file is that we can store a lot of info
#in contrast, to a text file(which is not possible)
