# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 00:12:24 2016

@author: yjl20
"""
#a refaire le graphe avec sum direct et non courante
#Sorti des barplots
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

list_isp = list(set(streamroot_data['isp']))
print('---------------------LIST OF THE ISP NAME--------------------------')
print(list_isp)



def som_data_isp(data , list_name_isp , connection , connection_state, column_target , type1 , type2):
    cur_data = data[data[connection] == connection_state]
    rolling_som1_data = 0
    rolling_som2_data = 0
    #vector_isp = list(data[column_target])
    rolling_som_data = []
    #list_vector1_data = list()
    #list_vector2_data = list()
    #number_isp = 0
    
    for isp in list_name_isp:
        stream_data = cur_data[cur_data[column_target] == isp]

        rolling_som1_data = sum(stream_data[type1])
        rolling_som2_data = sum(stream_data[type2])
        
        rolling_som_data.append([isp, rolling_som1_data , rolling_som2_data ,rolling_som1_data /(rolling_som2_data + rolling_som1_data) , rolling_som2_data /(rolling_som2_data + rolling_som1_data) ])

        
        
        
        
        
    
        
    return rolling_som_data
    
#result_som_data_browser = som_data_browser(data = streamroot_data , name_isp = 'BTP' , column_target = 'isp' , column_name = 'browser' , connection = 'connected' , connection_state = False  , type1 = 'p2p' , type2 = 'cdn')
        
print('##################################################################################') 
print('-----------------------------SOM DATA BY ISP----------------------------------------')

result_som_data_isp = som_data_isp(data = streamroot_data , list_name_isp = list_isp , connection = 'connected' , connection_state = True ,  column_target = 'isp'  , type1 = 'p2p' , type2 = 'cdn')
streamroot_data_isp = pd.DataFrame(result_som_data_isp)
streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn' , '%p2p' , '%cdn']  
fig = plt.figure()
fig.suptitle('p2p and cdn data by ISP')
#for k in range((len(list_isp))):
#    result_som_data_isp = som_data_isp(data = streamroot_data , name_isp = list_isp[k] , column_target = 'isp' ,  connection = 'connected' , connection_state = True  , type1 = 'p2p' , type2 = 'cdn')
#
som_data_type1 = [result_som_data_isp[j][1] for j in range(len(result_som_data_isp))]
som_data_type2 = [result_som_data_isp[j][2] for j in range(len(result_som_data_isp))]
name_isp = [result_som_data_isp[j][0] for j in range(len(result_som_data_isp))]                  
#
#
width = 0.1
ind = 1

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % float(height),
                ha='center', va='bottom')
for k in range(len(list_isp)):
    ax = plt.subplot(2 , 3 ,k+1)
    fig.set_size_inches(18.5, 10.5)
    rects1 = ax.bar(ind, som_data_type1[k], width, color='lightgreen')
    rects2 = ax.bar(ind + width,som_data_type2[k], width, color='lightblue')
    ax.set_ylabel('amount of data')
    ax.set_title(name_isp[k] )
#
#    streamroot_data_isp = pd.DataFrame(result_som_data_isp)
#    streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn']
    #ax.set_xticks(ind + width)
    ax.set_xticklabels('')

    ax.legend((rects1[0], rects2[0]), ('p2p', 'cdn') , loc = 2)

    #autolabel(rects1)
    #autolabel(rects2)

    







plt.show()
    
 
print('########################GLOBAL VIEW PP AND CDN#######################')
print('==============CONNECTED STREAMROOT BACKEND============================')
print(streamroot_data_isp)

