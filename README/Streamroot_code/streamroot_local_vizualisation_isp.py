# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 00:12:24 2016

@author: yjl20
"""
#package and dataset importation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

#setting the list of ISP name
list_isp = list(set(streamroot_data['isp']))
print('---------------------LIST OF THE ISP NAME--------------------------')
print(list_isp)


#method to get the aount of p2p and cdn data regarding the ISP name
def som_data_isp(data , list_name_isp , connection , connection_state, column_target , type1 , type2):
    cur_data = data[data[connection] == connection_state]
    rolling_som1_data = 0
    rolling_som2_data = 0
    
    rolling_som_data = []
   #loop over the list of the ISP name
    for isp in list_name_isp:
        stream_data = cur_data[cur_data[column_target] == isp]
        #storing of the amount of p2p and cdn data
        rolling_som1_data = sum(stream_data[type1])
        rolling_som2_data = sum(stream_data[type2])
        
        rolling_som_data.append([isp, rolling_som1_data , rolling_som2_data ,rolling_som1_data /(rolling_som2_data + rolling_som1_data) , rolling_som2_data /(rolling_som2_data + rolling_som1_data) ])

        
        
        
        
        
    
        
    return rolling_som_data
    

print('##################################################################################') 
print('-----------------------------SOM DATA BY ISP----------------------------------------')

#turning the list result into a dataframe
result_som_data_isp = som_data_isp(data = streamroot_data , list_name_isp = list_isp , connection = 'connected' , connection_state = True ,  column_target = 'isp'  , type1 = 'p2p' , type2 = 'cdn')
streamroot_data_isp = pd.DataFrame(result_som_data_isp)
streamroot_data_isp.columns = ['isp' , 'p2p' , 'cdn' , '%p2p' , '%cdn']  
fig = plt.figure()
fig.suptitle('p2p and cdn data by ISP')

som_data_type1 = [result_som_data_isp[j][1] for j in range(len(result_som_data_isp))]
som_data_type2 = [result_som_data_isp[j][2] for j in range(len(result_som_data_isp))]
name_isp = [result_som_data_isp[j][0] for j in range(len(result_som_data_isp))]                  
#
#
width = 0.1
ind = 1

 #plotting the result of our previous method       
for k in range(len(list_isp)):
    ax = plt.subplot(2 , 3 ,k+1)
    fig.set_size_inches(18.5, 10.5)
    rects1 = ax.bar(ind, som_data_type1[k], width, color='lightgreen')
    rects2 = ax.bar(ind + width,som_data_type2[k], width, color='lightblue')
    ax.set_ylabel('amount of data')
    ax.set_title(name_isp[k] )

    ax.set_xticklabels('')

    ax.legend((rects1[0], rects2[0]), ('p2p', 'cdn') , loc = 2)


    







plt.show()
    
 
print('########################GLOBAL VIEW PP AND CDN#######################')
print('==============CONNECTED STREAMROOT BACKEND============================')
print(streamroot_data_isp)

