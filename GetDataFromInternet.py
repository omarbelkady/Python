from urllib import request

n = request.urlopen("https://www.google.com")

#To get the HTTP Status code
print(n.getcode())

#To read data
print(n.read())
