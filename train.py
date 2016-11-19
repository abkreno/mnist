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

import numpy as np

from pylab import *
from numpy import *
from load_mnist import load_mnist
from plotting import plot_learning_curve

trainLimit = 10#20000
testLimit  = 5000#5000

images_train, labels_train = load_mnist('training', path='data/')
images_test, labels_test = load_mnist('testing', path='data/')

labels_train = pd.DataFrame(data=labels_train[:trainLimit])
images_train = pd.DataFrame(data=images_train[:trainLimit])
labels_test = pd.DataFrame(data=labels_test[:testLimit])
images_test = pd.DataFrame(data=images_test[:testLimit])

X_train = images_train
y_train = labels_train.values.ravel()
X_test  = images_test
y_test = labels_test.values.ravel()

mlp = MLPClassifier(hidden_layer_sizes = (300,300,), activation='relu' , random_state=0, early_stopping=False)
# mlp.fit(X_train, y_train) #Trains the classifier
# print(mlp.score(X_test, y_test)) #Gives accuracy score on test set

# svc = OneVsRestClassifier(SVC(C=1, kernel='linear', random_state=0))
# svc.fit(X_train, y_train)
# print(svc.score(X_test, y_test))

# y_predicted = np.array(mlp.predict(X_test), float16)
# print(classification_report(y_test, y_predicted))

# PLOTTING
title = "Learning Curves for MLP (2 Layers with sizes <300, 300>)"
# Cross validation with 10 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

estimator = mlp
plot_learning_curve(estimator, title, X_train, y_train,ylim=(0.0,1.5), cv=cv, n_jobs=4)

plt.show()
