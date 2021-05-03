import numpy as np
from collections import Counter

# distance formula in 2d
def distform(a, b):
    return np.sqrt(np.sum(a-b)**2)


class KNN:
    def __init__(self,k=4):
        #store the k val
        self.k = k
    #follow the scikit library convention.... fit method will fit the training samples
    def fit(self, X, y):
        #storing the vals
        self.X_train = X
        self.y_train = y

    #predict new samples
    def predict(self, testSamps):
        #write a helper method which is a list
        predictedLabs  = [self.__predict(x) for x in testSamps]
        #converting it into a numpy arr
        return np.array(predictedLabs)

    #helper method which takes one sample
    def __predict(self, newsamp):
    
    #predict the distances and find the nearest neighbor and their labels and I do a majority vote
    #and choose the most common class label
    #1. compute dists
        dist = [distform(newsamp,X_train) for X_train in self.X_train]
    
    #2. get the knn and labels
        k_indeces = np.argsort(dist)[:self.k]
        k_nearest_label = [self.y_train[elem] for elem in k_indeces]

    #3. perform a majority vote 
        most_comm = Counter(k_nearest_label).most_common(1)
        return most_comm[0][0]


