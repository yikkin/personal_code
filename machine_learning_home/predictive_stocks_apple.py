# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:10:46 2016

@author: yjl20
"""

#importation dde packages
import csv 
import numpy as np
import numpy
import pandas as pd
from sklearn.svm import SVR
#svm methode separant  un subset deja classifier
#de celui non classifir et essaye de le predire
import matplotlib.pyplot as plt
import pandas.io.data
import datetime as dt
#intervalle de temps a analyser
dates = []

#prix de du stock a ces dates
prices = []

#importation des donnees
Cotation = pd.io.data.get_data_yahoo('AAPL', start = dt.datetime(2015 , 11 , 22) , end = dt.datetime(2016 , 12 , 19))

#definition de la fonction de recuperation de donnees
#♦si vous recuperez vos donnees de google finance et enregistrer sur un csv
def get_data_register(filename):
    #ouverture du csv en mode lecture
    with open(filename , 'r' , ) as csvfile:
        #instruction a la lecture de chaque ligne
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            #mode de separation digits dates
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[0].split(';')[1]))
            
    return [dates , prices]

#si vous recueperez vos donnees de yahoo finance en ligne
def get_data_online(dataframe , name_column):
    
    dates = []
    new_array = np.array(dataframe.index.to_pydatetime(), dtype=numpy.datetime64)
    nw = new_array.tolist()
    
    for elt in nw:
        dates.append(elt.day)
        
    prices = dataframe[name_column]
    return [dates , prices.values]
    
def predict_prices(dates , prices , x , kernel):
    dates = np.reshape(dates , (len(dates) , 1))
    
    svr_model = SVR(kernel = kernel , C =1e3)
    svr_model.fit(dates , prices)
    
    
    plt.scatter(dates , prices , color = 'black' , label ='Apple Stocks Data')
    plt.plot(dates, svr_model.predict(dates) , color = 'red' , label = 'linear model')
    
    plt.xlabel('dates')
    plt.ylabel('price')
    plt.title('Suport Vector Regression')
    plt.legend()
    plt.show()
    
    #prediction de la regression sur l approche
    
    return svr_model.predict(x)[0]

#a remarquer que on aurait pu utiliser la fonction gridsearch pour trouver le C optimal 
#get_data('apple.csv')

#pour le csv
dates = get_data_register('apple.csv')[0]
prices = get_data_register('apple.csv')[1]

#kernel = ['linear','rbf']
#
predicted_price = predict_prices(dates , prices ,29 , kernel = 'rbf')
#
print('predcted value' , predicted_price)

#nom de la colonne a evaluer
name_column = 'Open'
dates = get_data_online(Cotation , name_column)[0]
prices = get_data_online(Cotation , name_column)[1]

##pour la version online
predicted_price = predict_prices(dates , prices , 29 , kernel = 'linear')

print('predicted value' , predicted_price)




