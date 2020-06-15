import random

money= 100

guess = ["Heads", "Tails"]
guess1=random.choice(guess)
bet = random.randint(1,1000)
#Coin Flip
def flip_a_coin(guess1, bet):
    if bet <= 0:
        print("Place a minimum bet of 1. ")
        return 0

print("Let's flip a coin!\n You guessed "+guess1)
result = random.randint(1,2)

if result ==1:
    print("Heads")

elif result ==2:
        print("Tails")
    
if(guess1 == "Heads" and result ==1) or (guess1 == "Tails" and result ==2):
        print("You won " + str(bet) + " pounds.")
        money+=bet
    

else:
        print("You lost " + str(bet) + " pounds!!!")
        money-=bet
    
