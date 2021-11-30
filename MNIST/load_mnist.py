from keras.datasets import mnist 
from keras import models
from keras import layers

# Load training and test data

(train_img, train_labels), (test_img, test_labels) = mnist.load_data()
print("Information about train data:")
print(train_img.shape)
print(len(train_labels))
print("Information about test data:")
print(test_img.shape)
print(len(test_labels))

