from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

with open(input("Enter the name of Your File"), "r") as myFile:
    j = myFile.read()

filtered=pf.censor(j)
print(filtered)


