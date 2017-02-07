# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 08:36:37 2017

@author: yjl20
"""
#module importation

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
#from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics

from data_preprocessing import binary_coding , separate_type


#data importation
LP  = pd.read_csv('Loan_Predictions.csv', sep =';' , header = 0)

#droping the NAN values (null values)
LP = LP.dropna()

#basics informations
types = LP.dtypes
columns_names = LP.columns

print('features types:' , types)
print('features names:' , columns_names)

#numerical description
print('description:' , LP.describe())


x = LP.drop('Loan_Status' , 1)
x = x.drop('Loan_ID' , 1)
y = LP['Loan_Status']


#splittting data
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.33 , random_state = 1)

#dealing with categorical variables 
x_train = separate_type(x_train)
x_test = separate_type(x_test)

y_train = binary_coding(y_train)
y_test =binary_coding(y_test)


##model application
#forest with 500 trees
Classifier = RandomForestClassifier(n_estimators = 500 , criterion = 'entropy')
Classifier.fit(x_train , y_train)
predictions = Classifier.predict(x_test)
#
##model evaluation
accuracy  = metrics.accuracy_score(y_test , predictions)
matrix_confusion = metrics.confusion_matrix(y_test , predictions)

print('confusin matrix:' , matrix_confusion)

print('precision ratio:' , accuracy)
print('error ratio : ' , 1-accuracy)


#confusin matrix: [[23 31]
# [ 7 98]]
#precision ratio: 0.761006289308
#error ratio :  0.238993710692

#note : the precision can be sharpen by modifying the parameters


