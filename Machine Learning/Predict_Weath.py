import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib
import csv

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data= pd.read_csv(dataset_url, sep=';')
print(data.head())
print(data.describe())

#split the data
X= data.drop('quality', axis=1)
y=data.quality()

#Use the train_test_split function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

#standardization
X_train_scaled = preprocessing.scale(X_train)

print(X_trained_scaled)

print(X_train_scaled.mean(axis=0))
print(X_train_scaled.std(axis=0))

scaler= preprocessing.StandardScaler().fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_train_scaled = scaler.transfor(X_test)
print(X_train_scaled.mean(axis=0))
print(X_train_scaled.std(axis=0))


#pipeline with process and model
pipeline = make_pipeline(preprocessing.StandardScaler(),RandomForestRegressor(n_estimators=100))

print(pipeline.get_params())
