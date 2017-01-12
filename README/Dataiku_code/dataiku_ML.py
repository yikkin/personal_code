# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:18:22 2017

@author: yjl20
"""

#importation pacakges
from sklearn import tree , metrics
#from sklearn.preprocessing import OneHotEncoder 
from sklearn.feature_extraction import DictVectorizer


import pandas as pd

#importation dataset 
us_census_data_learn = pd.read_csv('census_income_learn_preprocessed.csv', sep = ';' , header = 0)
us_census_data_test = pd.read_csv('census_income_test_preprocessed.csv' , sep = ';' , header = 0)
#transformation into a dataframe
us_census_income_learn = pd.DataFrame(us_census_data_learn)
us_census_income_test = pd.DataFrame(us_census_data_test)
#features selection
y_train = us_census_income_learn['target']
X_train = us_census_income_learn.drop('target' , 1)

X_test =  us_census_income_test.drop('target' , 1)
y_test = us_census_income_test['target']

def separate_type(dataframe):
    colnames = dataframe.columns
    qual_data = pd.DataFrame()
    quant_data = pd.DataFrame()
    for element in colnames:
        if type(dataframe[element][0]) == str:
            qual_data[element] = dataframe[element]
     
        else :
            
            quant_data[element] = dataframe[element]
   
   
    return [quant_data , qual_data]
            
            
X_train_separate_type = separate_type(X_train)
X_test_separate_type = separate_type(X_test)

            


def coding_qualitative_variable(dataframe):
    
    dictvect = DictVectorizer(sparse=False) 
    df = pd.DataFrame(dataframe).convert_objects(convert_numeric=True)
    result_coding = dictvect.fit_transform(df.to_dict(orient='records'))
    
    return [result_coding , dictvect.feature_names_]
    
coding_X_train = coding_qualitative_variable(X_train_separate_type[1])[1]
coding_X_test = coding_qualitative_variable(X_test_separate_type[1])[1]
print('######################RECODING MODALITIES DATASET#########################################')
print('recoding training file :' , len(coding_X_train) , 'numbers of modalities')
print('recoding test file :' , len(coding_X_test) , 'number of modalities') 
                                           
#lst = []
#for element in list(set(X_train_separate_type[1])):
#    lst.append(set(list(X_train_separate_type[1][element])))
#    
#lste = []
#for elt in list(set(X_train_separate_type[1])):
#    lste.append(set(list(X_train_separate_type[1][elt])))
    
    









 

