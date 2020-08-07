import numpy as np
activation = lambda x: 1.0/(1.0 + np.exp(-x)) #the sigmoid function
input = np.random.randn(3,1)
hidden_1 = activation(np.dot(W1,input) + b1)
hidden_2 = activation(np.dot(W2,hidden_1) + b2)
output = np.dot(W3, hidden_2) + b3
