# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:14:53 2016

@author: yjl20
"""
####pre install in the cmd 
##pip install tweepy 
##pip install textblob
#to install coprora (stop words EN) python -m textblob.download_corpora
###create a twitter account and ask for your own app 
#spplitting words = tokenization
#counting numbers of times a word shows up = bag of words
import tweepy
import os
import pandas as pd
from textblob import TextBlob
print('###############example textblob###################')
liki = TextBlob('John is angry he never find the street')
print(liki.tags)

print('###########Twitter API access ####################')
consumer_key = 'OheVAjk4Rov26moFkvnuZRMnt'
consumer_secret = '3pnPBLitHwbOOFAJhmJ5LwPstFsyBoAsR4FSpHPAi06IadKJrz'

access_token = '713836308339245056-sfaxxs6cakIoCdqAlpkNqNbIAaXEp07'
access_token_secret = 'obK6qEkQSNYC10ZZMezsGWo2zuKjgzdvCY12Hi1c5Ijc3'

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth)

#keybard reading ..not wrking for my version but should work with python 2.7
#keyword = input('give the keyword or subject')

#method to get tweets from the Twitter API
def get_tweets(subject):
    
    public_tweets = api.search(subject)
    list_tweets_text = []
    list_tweets_analysis = []
    for tweet in public_tweets:
        list_tweets_text.append(tweet.text)
        analysis = TextBlob(tweet.text)
        list_tweets_analysis.append(analysis.sentiment)
        
    results_tweets = [[x,str(y)] for x,y in zip(list_tweets_text , list_tweets_analysis)]
        
    return results_tweets



##method of storage tweets in a file
def storage_tweets(list_tweets , subjects):
   list_results_tweets = []
   for tweets in list_tweets:
       list_results_tweets.append(tweets)
       
   dataframe = pd.DataFrame(list_results_tweets)
   dataframe.columns = ['Tweets' , 'Analysis']
   
   return dataframe


    
subject = 'Fillon'   
tw = get_tweets(subject)

storage_tweets(tw , subject).to_csv("sujet.csv" , sep = ";")
         
#    
#
##list of few subjects
list_subjects = ["Sopra Steria" , "Fitle" , "yikkin75"]
#
##registration of the subjects in file
def registration(list_subjects):
    
    dataframe = pd.DataFrame()
    for subject in list_subjects:
        dataframe = storage_tweets(get_tweets(subject) , subject)
        
        dataframe.to_csv(subject  + ".csv" , sep = ";")
        
#        
registration(list_subjects)

             
             





