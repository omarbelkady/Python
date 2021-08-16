## Terminology and Techniques


![ML CHEATSHEET](https://user-images.githubusercontent.com/31806568/119829824-91f4c500-bef3-11eb-8518-05fe93e5a155.jpg)

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
|Boosting |N/A |Unsupervised
|Decision Tree| Classification/Regression |Supervised
|Ensemble Methods| Regression |Supervised
|Gaussian Mixtures |N/A |Unsupervised
|Gaussian Progresses Regression|Regression|Supervised
|Hierarchical Clustering | Clustering | Unsupervised
|Linear Reg|Regression|Supervised
|Logistic Reg|Classification|Supervised
|K-Means| Clustering |Unsupervised
|KNN| Classification|Supervised
|Naive-Bayes| Classification|Supervised
|Random Forest| Classification/Regression |Supervised
|Spectral Clustering|Clustering|Unsupervised
|Support Vector Regression|Regression|Supervised
|SVM| Classification/Regression|Supervised


### Types of Algo in Clustering:
- K Means Clustering
- Hierarchial Clustering
- DBSCAN Clustering
- Expectation Maximization Clustering

### Optimization in ML

- Find the ideal model weights which reduces the loss between predicted and actual value
- whilst remembering to obtain the best fit of a certain dataset to the model  

### Naive Bayes Algorithm

- Based on the Bayes Theorem
- It gathers information to determine the probability of an event to take place based on knowledge
- ... it has from the past which are related to the event
- It is naive because the way it makes up its decision may or may not be accurate 
- P(y|X)....(P of y given x) is called the posterior probability
- P(x_i|Y)....(P of x given y) is called the class conditional probability
- P(y)...(P of y) is called the prior probability of y
- P(x)...(P of x) is called the prior probability of x

    - Objective: Choose class with the highest probability because we are doing classification


### Class Conditional Property in NaiveBayes
```python
import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        '''
            train data = X
            training label = Y
            number_of_rows: num_of_samples
            number_of_columns: num_of_features 
        '''
        num_of_samples, num_of_features = X.shape
        #to find the unique elements within the list i.e. array

        self._classes = np.unique(y)
        num_of_classes = len(self._classes)

        ''' 
        initializing the mean, variance and priors
        for each class... we need a mean for each feature
        '''

        
        self._mean = np.zeros((num_of_classes, num_of_features), dtype=np.float64)
        self._variance = np.zeros((num_of_classes, num_of_features), dtype=np.float64)
        self._priors = np.zeros(num_of_classes, dtype=np.float64)

        for eachclass in self._classes:
            #only want the samples 
            X_c = X[eachclass == y]
            '''
            calculate the mean for each class
            I want to fill the row  and all columns
            '''
            self._mean[eachclass,:] = X_c.mean(axis=0)
            self._variance[eachclass,:] = X_c.var(axis=0)
            #divide by the number of sample
            self._priors[eachclass] = X_c.shape[0] / float(num_of_samples) 


    def predict(self, X):
        predic_y = [self._predictmeth(eachsample) for eachsample in X]
        return predic_y

    #takes in one sample
    def _predict(self, x):
        '''
        1. calculate the posterior probability
        2. calculate the class conditional
        and the prior for each(class cond)
        3. Select the class with the highest probability
        '''
        the_posteriors = []
        # go over each class 
        for idxc, c in enumerate(self._classes):
            the_prior = self._priors(idxc)
            clss_cond = np.sum(np.log(self._prob_dens_func(idxc,x)))
            posterior = the_prior + clss_cond 
            the_posteriors.append(posterior)
            #I choose the class with the highest probability thanks to argsmax
        #index is now: the posteriors with the highest probability 
        return self._classes[np.argmax(the_posteriors)]
    
    # pdf function
    def _prob_dens_func(self, clss_idx, x):
        #i need the mean and the variance
        the_mean = self._mean[clss_idx]
        the_variance = self._variance[clss_idx]
        numerator = np.exp(-(x-the_mean)**2/(2*the_variance))
        denominator = np.sqrt(2*np.pi*the_variance)
        return numerator / denominator
```



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

