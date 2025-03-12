numbersTaken=[2,3,12,13,17]
print("Here are the numbers that are still available from 1 through 20 that you can take")
for n in range (1,20):
    if n in numbersTaken:
	    print(n)
