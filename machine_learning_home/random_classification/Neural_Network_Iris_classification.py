# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 06:44:02 2017

@author: yjl20
"""

#module importation
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#data importation
iris = datasets.load_iris()


x = iris.data
y = iris.target

#data splitting
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.33)

#¸model applcation
#neural network classifiaction with 5 perceptrons and 2 hidden layer 
Classifier = MLPClassifier(solver = 'lbfgs' , alpha = 1e-2 , hidden_layer_sizes = (5,2) , random_state = 1)
Classifier.fit(x_train , y_train)
predictions = Classifier.predict(x_test)


#model evaluation
accuracy = metrics.accuracy_score(y_test , predictions)
confusion_matrix = metrics.confusion_matrix(y_test , predictions)
print('confusion matrix:' , confusion_matrix)
print('precision ratio :' , accuracy)
error = 1 - accuracy
print('error ratio :', error)

#print screen
#confusion matrix: [[18  1  0]
# [ 1  9  0]
# [ 0  0 21]]
#
#precision ratio : 0.96
#error ratio : 0.04




