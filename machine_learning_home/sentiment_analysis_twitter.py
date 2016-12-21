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

#keybard reading ..not wrking for my version but should work with python 2.7
#keyword = input('give the keyword or subject')




public_tweets = api.search('streamroot')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)





