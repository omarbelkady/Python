class Girl:
	gender= "female"#this is a class variable shared among each no matter what
	
	def __init__(self,name):
    self.name=name#instance variable unique to each girl and each object
r=Girl('Rachel')
s=Girl('Stankey')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
