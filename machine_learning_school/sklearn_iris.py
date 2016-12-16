# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:29:38 2016

@author: etu2016
"""

from sklearn.datasets import load_iris
from sklearn import metrics
iris = load_iris()
#metadata
print(iris.feature_names)
print(iris.target_names)

#head printing
print(iris.data[0:5])


x = iris.data #features
y = iris.target #label

#data partitioning
from sklearn.cross_validation import train_test_split

x_train , x_test , y_train  , y_test = train_test_split(x , y, test_size = .4)

from sklearn import neighbors
classifier = neighbors.KNeighborsClassifier(n_neighbors = 3 ,algorithm = 'ball_tree')

classifier.fit(x_train , y_train)

predictions = classifier.predict(x_test)
confusion_matrix = metrics.confusion_matrix(y_test , predictions)
print('matrice de confusion' , confusion_matrix)

accuracy = metrics.accuracy_score(y_test , predictions)

print('taux de succes :' , accuracy)

error = 1 - accuracy
print('taux d erreur :',error)



