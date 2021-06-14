## Terminology and Techniques




|Problem                          |Definition                         
|-------------------------------|-----------------------------|
|Regression            |find a relation between x(indep var) and y(dep var)            |
|Classification          |classify an observation to one of the known categories         |
|Clustering| group a set of objects into several known clusters|


### Steps to Building a Model
---
1. Retrieve The Data
2. Prepare the data and fix the issues such as any values missing and the outliers
3. Analyze your data and make a decision on which algorithm suits your needs
4. Train your model using the algo you just chose. Start simple by only using the most import variables
5. If your model does not meet your needs choose another algorithm or bring in different variables into your existing model

### Machine Learning Algorithm, Problem and its Learning Style
|Algorithm                          |Problem | Learning Style|                  
|-------------------------------|-----------------------------|------------|
|Decision Tree| Classification/Regression |Supervised
|Logistic Reg|Classification|Supervised
|K-Means| Clustering |Unsupervised
|KNN| Classification|Supervised
|Naive-Bayes| Classification|Supervised
|Random Forest| Classification/Regression |Supervised
|SVM| Classification/Regression|Supervised


### Types of Algo in Clustering:
- K Means Clustering
- Hierarchial Clustering
- DBSCAN Clustering
- Expectation Maximization Clustering

### Optimization in ML

- Find the ideal model weights which reduces the loss between predicted and actual value
- whilst remembering to obtain the best fit of a certain dataset to the model  


### Cross-Validation:
- Gives you the performance of your ML model depending on the new unseen data

### Loss Functions You Must Know in Each Category of ML

#### Classification

1. Log
2. Hinge
3. Exponential
4. Cross Entropy
5. Kullback Leibler Divergence

#### Regression

1. Huber
2. Quantile
3. Log Cosh
4. Mean Absolute Error/ L1
5. Mean Squared Error/ L2
6. Mean Squared Logarithm Error/ L2
