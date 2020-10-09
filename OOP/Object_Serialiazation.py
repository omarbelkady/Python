#to serialize an object we must import a libary called pickle
import pickle

class Nelan(object):
	name=" "
	age= 0
    
	def __init__(self, name="notknown"):
		self.name=name
        
	def hello(self):
		print("\nHello There Everyone my name is %s" %self.name)

#how to store to disk and pull it up later aka object serialization
#We create a file and it gets serialized to the disk


#Let's see if the object works fine
neha=Nelan()
neha.name="Alan"
neha.age=24
neha.hello()

#Write to a file
wrtofile=r"/home/test.txt"

with open(wrtofile, "bw") as d:
	pickle.dump(neha,d)

print("The plane has landed at Nelan Island")

#Now I read that file back in and load it
with open(wrtofile,"br") as d:
	m=pickle.load(d)
	print(m)
    
	#isinstance takes object as 1st param and className
	if isinstance(m,Nelan):
		print(m.name)
