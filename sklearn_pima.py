# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:51:21 2016

@author: etu2016
"""
import pandas as pd
from sklearn import metrics
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy  as np
from sklearn.cross_validation import train_test_split
pima = pd.read_csv('pima.txt' , header = 0)
pima = pd.DataFrame(pima)

pima_shape = pima.shape
pima_columns = pima.columns
pima_type =pima.dtypes

pima_info = [pima_shape , pima_columns , pima_type]

print(pima_info)

pima_matrix = pima.as_matrix()

x = pima_matrix[: , 0:8]
y = pima_matrix[:,8]

x_train , x_test , y_train , y_test = train_test_split(x,y,train_size =pima.shape[0] - 300)

print(y_train.shape)

C = 1.0
kernel = 'linear'


classifier = SVC(C=1.0,kernel='linear', coef0=0.0,degree=3, gamma='auto',
    decision_function_shape=None,
    max_iter=-1,
    probability=False,
    random_state=None,
    shrinking=True,
    tol=0.001,
    verbose=False)

classifier.fit(x_train , y_train)

predictions = classifier.predict(x_test)
confusion_matrix = metrics.confusion_matrix(y_test , predictions)
print('matrice de confusion' , confusion_matrix)

accuracy = metrics.accuracy_score(y_test , predictions)

print('taux de succes :' , accuracy)

error = 1 - accuracy
print('taux d erreur :',error)

from sklearn.feature_selection import RFE
selecteur = RFE(estimator = classifier)

#lancer la recherche
sol = selecteur.fit(x_train,y_train)
print(sol.n_features_)

#liste des variables sélectionnées
print(sol.support_)

#ordre de suppression
print(sol.ranking_)

x_new_train= x_train[:,sol.support_]
x_new_test= x_test[:,sol.support_]
#y_new_train= y_train[:,sol.support_]
print(x_new_train.shape)

classifier.fit(x_new_train , y_train)

predictions = classifier.predict(x_new_test)
confusion_matrix = metrics.confusion_matrix(y_test , predictions)
print('matrice de confusion' , confusion_matrix)

accuracy = metrics.accuracy_score(y_test , predictions)

print('taux de succes :' , accuracy)

error = 1 - accuracy
print('taux d erreur :',error)