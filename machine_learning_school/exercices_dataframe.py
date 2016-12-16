# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:39:15 2016

@author: etu2016
"""

#importation de packages
import pandas as pd
import numpy as np
import datetime as dt
import pandas.io.data
import matplotlib.pyplot as plt
#importation de donnees
#Cotation_Orange = pd.io.data.get_data_yahoo('ORA.PA', start = dt.datetime(2014 , 1 , 1) , end = dt.datetime(2015 , 12 , 31))
#Cotation_Bouygues = pd.io.data.get_data_yahoo('EN.PA', start = dt.datetime(2014 , 1 , 1) , end = dt.datetime(2015 , 12 , 31))

#enregistrement dans un csv
#Cotation_Orange.to_csv('Cotation_Orange.csv' , sep = ';')
#Cotation_Bouygues.to_csv('Cotation_Bouygues.csv' , sep = ';')

#transformation en dataframe
dfOrange = pd.read_csv('Cotation_Orange.csv',sep = ';' , index_col = 'Date' ,parse_dates = True)
dfBouygues =  pd.read_csv('Cotation_Bouygues.csv',sep = ';' , index_col = 'Date' ,parse_dates = True)

dfOrange['diff_high_low'] = dfOrange['High'] - dfOrange['Low']
dfBouygues['diff_high_low'] = dfBouygues['High'] - dfBouygues['Low']

dfOrange['diff_open_close'] = dfOrange['Open'] - dfOrange['Close']
dfBouygues['diff_open_close'] = dfBouygues['Open'] - dfBouygues['Close']


#new_dfOrange = dfOrange[ dt.datetime(2015 , 12, 31) < dfOrange < dt.datetime(2015 , 1, 1)]
#dfdate = dfOrange[ dfOrange  >= dt.datetime(2015 , 12 , 31)]

#print(dfOrange.)
#◘Cotation_Time = [dt.datetime(2014 , 1 , 1) + dt.timedelta(k) for k in range((len(dfOrange) + 180)]
#visualisation graphique
Corr_df_orange_bouygues = pd.concat([dfOrange['Close'] ,  dfBouygues['Close']] , axis = 1  , keys = ['dfOrange' , 'dfBouygues'])

print(Corr_df_orange_bouygues.corr())
#il semblerait que les actions de orange et bouygues sont corréles
#assez fortement car le coefficient de corrélation est de 0.75 (fortement corrélé)

datas_orange = dfOrange[dfOrange.index >= dt.datetime(2015 , 1 ,1)]
datas_bouygues = dfBouygues[dfOrange.index >= dt.datetime(2015 , 1 ,1)]
plt.subplot(2,1,1)
plt.plot(datas_orange['diff_open_close'],'red', datas_orange['diff_high_low']  ,'blue')
plt.title('CAC40_Orange')
plt.ylabel('cotation_orange')
plt.grid()
plt.subplot(2,1,2)
plt.plot( datas_bouygues['diff_open_close'],'purple' , datas_bouygues['diff_high_low'],'yellow')
plt.title('CAC40_Bouygues')
plt.ylabel('cotation_bouygues')
plt.grid()
plt.show()

#plt.legend(
#print(dfOrange)