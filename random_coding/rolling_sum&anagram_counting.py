# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:00:47 2017

@author: etu2016
"""

import math as m

#Calcul de somme glissante d'un tableau
def rollin_sum(liste , size_window):
    result = []
    for k in range((len(liste)- size_window + 1)):
        #sotckage des elements sur une fenetre temporaire
        curr_liste = liste[k:k+size_window]
        #recuperation des sommes
        result.append(sum(curr_liste))
    return result

#test unitaire

#liste test  
liste_test = [k for k in range(5)]

#impression des resultats en sortie
print("the rolling sum on " +str(liste_test)+ " is:" +str(rollin_sum(liste_test , 3)))
    
# Réalisez un algo pour compter les anagrammes d'une liste de   mots    
def anagram_counting(liste_words , liste_syllables):
    result = []
    for syl in liste_syllables:
        #stockage du compte du nombre d anagrammes par mots
        result.append(m.factorial(syl))
        
    return result

#test unitaire

#liste de mots test
liste_words_test = ['allo' , 'bench' , 'brain']
#liste de anagram test
liste_anagram_test = [4,3,3]
print(" the anagram counting of your " +str(liste_words_test)+ " is : " + str(anagram_counting(liste_words_test , liste_anagram_test)))
        
        