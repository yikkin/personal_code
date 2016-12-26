# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 19:30:45 2016

@author: yjl20
"""

import pandas as pd
import matplotlib.pyplot as plt
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

name_browser = list(set(streamroot_data['browser']))
def som_data_isp_browser(data , column , name_isp , name_browsers , column_target , connection , connection_state ,  type1 , type2):
    som1_data = 0
    som2_data = 0
    
    current_data = data[data[column] == name_isp]
    result_som_data = []
    for browser in name_browser:
        rolling_data = current_data[current_data[column_target] == browser]
        som1_data = sum(rolling_data[type1])
        som2_data = sum(rolling_data[type2])
        
        result_som_data.append([browser , som1_data/(som1_data+ som2_data) , som2_data/(som1_data + som2_data)])
        
    
    
    return result_som_data
 
name_isp = 'Datch Telecam'
#{'Arange', 'BTP', 'Datch Telecam', 'Fro', 'Olga'}
result_som_data_isp_browser = som_data_isp_browser(data = streamroot_data , column ='isp' , name_isp = name_isp , name_browsers = name_browser , column_target = 'browser' ,connection = 'connected' , connection_state = True, type1  = 'p2p', type2 = 'cdn')
 
dataframe = pd.DataFrame(result_som_data_isp_browser)
dataframe.columns = ['browser' , '%' + 'p2p' , '%' + 'cdn']       
print(dataframe)  

som_data_type1 = [result_som_data_isp_browser[j][1] for j in range(len(result_som_data_isp_browser))]
som_data_type2 = [result_som_data_isp_browser[j][2] for j in range(len(result_som_data_isp_browser))]
name_browser = [result_som_data_isp_browser[j][0] for j in range(len(result_som_data_isp_browser))]  

width = 0.1
ind = 1
fig = plt.figure()
fig.suptitle('name ISP: ' +name_isp )
for k in range(len(name_browser)):
    ax = plt.subplot(2 , 3 ,k+1)
    fig.set_size_inches(12.5, 9.5)
    rects1 = ax.bar(ind, som_data_type1[k], width, color='lightgreen')
    rects2 = ax.bar(ind + width,som_data_type2[k], width, color='lightblue')
    ax.set_ylabel('amount of data')
    ax.set_title(name_browser[k] )
#
#    streamroot_data_isp = pd.DataFrame(result_som_data_isp)
#    streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn']
    #ax.set_xticks(ind + width)
    ax.set_xticklabels('')

    ax.legend((rects1[0], rects2[0]), ('p2p', 'cdn') , loc = 2)

    #autolabel(rects1)
    #autolabel(rects2)

    







plt.show()     
    
    