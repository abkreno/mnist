import pandas as pd
import sklearn
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import numpy as np

from pylab import *
from numpy import *
from load_mnist import load_mnist


images_train, labels_train = load_mnist('training', path='data/')
images_test, labels_test = load_mnist('testing', path='data/')
# imshow(images_train.mean(axis=0), cmap=cm.gray)
# show()
labels_train = pd.DataFrame(data=labels_train)
images_train = pd.DataFrame(data=images_train)
labels_test = pd.DataFrame(data=labels_test)
images_test = pd.DataFrame(data=images_test)

print(images_test.shape)
#print(labels_train.value_counts())
