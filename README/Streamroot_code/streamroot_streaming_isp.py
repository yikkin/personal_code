# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:26:54 2016

@author: yjl20
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

def som_data_streaming_isp(data , column_target ,column , connection , connection_state , stream_id , name_isp , type1 , type2):
    current_data = data[data[column_target] == stream_id]
    som1_data = 0
    som2_data = 0
    result_som_data = []
    for isp in name_isp:
        rolling_data = current_data[current_data[column] == isp]
        som1_data = sum(rolling_data[type1])
        som2_data = sum(rolling_data[type2])
        
        result_som_data.append([isp , som1_data/(som1_data + som2_data) , som2_data/(som1_data + som2_data)])
    
    dataframe = pd.DataFrame(result_som_data)
    dataframe.columns = [column , '%' + type1 , '%' + type2]
        
    return dataframe
  
stream_id = 9


result_som_data_streaming_isp = som_data_streaming_isp(data  = streamroot_data , column_target = 'stream_id' ,column = 'isp' , connection = 'connected' , connection_state = True , stream_id  = stream_id, name_isp = list(set(streamroot_data['isp'])) , type1 = 'p2p' , type2 = 'cdn')
print(result_som_data_streaming_isp)

fig = plt.figure()
fig.suptitle('stream_id : ' +  str(stream_id))
list_isp = list(set(streamroot_data['isp']))
k = 0
for isp in list_isp:
    k = k + 1
    current_dataframe = result_som_data_streaming_isp[result_som_data_streaming_isp['isp'] == isp]
    division =[float(current_dataframe['%p2p']), float(current_dataframe['%cdn'])] 
    activites = ['p2p' , 'cdn']
    couleurs = ['lightgreen','lightblue']
    fig.set_size_inches(9.5, 6.5)
    plt.subplot(2,3, k)
    line1 = plt.pie(division , labels=activites, colors=couleurs, startangle=90, autopct='%1.1f%%')
    plt.title('ISP : ' + isp)
    
    #div_stock0.append(division[0])
    #div_stock1.append(division[1])

#affichage du plot avec la methode show()
#fig.legend(handles = line1  , labels = ('p2p' , 'cdn'), loc = 'upper left')
plt.show()
        
        
        