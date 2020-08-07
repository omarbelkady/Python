import numpy as np
f = lambda x: 1.0/(1.0+np.exp(-x))
x = np.random.randn(3,1)
h1 = f(np.dot(W1, x)+b1)
h2 = f(np.dot(W2, h1)+b2)
out = np.dot(W3, h2) +b3
print(out)
