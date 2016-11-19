import pandas as pd
import sklearn
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from bounding_box import bounding_box_preprocess
import numpy as np

from pylab import *
from numpy import *
from load_mnist import load_mnist
from plotting import plot_learning_curve

trainLimit = 20000#20000
testLimit  = 5000#5000

images_train, labels_train = load_mnist('training', path='data/',reshape_2d=True)
images_test, labels_test = load_mnist('testing', path='data/',reshape_2d=True)
images_train = bounding_box_preprocess(dataset=images_train[:trainLimit])
images_test  = bounding_box_preprocess(dataset=images_test[:testLimit])
images_train = images_train.ravel()
images_test = images_test.ravel()
print("DONE PREPROCESSING")
#PREPROCESSING THE TRAINING AND THE TEST TO USING BOUNDING BOX TECHNIQUE
labels_train = pd.DataFrame(data=labels_train[:trainLimit])
images_train = pd.DataFrame(data=images_train[:trainLimit])
labels_test = pd.DataFrame(data=labels_test[:testLimit])
images_test = pd.DataFrame(data=images_test[:testLimit])

X_train = images_train
y_train = labels_train.values.ravel()
X_test  = images_test
y_test = labels_test.values.ravel()

mlp = MLPRegressor(hidden_layer_sizes = (300,300,), activation='relu' , random_state=0, early_stopping=False)
mlp.fit(X_train, y_train) #Trains the classifier
print(mlp.score(X_test, y_test)) #Gives accuracy score on test set

y_predicted = np.array(mlp.predict(X_test), float16)

print(classification_report(y_test, y_predicted))
