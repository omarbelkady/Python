import os
import sys

def swearwords():
	userinput = str(input("Navigate to the .txt file you would like to censor(remove swear words)"))
	swearwordslist = ["fuck", "shit", "piss"]
	with open("{}".format(userinput), 'r+') as f:
		text = f.readlines()
		if swearwordslist in text:
			for swears in swearwordslist:
				text.replace('{}'.format(swears), '****')
				print("{}".format(len(swears)) + "swear words removed from {}".format(userinput))
		else:
			print("Did not find any swear words in the .txt file at {} you provided...".format(userinput))
swearwords()
