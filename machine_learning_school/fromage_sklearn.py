# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:50:31 2016

@author: etu2016
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import metrics
fromage = pd.read_csv('fromage.txt' , sep = '\t' , header = 0 , index_col = 0)

fromage_prime = preprocessing.scale(fromage)
from sklearn import cluster

print(fromage.head())
print(fromage.describe())

classifierdbscan = cluster.DBSCAN(eps = 0.3 , min_samples = 4 ,  metric = 'cosine', algorithm = 'brute')

classifierdbscan.fit(fromage_prime)

classifierbirch = cluster.Birch(threshold = 0.3 , n_clusters = 4)

classifierbirch.fit(fromage_prime)

print([classifierdbscan.fit_predict(fromage_prime),classifierbirch.subcluster_labels_] )

idk = np.argsort(classifierdbscan.labels_)

print(pd.DataFrame(fromage.index[idk],classifierdbscan.labels_[idk]))

idk = np.argsort(classifierbirch.labels_)

print(pd.DataFrame(fromage.index[idk],classifierbirch.labels_[idk]))

print('silhouette_dbscan:',metrics.silhouette_score(fromage_prime[classifierdbscan.labels_ != -1] ,classifierdbscan.labels_[classifierdbscan.labels_ != -1]))
print('silhouette_birch:',metrics.silhouette_score(fromage_prime[classifierbirch.labels_ != -1] ,classifierdbscan.labels_[classifierbirch.labels_ != -1]))
