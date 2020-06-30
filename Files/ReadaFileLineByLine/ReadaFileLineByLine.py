import os

path=r"/home/name.txt"



#Read the whole file for me Way#1
if os.path.exists(path):
    #Binary vs Text: binary has bunch computer readable code vs text is human readable code
    with open(path) as u: #with object returning sth and we call u 
        print(u.read())


print("REaddiiinnnggg The lines ONE AT A TIME!")

#Read the whole file for me Way#2
if os.path.exists(path):
    #Binary vs Text: binary has bunch computer readable code vs text is human readable code
    with open(path) as myLines: #with object returning sth and we call u 
        for line in myLines.readlines():
            print(line.strip('\n'))
