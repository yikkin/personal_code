# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:38:35 2017

@author: yjl20
"""
#modules importation
import pandas as pd


#type_file = txt

def text_file(filename):
    file_text = pd.read_table(filename , sep = '\t' , header = 0)
    #file_text = file_text.dropna()
    print(file_text.head())
    print(file_text.tail())
    
def csv_file(filename):
    file_csv = pd.read_csv(filename , sep = ';' , header = 0)
    #file_csv = file_csv.dropna(axis= 0)
    print(file_csv)
    print(file_csv)
    
type_file = input('type of the file :')
filename = input('filename:')

if type_file == 'txt':
    filename = str(filename) + '.txt'
    data_file = text_file(filename)
    
if type_file == 'csv':
    filename = str(filename) + '.csv'
    data_file = csv_file(filename)