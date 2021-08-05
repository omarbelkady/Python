## Regression in ML

- Types of Regressions in ML
    - Huber
    - Quantile
    - Log Cosh
    - Mean Absolute Error/ L1
    - Mean Squared Error/ L2
    - Mean Squared Logarithm Error/ L2


#### Logistic Regression in Python

- A logistic regression function is a sigmoid function essentially
- and my I plug in the ordinary linear equation for x i.e. y=mx+b
- The output is a probability of something happening
- 1/(1+e^(-wx+b)) where w is my weight and b is my bais
- w and b are called my parameters
- Prior to knowing w and b I must have a cost function
- I must calculate my derivative and learning rate


### Implementation

```python
import numpy as np

class LogisticReg():
    def __init__(self, lear_rate=0.001, num_of_iters=1000):
        #storing the args
        self.lear_rate = lear_rate
        self.num_of_iters = num_of_iters
        #creating the weights
        self.weights = None
        self.bias = None
    
    '''
    fit method that takes a training sample
    and training labels
    '''
    def fit(self, X, y):
        '''
        X is a numpy I and d vector of size m by n
        where m is the number of samples
        and n is the number of features for each 
        sample
        1. I must initialize the weights i.e. the parameters
        '''
        num_ofsamps, num_offeatures = X.shape
        self.weights = np.zeros(num_offeatures)
        self.bias = 0

        # gradient descent to iteratively update my weights
        for el in range(self.num_of_iters):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predic = self._sigmoidfunc(linear_model)

            #must take the derivative of the weight
            dw = ( 1 / num_ofsamps ) * np.dot(X.T, (y_predic-y))

            db = ( 1 / num_ofsamps ) * np.sum(y_predic - y)

            # must update my parameters
            
            self.weights -= self.lear_rate * dw 

            self.bias -= self.lear_rate * db

    
    '''
    predict method
    ```

    #if >0.5 then +1..... if <0.5 then +0
    def predict(self, X):
        #approximate my data with a linear model
        linear_model = np.dot(X, self.weights) + self.bias
        y_predic = self._sigmoidfunc(linear_model)
        y_predic_class = [1 if i > 0.5 else 0 for i in y_predic]
        #return the predicted class
        return y_predic_class 



    
    #private method
    def _sigmoidfunc(self, x):
        return 1 / (1 + np.exp(-x))
    
```