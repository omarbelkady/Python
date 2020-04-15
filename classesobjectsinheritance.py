class Mario:
	def move(self):
		print("I am moving")
class Jumboshrimp:
	def eat_jumboshrimp(self):
		print("Now I am big")
class BigMario(Mario, Jumboshrimp):
	pass#this handles the syntax error and makes your class still function
bm=BigMario()
bm.move()
bm.eat_jumboshrimp()
