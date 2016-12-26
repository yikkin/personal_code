# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 00:12:24 2016

@author: yjl20
"""

#Sorti des barplots
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

list_isp = list(set(streamroot_data['isp']))
print('---------------------LIST OF THE ISP NAME--------------------------')
print(list_isp)



def som_data_isp(data , list_name_isp , column_target , connection , connection_state , type1 , type2):
    
    rolling_som1_data = 0
    rolling_som2_data = 0
    
    rolling_som_data = []
    
    
    for isp in list_name_isp:
        current_data = data[data[column_target] == isp]
        rolling_data = current_data[current_data[connection] == connection_state]
        rolling_som1_data = sum(rolling_data[type1])
        rolling_som2_data = sum(rolling_data[type2])
        
        rolling_som_data.append([isp, rolling_som1_data , rolling_som2_data ,rolling_som1_data /rolling_som2_data ])
        
    
        
    return rolling_som_data
    
#result_som_data_browser = som_data_browser(data = streamroot_data , name_isp = 'BTP' , column_target = 'isp' , column_name = 'browser' , connection = 'connected' , connection_state = False  , type1 = 'p2p' , type2 = 'cdn')
        
print('##################################################################################') 
print('-----------------------------SOM DATA BY ISP----------------------------------------')

result_som_data_isp = som_data_isp(data = streamroot_data , list_name_isp = list_isp , column_target = 'isp' ,  connection = 'connected' , connection_state = True  , type1 = 'p2p' , type2 = 'cdn')
streamroot_data_isp = pd.DataFrame(result_som_data_isp)
streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn' , 'p2p//cdn']  
fig = plt.figure()
#for k in range((len(list_isp))):
#    result_som_data_isp = som_data_isp(data = streamroot_data , name_isp = list_isp[k] , column_target = 'isp' ,  connection = 'connected' , connection_state = True  , type1 = 'p2p' , type2 = 'cdn')
#
som_data_type1 = [result_som_data_isp[j][1] for j in range(len(result_som_data_isp))]
som_data_type2 = [result_som_data_isp[j][2] for j in range(len(result_som_data_isp))]
name_isp = [result_som_data_isp[j][0] for j in range(len(result_som_data_isp))]                  
#
#
width = 0.1
ind = np.arange(len(list_isp))


ax = plt.subplots()
fig.set_size_inches(9.5, 5.5)
rects1 = ax.bar(ind, [1,2,4,5,4], width, color='green')
rects2 = ax.bar(ind + width,som_data_type2, width, color='purple')
ax.set_ylabel('amount of data')
#    ax.set_title(list_isp[k])
#
#    streamroot_data_isp = pd.DataFrame(result_som_data_isp)
#    streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn']
ax.set_xticks(ind + width)
ax.set_xticklabels(streamroot_data_isp['isp'])
ax.legend((rects1[0], rects2[0]), ('p2p', 'cdn'))


    
def autolabel(rects):
    # attach some text labels
   for rect in rects:
       height = rect.get_height()
       ax.text(rect.get_x() + rect.get_width()/4., 1.05*height,
             '%d' % int(height),
               ha='center', va='bottom')



plt.show()
#    
 
 

print(streamroot_data_isp)