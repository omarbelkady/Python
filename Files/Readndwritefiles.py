##syntax to open file varName=open("Filename.txt",mode:'r' for read or 'w' for write)
##syntax to open varName=open("fileName.txt","mode")
fw=open("nameofthefile.txt", 'w')
fw.write("Writing some stuff in the text file\n")
fw.write("I like sushi\n")
fw.close()

fr=open("nameofthefile.txt", "r")
text=fr.read()#this will store all the data from the file in the text variable
print("bla blaldlafjal")
print("kjafjkalfds")
fr.close()
