#(reecrire toutes les fonctions en mode "class" pour faire plus propre)
#voir a les rendre "rolling" (au fil de l'eau) Rio Tinto coding style with the "deque" adn stuff
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


#conversion (from string to integers) of all modalities in a target column 
def multinary_coding(dataframe , name_column):
    target = df[name_column].tolist()
    print(target)
    list_initialized = [0 for elt  in target]
    list_target = [[modality , convert_modality] for modality , convert_modality in zip(list(set(target)), range(len(target)))]
    print(list_target)
    
    def extraction_indexes_occurency(elt , vector_target):
        indices = [i for i, x in enumerate(target) if x == elt[0]]
        return indices

    indexes_modality = list(map(lambda x : extraction_indexes_occurency(x , target) , list_target))
    list_values = list(map(lambda x : x[1] , list_target))
    print(list_values)
    
    def remplissage_liste(indexes_modality , val , list_initialized):
        for index  in indexes_modality:
            list_initialized[index] = val
        return list_initialized

    convert_target = []
    for list_indexes_modality , value in zip(indexes_modality , list_values):
        convert_target = remplissage_liste(list_indexes_modality , value , list_initialized)
    
    dataframe["convert_target"] = convert_target
    return dataframe 



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

#methode pour filtrer selon une valeur voulu et son indice
def filtlist(self , condition , index):
    res = []
    for line in self:
        if line[index] == condition:
            res.append(line)
    return res
 
satisfaction_votes = filtlist(resultats , 'Caisse 1' , 0)

#methode de verification si reel est un integer
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def is_integer(fl):
    return isclose(fl, round(fl))

#methode pour extraire tous les elements inferieurs a un autre  en index
def under_line(self , elt):
    index = self.index(elt)
    
    reslt = []
    
    for element in self:
        if self.index(element) > index:
            reslt.append(element)
            
    return reslt

#methode pour trouver l index d un element
def get_index(self , item):
    try:
        return self.index(item)
    except ValueError:
        pass


#methode pour verifier si une liste est vide
def is_empty(a):
    return not a and isinstance(a, collections.Iterable)

