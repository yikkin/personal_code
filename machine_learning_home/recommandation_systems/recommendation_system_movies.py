# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:12:29 2016

@author: yjl20
"""

import numpy as np
import scipy as sc
#datasets of 100k mvies rated by viewers
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
#fetch data and format it
data = fetch_movielens(min_rating = 4.0)

#print and training and testing data
#print(repr(data['train']))
#print(repr(data['test']))

#create model
model = LightFM(loss = 'warp')

#train model 
model.fit(data['train'] , epochs = 30 , num_threads = 2)

def sample_recommandation(model , data , user_ids):
    #number of users and movies in training data
    n_users , n_items = data['train'].shape
    #generate recommandations for each user we input
    for user_id in user_ids:
        #movies they already likes
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        #movies our model
        scores = model.predict(user_id , np.arange(n_items))  
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)] 
        #print our results
        print('user %s',user_id)
        print('known positives :')
        for x in known_positives[:3]:
            print('%s',x)
            
        print('recommended:')
        for x in top_items[:3]:
            print('%s',x)



          
res_recommandation = sample_recommandation(model , data ,user_ids = [3,25,450])
            


        
        
                                
