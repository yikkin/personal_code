# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:23:03 2017

@author: yjl20
"""
#module importation
import pandas as pd
from datetime import datetime
import numpy as np

#percentage of the missing values
def percent_missing_values(dataframe):
    missing_values_columns = dataframe.apply(lambda x : sum(x.isnull().values) , axis = 0)
    missing_values_percent = missing_values_columns / dataframe.shape[0]
    return missing_values_percent
    

#binarisation of the target column
def binary_coding(column , modality):
     #extraction of the modalities for the target variable
    #binarisation
    binary_column = pd.get_dummies(column) 
    return binary_column[modality] 



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
	

   
def preliminaries_xls(filename):
    dataframe = pd.read_excel(filename , header = 0)
    dataframe2 = pd.DataFrame()
    print('head of file:' ,  dataframe.head())
    print('tail of file:' ,  dataframe.tail())
    print('features names:' , dataframe.columns)
#numerical description
    print('description :', dataframe.describe())

    print('missing values :' , percent_missing_values(dataframe))
    
    numb = input('combien de colonnes a effacer ?')
    
    if int(numb) == 0 :
        return dataframe
    
    print('quels colonnes supprimer ?')
    for index in range(int(numb)):
        colonne = input()
        dataframe2 = dataframe.drop(colonne , 1)
    
    print('features names:' , dataframe.columns)
    print('number of rows (before) :' , len(dataframe))
    
    dataframe2 = dataframe2.dropna()
    
    print('number of rows (after) :' , len(dataframe2))
    print('features names:' , dataframe2.columns)
    print('missing values :' , percent_missing_values(dataframe2))
    print('percent drop :' , (len(dataframe) -  len(dataframe2))/len(dataframe))
    
    return dataframe2

def preliminaries_txt(filename):
    dataframe = pd.read_csv(filename , sep = '\t' , header = 0)
    dataframe2 = pd.DataFrame()
    print('head of file:' ,  dataframe.head())
    print('tail of file:' ,  dataframe.tail())
    print('features names:' , dataframe.columns)
#numerical description
    print('description :', dataframe.describe())

    print('missing values :' , percent_missing_values(dataframe))
    
    numb = input('combien de colonnes a effacer ?')
    if int(numb) == 0 :
        return dataframe
    
    print('quels colonnes supprimer ?')
    for index in range(int(numb)):
        colonne = input()
        dataframe2 = dataframe.drop(colonne , 1)
    
    print('features names:' , dataframe.columns)
    print('number of rows (before) :' , len(dataframe))
    
    dataframe2 = dataframe2.dropna()
    
    print('number of rows (after) :' , len(dataframe2))
    print('features names:' , dataframe2.columns)
    print('missing values :' , percent_missing_values(dataframe2))
    print('percent drop :' , (len(dataframe) -  len(dataframe2))/len(dataframe))
    
    return dataframe2
    
def occurency(item_liste):
    liste_occurency = [[x,item_liste.count(x)] for x in set(item_liste)]
    return sorted(liste_occurency)

def EWMA(vector , alpha):
    
    output = vector
    for k in range(1,len(vector)):
        output[k] = alpha * vector[k] + (1-alpha) * output[k-1]
        
    return output

#a refaire cette fonction
def aggregate_time(dataframe , colonne_target , colonne_time):
    list_sum = []
    set_time = sorted(list(set(dataframe[colonne_time])))
    for time in set_time:
        res = dataframe[dataframe[colonne_time] == time]
        aggregate_sum = sum(res[colonne_target])
        list_sum.append(aggregate_sum)
        
    return list_sum



#def aggregate_vote(dataframe  , colonne_time):
    

def aggregate_dataframe(dataframe , colonne_target):
    list_dataframe = []
    modalities = list(set(dataframe[colonne_target]))
    for mod in modalities:
        df = dataframe[dataframe[colonne_target] == mod]
        list_dataframe.append(df)
        
    return list_dataframe


def create_timeline(dataframe , col_time , intervalle):
    df_time = dataframe[col_time]
    if intervalle == 'day':
         time_space = list(map(lambda x : x.strftime('%Y-%m-%d') , df_time))
    if intervalle == 'week':
        time_space = list(map(lambda x : datetime.strptime(x, '%Y-%m-%d').date().isocalendar()[1] , df_time))
    if intervalle == 'month':
        time_space = list(map(lambda x : x.strftime('%Y-%m') , df_time))
    if intervalle == 'hour':
        time_space =  list(map(lambda x : x.hour , df_time))
        
    dataframe[intervalle] = time_space
    
    return dataframe
    
def moyenne(liste1, liste2 ,liste3):
   moy = list(map(lambda x,y,z : (x + 0.5*y)/(x+y+z) , liste1,liste2,liste3))
    
   return moy





#res = list(map(lambda x , y : x/y[1] , aggregate_time(example , 'satisfaction' , 'hour') , occurency(example['hour'].tolist())))
#
#ryes = aggregate_time(example , 'yes' , 'hour')
#rneutre = aggregate_time(example ,'neutre' , 'hour')
#rno =  aggregate_time(example , 'no' , 'hour')
#
#rest = list(map(lambda x,y,z : (x+0.5*y)/(x+y+z) , ryes , rneutre , rno))
#        

def movingaverage(interval, window_size):
    window= np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

#methode pour ajouter une ligne dans un dataframe
def add_row(self , row):
    self.loc[len(self.index)] = row
pd.DataFrame.add_row = add_row

#methode pour ajouter une colonne
def add_column(self , column_name , column_values):
    if type(column_name) != str and type(column_values) != list:
        return None
    else :
        self.loc[: , column_name] = pd.Series(column_values , index = self.index)
pd.DataFrame.add_column = add_column



