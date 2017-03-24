#method importation
from sklearn import tree
import random as rnd
import pandas as pd

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
    #list to store the results
    for element in range(number_element_predict):
        element_predit = rnd.randint(0,1)
        #0 : male measurment , 1 : female measurment
        if element_predit  == 0:
            new_element = [rnd.randint(171 ,181) , rnd.randint(70 , 90),rnd.randint(43 , 46)]
            predict_gender = classifier_gender.predict([new_element])
            #prediction of the gender new element
            predict_gender = list(predict_gender)
            list_gender_predicted.append(predict_gender + new_element)
        else : 
            
            new_element = [rnd.randint(155 ,170) , rnd.randint(50 , 65),rnd.randint(39 , 43)]
            predict_gender = classifier_gender.predict([new_element])
            predict_gender = list(predict_gender)
            list_gender_predicted.append(predict_gender  +  new_element)
            
    
    gender_predicted = pd.DataFrame(list_gender_predicted , columns= ['gender' , 'height' , 'weight' , 'shoe size'])


    return(gender_predicted)
  
  #exemple with 10
  #screen printing of the gender prediction
#print("How many people in total do you want to predict?")
#number_of_gender_predict = int(input())
#print("These are the randomly genearated people that you asked for:")
#print(gender_prediction(number_of_gender_predict).head())

#How many people in total do you want to predict?
#10
#These are the randomly genearated people that you asked for:
#   gender  height  weight  shoe size
#0    male     174      88         44
#1  female     165      63         41
#2    male     172      84         45
#3    male     178      87         45
#4  female     168      52         43


  
