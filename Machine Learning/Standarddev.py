import numpy as np
#standard deviation tells us how far is every user from the average
#A low standard deviation means the numbers in the set are close apart
#A high standard deviation means the numbers in the set are spread out
smart_class=[100,91,92,100,100,98,99,101,93,97,99,100,108,110,110,102,99,88,92,93,94,93,93,97,99]
horrible_prof=[99,93,93,71,88,71,70,58,53,53,0,0,16,25,33,58,66,88,31]

s=np.std(smart_class)
h=np.std(horrible_prof)
print("The standard deviation of the smart class is: "+ str(s))
print("The standard deviation of the dumb class is: "+ str(h))
