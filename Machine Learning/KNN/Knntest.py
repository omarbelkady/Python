import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from Knn import KNN
colormp = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])


iris = datasets.load_iris()
X,y = iris.data, iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

'''
print(X_train.shape)

#result is:(120, 4) where 120 is the number of samples and 4 is the number of features per sample

print(X_train[0])

print(y_train.shape)
print(y_train)

plt.figure()

plt.scatter(X[:,0], X[:,1], c=y, cmap=colormp, edgecolor="k", s=20)
plt.show()

alpha = [1,1,1,2,2,3,4,5,6]


from collections import Counter

#print only one most common item
most_common = Counter(alpha).most_common(1)
print(most_common) 
'''


myclassifier = KNN(k=3)
myclassifier.fit(X_train, y_train)

#predicting my test samples
predict = myclassifier.predict(X_test)

#predicting the accuracy of my model aka how many predictions I made are correctly classified
how_accurate = np.sum(predict== y_test) / len(y_test) 

print(how_accurate)