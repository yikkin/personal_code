# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:26:54 2016

@author: yjl20
"""
#package importation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#dataset impportation
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

#method to sum the amount of data exchange by peer-to-peer or cdn regarding the ISP by streaming content
def som_data_streaming_isp(data , column_target ,column , connection , connection_state , stream_id , name_isp , type1 , type2):
    #getting a dataset where the stream_id is the stream_id (only one) in parameters
    current_data = data[data[column_target] == stream_id]
    som1_data = 0
    som2_data = 0
    result_som_data = []
    #segmentation by ISP
    for isp in name_isp:
        #getting the dataset where the ISP (only one) in the current ISP
        rolling_data = current_data[current_data[column] == isp]
        #storing the sum into local variable
        som1_data = sum(rolling_data[type1])
        som2_data = sum(rolling_data[type2])
        #storing the result in a list
        result_som_data.append([isp , som1_data/(som1_data + som2_data) , som2_data/(som1_data + som2_data)])
    #transformation of the list into a  dataframe
    dataframe = pd.DataFrame(result_som_data)
    dataframe.columns = [column , '%' + type1 , '%' + type2]
        
    return dataframe
 
#code testing 
stream_id = 9


result_som_data_streaming_isp = som_data_streaming_isp(data  = streamroot_data , column_target = 'stream_id' ,column = 'isp' , connection = 'connected' , connection_state = True , stream_id  = stream_id, name_isp = list(set(streamroot_data['isp'])) , type1 = 'p2p' , type2 = 'cdn')
print(result_som_data_streaming_isp)

#plotting of the results on one figure [one stream_id and all p2p cdn data by ISP]
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
    
   
plt.show()
        
        
        
