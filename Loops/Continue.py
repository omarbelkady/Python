//The Continue statement serves to tell the iterator to stop looping if you have found a particular item
//we are looking for and resume iterating,do not take me nor output me.
goodPeople=["Alan", "Waleed", "Angela", "LauraTheMongue"]
for z in goodPeople:
	if z == "LauraTheMongue":
		continue
	print(z)
