class Enemy:
    life= 3
    def attack(self):
      print("Ouch")
      self.life-=1
		
    def checkLife(self):
	    if self.life <= 0:
		    print("I am dead")
	    else:
	    	print(str(self.life)+ "life/lives left")
#Must create an object to access the class first to use the attack function
enemy1= Enemy()
enemy2=Enemy()


enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
