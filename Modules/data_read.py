# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:38:35 2017

@author: yjl20
"""
"""
module d'ouverture et de lecture d'entete de tout type de fichier rencontré 
au travers le temps 
"""

#modules importation
import pandas as pd

#methode d ouverture d un fichier de type "txt"
def text_file(filename):
    file_text = pd.read_table(filename , sep = '\t' , header = 0)
    #file_text = file_text.dropna()
    print(file_text.head())
    print(file_text.tail())

 #methode d ouverture d un fichier de type "csv"   
def csv_file(filename):
    file_csv = pd.read_csv(filename , sep = ';' , header = 0)
    #file_csv = file_csv.dropna(axis= 0)
    print(file_csv.head())
    print(file_csv.tail())

#interrogation du type de fichier 
type_file = input('type of the file :')
#nom du fichier
filename = input('filename:')

#ouverture en fonction du .type_file
if type_file == 'txt':
    data_file = text_file(filename)
    
if type_file == 'csv':
    data_file = csv_file(filename)
