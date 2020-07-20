import numpy as np

o=np.array([1,2,3])
b=np.array([4,5,6])

#Dot Protect: scaler magnitude but no direction
print(np.dot(o,b))

#Cross Protect: vector meaning magnitude+direction
print(np.cross(o,b))


#matrix calculation row*colum
m=np.array([[3,4],[6,9]])
j=np.array([[2,5],[7,19]])


#calculating the determinant of a 2x2 matrix * 2x2 matrix
print(np.linalg.det(j))#(2*19)-(5*7)=38-35=3

mu=17
sigma=15
samples=10000

x=np.random.normal(mu,sigma,samples)
print(x)
