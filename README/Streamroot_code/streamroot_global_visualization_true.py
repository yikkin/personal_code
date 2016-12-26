# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 02:24:06 2016

@author: yjl20
"""

import pandas as pd
streamroot_data = pd.read_csv('streamroot_data.csv' , sep = ';' , header = 0)
streamroot_data = pd.DataFrame(streamroot_data)

#lecture preliminaire du fichier
print('########################HEAD AND TAIL OF THE FILE#######################################')
print(streamroot_data.head())
print('========================================================================================')
print(streamroot_data.tail())

#dimension  du dataframe et element colonne et types
dimensions = streamroot_data.shape
columns_names = streamroot_data.columns
types = streamroot_data.dtypes

def consumer_som_data_content(data , column_target , connection , connection_state , type1 , type2):
    list_set_ids = list(set(data[column_target]))
    current_data = data[data[connection] == connection_state]
    
    result_som_data = []
    
    for stream_id in list_set_ids:
        stream_data = current_data[current_data[column_target] == stream_id]
        som1_data = sum(stream_data['p2p'])
        som2_data = sum(stream_data['cdn'])
        
        result_som_data.append([stream_id , som1_data , som2_data , som1_data / (som1_data + som2_data) , som2_data / (som1_data + som2_data)])
    result = pd.DataFrame(result_som_data)
    result.columns = [column_target , type1 , type2 , '%' + type1 , '%' + type2]
    
        
        
    
 
	
   
		
    return result

print('###################################GLOBAL VIEW P2P AND CDN####################################')
print('=================================CONNECTED BACKEND STREAMROOT=======================================================')
consumer_data_content_true = consumer_som_data_content(data = streamroot_data , column_target = 'stream_id' , connection = 'connected' , connection_state = True , type1 = 'p2p' , type2 = 'cdn')
print(consumer_data_content_true)
#
#
print('=============================NOT CONNECTED BACKEND STREAMROOT==================================================')
print(consumer_som_data_content(data = streamroot_data , column_target = 'stream_id' , connection = 'connected' , connection_state = False , type1 = 'p2p' , type2 = 'cdn'))