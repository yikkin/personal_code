# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:20:12 2016

@author: yjl20
"""

from sklearn import tree
import random as rnd
#creation of data

nb_random = 50

sample1 = [[rnd.randint(171 ,181) , rnd.randint(70 , 90),rnd.randint(43 , 46)] for k in range(50)]
  
sample2 = [[rnd.randint(155 ,170) , rnd.randint(50 , 65),rnd.randint(39 , 43)] for k in range(50)]
             
X = sample1 + sample2

y1 = ['male']*50
y2 = ['female']*50

Y = y1  + y2

#classification of the measurments according to the gender
classifier_gender = tree.DecisionTreeClassifier()
classifier_gender = classifier_gender.fit(X ,Y)

new_element = [rnd.randint(171 ,181) , rnd.randint(70 , 90),rnd.randint(43 , 46)]
     
#method to choose and predict as many measurements that we want            
def gender_prediction(number_element_predict):
    
    list_gender_predicted = []
    for element in range(number_element_predict):
        element_predit = rnd.randint(0,1)
        
        if element_predit  == 0:
            new_element = [rnd.randint(171 ,181) , rnd.randint(70 , 90),rnd.randint(43 , 46)]
            predict_gender = classifier_gender.predict([new_element])
            predict_gender = list(predict_gender)
            list_gender_predicted.append([element + 1 ,predict_gender])
        else : 
            
            new_element = [rnd.randint(155 ,170) , rnd.randint(50 , 65),rnd.randint(39 , 43)]
            predict_gender = classifier_gender.predict([new_element])
            predict_gender = list(predict_gender)
            list_gender_predicted.append([element + 1 , predict_gender])

    return(list_gender_predicted)
    
#screen printing of the gender prediction   
print(gender_prediction(15))

