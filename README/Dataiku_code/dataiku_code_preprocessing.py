# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 03:23:56 2017

@author: yjl20
"""
#import packages
import pandas as pd 

#dataset importation
us_census_data_learn = pd.read_csv('census_income_learn.csv' , sep = ';' , header = None)
us_census_data_test = pd.read_csv('census_income_test.csv' , sep = ';' , header = None)


#transformation into a dataframe
us_census_income_learn = pd.DataFrame(us_census_data_learn)
us_census_income_test = pd.DataFrame(us_census_data_test)

length_dataframe_learn = us_census_income_learn.shape[1] #number of rows in us_census_income dataframe
length_dataframe_test = us_census_income_test.shape[1]

us_census_income_learn_header = [['var' , str(k+1)] for k in range((length_dataframe_learn-1))]
us_census_income_test_header = [['var' , str(k+1)] for k in range((length_dataframe_test-1))]


us_census_income_learn_header_concatenate = [''.join(element) for element in us_census_income_learn_header]
us_census_income_learn_header_concatenate.append('target')                                  
us_census_income_learn.columns = us_census_income_learn_header_concatenate  

us_census_income_test_header_concatenate = [''.join(element) for element in us_census_income_test_header]
us_census_income_test_header_concatenate.append('target')                                  
us_census_income_test.columns = us_census_income_test_header_concatenate                                    

#head of the dataset
#print(us_census_income.head())

target_column_learn = us_census_income_learn['target']
target_column_test = us_census_income_test['target']
#binarisation of the target column
def binary_coding(column):
    binary_column = pd.get_dummies(column)
    return binary_column
    
binary_target_column_learn = binary_coding(target_column_learn)
binary_target_column_test = binary_coding(target_column_learn)

#assignement of binarisation to the target column
binary_target_column_learn.columns = ['under_treshold' , 'target']
binary_target_column_learn_saved = binary_target_column_learn['target']

binary_target_column_test.columns = ['under_treshold' , 'target']
binary_target_column_test_saved = binary_target_column_test['target']

us_census_income_learn['target'] = binary_target_column_learn_saved
us_census_income_test['target'] = binary_target_column_test_saved

#checking if the dataframe have been correctly modified
#←print(us_census_income_learn['target'].head(75))


us_census_income_learn.to_csv('census_income_learn_preprocessed.csv',sep = ';')
us_census_income_test.to_csv('census_income_test_preprocessed.csv',sep = ';')

