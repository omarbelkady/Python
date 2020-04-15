from operator import itemgetter
users=[
    {'firstName':'Richard', 'lastName': 'Dorris'},
    {'firstName':'Michael', 'lastName':'Carlos'},
    {'firstName':'Richelle', 'lastName':'Smith'},
    {'firstName':'Angela', 'lastName':'Jones'},
    {'firstName':'Patrick', 'lastName':'Johnson'},
    {'firstName':'Michelle', 'lastName':'Popescu'},
    {'firstName':'Georgina', 'lastName':'Hughes'},
    {'firstName':'Harvey', 'lastName':'Barker'},
    {'firstName':'Tristan', 'lastName':'Daniels'},
    {'firstName':'Cristina', 'lastName':'Chavez'},
    {'firstName':'Hugo', 'lastName':'Chavez'},
    {'firstName':'Albert', 'lastName':'Chavez'}
    ]

print('--------')
#sort the users by lastName and if there are 2 sort by their first Name
for x in sorted(users,key=itemgetter('lastName', 'firstName')):
  print(x)
