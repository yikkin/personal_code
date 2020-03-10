# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:24:28 2020

@author: jean-
"""

import unittest

def add(x,y):
    return x + y

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(3,4), 7)

#unittest.main()


class testpoly_func(unittest.TestCase):
    def test_value(self):
        self.assertRaises(TypeError  , poly_func, True)
        self.assertRaises(TypeError  , poly_func, str)
        
    def test_type(self):
        self.assertIn(type(poly_func(10)),[int , float])
        
    


    
def poly_func(x):
    if type(x) not in [int , float]:
        raise TypeError("parameter not a number")
    return 2*x**3 + x + 5

elts = [2 , 0 , -3 , True]

#for elt in elts:
#    print(poly_func(elt) , end = ' ')

#dictionnaires 

a = dict()


a = {"name" : "Wayne" , "surname":"Bruce"}

def get_values(a):
    if type(a) is dict:
        if len(a) == 0:
            print("dictionary is empty")
        else:
            for val in a.values():
               yield val
    else:
        raise TypeError("parmaeter not a dictionary")
        
        
class test_dictionary(unittest.TestCase):
    def test_type(self):
        self.assertTrue(type(a) , dict)


unittest.main() 

def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
        
myFun(firs = 'gekks' , doo = 'for' ,lat = 'geeks')
    

listA = ['a','e','i','o','u']

iter_listA = iter(listA) 

while True:
    try:
        print(iter_listA.__next__())
    except:
        break


