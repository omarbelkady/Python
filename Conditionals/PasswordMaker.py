#This program requires the user to enter a username and password
#The username has no restriction
#The password must have:
'''
    - 1 lowercase letter
    - 1 uppercase letter
    - 1 single-digit number
    - 1 char
    - Minimum Password Length Must Be: 7
    - Maximum Password Length Must Be: 14 ^:)^ Alan
    - Input 1: ABc23
    - Input 2: ENehaTS$
    - Input 3: Nelan<3CAND6342
    - Input 4: Nelan<3C
'''
import re
passArray[]
elems=[p for p in input().split(',')]
for j in elems:
    if len(j)<6 or len(j)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",j):
        continue
    elif not re.search("[0-9]",j):
        continue
    elif not re.search("[A-Z]",j):
        continue
    elif not re.search("[!@#$%^&*()_<>{}]",j)
        continue
    elif re.search("\s",j):
        continue
    else:
        pass
        passArray.append(j)
print(",".join(passArray))
