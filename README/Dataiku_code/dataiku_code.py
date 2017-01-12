# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:18:05 2017

@author: yjl20
"""

#package importation 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
#♥import sklearn as sk

#dataset importation
us_census_data = pd.read_csv('us_census_income_learn_preprocessed.csv' , sep = ';' , header = 0)
us_census_data_test = pd.read_csv('census_income_test_preprocessed.csv' , sep = ';' , header = 0)

us_census_income = pd.DataFrame(us_census_data)
us_census_income_test = pd.DataFrame(us_census_data_test)

#dataset visualisation
print('########################HEAD AND TAIL OF THE FILE#######################################')
print(us_census_income.head(2))
print('========================================================================================')
print(us_census_income.tail(2))

dimensions = us_census_income.shape
print('dimensons' , dimensions)
columns_names = us_census_income.columns
print('columns_names' , list(columns_names))
types = us_census_income.dtypes
print('types' , types)

#print(us_census_income.describe())

print('####################### % STATISTIC AND UNIVARIATE AUDIT ################################################')

columns_described = us_census_income.describe().columns
columns_non_described = list(set(columns_described) ^ set(columns_names))
#i choose to look nan in not decribed columns because if a described columns has at least one nan then you will see it results

#print('columns not described :' , columns_non_described)

def occurency_element(data , vector):
    result_occurency = []
    for element in vector:
        liste_element = list(data[element])
        occurency =  [[x , liste_element.count(x)] for x in set(liste_element)]
        result_occurency  = result_occurency +  occurency
        
    return result_occurency
    
resultata_occurency_sorted = sorted( occurency_element(us_census_income , columns_non_described))

#print(resultata_occurency_sorted)

# [' NaN', 708],
# [' NaN', 3393],
# [' NaN', 6119],
# [' NaN', 6713],
# [' NaN', 99696],
# [' NaN', 99696],
# [' NaN', 99696],
# [' NaN', 99696]

counter_nan = 708 + 3393 + 6119 + 6713 + 3*99696
percent_missing_values = counter_nan /(dimensions[0] * dimensions[1])

print('% missing values: ' , "{0:.2f}".format(percent_missing_values*100, 2),'%')
print('========================================================================================')
print('statistical description of the quantitative variables :')
print(us_census_income.describe())


#graphical vizualisation

def bar_graphical_describe(variable):
    
    values_columns_described = [us_census_income.describe()[variable]['max'] , us_census_income.describe()[variable]['min'] , us_census_income.describe()[variable]['mean']  , us_census_income.describe()[variable]['std']]
    ind = np.arange(len(values_columns_described))
    width = 0.1
    
    fig = plt.figure()
    
    
    plt.bar(ind, values_columns_described , width, color='green')
    plt.title(variable)
    plt.xticks(ind , ['max' , 'min' , 'mean' , 'std'])
    plt.grid()
    
    title = [variable , '.png']
    new_title = ''.join(title)
    fig.savefig(new_title)

  

for element in columns_non_described:
    us_census_income = us_census_income.drop(element , 1)
    us_census_income_test = us_census_income_test.drop(element , 1)
    
print(us_census_income.columns)
    
#us_census_income.to_csv('census_income_learn_preprocessed_second_prime_prime.csv',sep = ';')
#us_census_income_test.to_csv('census_income_test_preprocessed_second_prime_prime.csv',sep = ';')
    








    

         
        
        

                                    
                                    
