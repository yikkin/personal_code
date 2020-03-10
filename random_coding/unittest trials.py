# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:08:35 2020

@author: jean-
"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    

unittest.main()


#acces a toute la documentation de une fonction
#de unittest

help(unittest.TestCase.assertIn)