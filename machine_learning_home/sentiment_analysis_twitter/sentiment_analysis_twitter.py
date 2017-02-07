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

#keyboard reading ..not working for my version but should work with python 2.7
#keyword = input('give the keyword or subject')

#method to get tweets from the Twitter API
def get_tweets(subject):
    
    public_tweets = api.search(subject)
    list_tweets_text = []
    #list to store the text part of the tweet
    list_tweets_analysis = []
    for tweet in public_tweets:
        list_tweets_text.append(tweet.text)
        analysis = TextBlob(tweet.text)
        list_tweets_analysis.append(analysis.sentiment)
        
    results_tweets = [[x,str(y)] for x,y in zip(list_tweets_text , list_tweets_analysis)]
        
    return results_tweets



#method of storage tweets in a file
def storage_tweets(list_tweets , subjects):
    file = open(subjects , 'w' , encoding='utf-8')
    for tweets in list_tweets:
        file.writelines(tweets)
    
    file.close()
    

#list of few subjects
list_subjects = ['Dataiku' , 'streamroot']

#registration of the subjects in file
def registration(list_subjects):
    for subject in list_subjects:
        tweets = get_tweets(subject)
    
        storage_tweets(tweets , subjects = subject)
        
registration(list_subjects)

             
             





