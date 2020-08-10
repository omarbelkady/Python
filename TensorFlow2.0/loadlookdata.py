import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

#loading the fasion mnist  dataset which is an alternative to mnist
data=keras.datasets.fashion_mnist

# split the data into training and testing pass in always 80-90% of the data to train
# Use the remainder 10-20% of the data left to testing because it hasn't been seen
# Testing data on the network which it had already seen will not give any errors
# Because the models will already have memorized
(train_images, train_labels), (test_images, test_labels) = data.load_data()

#Each image above will have its corresponding label
print(train_labels)

