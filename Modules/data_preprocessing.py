# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:23:03 2017

@author: yjl20
"""
#module importation
import pandas as pd

#percentage of missing values
def percent_missing_values(dataframe):
    percentage_missing_values = 1 - dataframe.count(axis = 0) / dataframe.shape[0]
    return percentage_missing_values
    

#binarisation of the target column
def binary_coding(column):
     #extraction of the modalities for the target variable
    modalities = list(set(column))
    #binarisation
    binary_column = pd.get_dummies(column) 
    return binary_column[modalities[1]] 



def separate_type(dataframe):
    dataframe   = dataframe.dropna()
    #coltypes = dataframe.dtypes
    colnames = list(dataframe.columns)
    qualitative_data = pd.DataFrame()
    quantitative_data = pd.DataFrame()
    #names_types = list(map(lambda x , y : [x,y] , colnames , coltypes))
    for variable in colnames:
        if dataframe[variable].dtypes != 'float64' or dataframe[variable].dtypes != 'int64' :
            qualitative_data[variable] = dataframe[variable].astype('category')
            
        else :
            quantitative_data[variable] = dataframe[variable]
            
    categorical_columns = qualitative_data.select_dtypes(['category']).columns
    qualitative_data[categorical_columns] = qualitative_data[categorical_columns].apply(lambda x: x.cat.codes)
    
    new_dataframe = pd.concat([qualitative_data , quantitative_data] , axis = 1)
    return new_dataframe
   








