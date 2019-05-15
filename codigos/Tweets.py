from __future__ import print_function
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
import tweepy
import csv

# If service instance provides API key authentication
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    # url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    iam_apikey='4bFuF68iqbLIJtcoJHGlDMIXe88GldQj4lXttUnkkN8C')

# input your credentials here
consumer_key = "WD6MNBdsjOSlEtOL6K7lSz3Jj"
consumer_secret = "javuS4bikNZtpDqwp98hoifI3LRcLl8Or0KPeEKbZ9SH3SxrXN"
access_token = "369120217-EX4KS3ObQfe1SSIYgoskjENt1cg7XNilamxvQbqK"
access_token_secret = "ttsdHxwATCOK4Eu2LMmxMVKkWfTto3zqQIPmfdVohXENU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('analise_de_dados.csv', 'a')

# Use csv Writer
csvWriter = csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="@dell", count=100000,
                           lang="pt",
                           since="2019-01-01").items():
    # service = NaturalLanguageUnderstandingV1(
    #     version='2018-03-16',
    #     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    #     # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #     username='YOUR SERVICE USERNAME',
    #     password='YOUR SERVICE PASSWORD')
    try:
        response = service.analyze(
            text=tweet.text,
            features=Features(sentiment=SentimentOptions())).get_result()

        print(tweet.created_at, tweet.text)
        print(response['sentiment']['document']['label'])

        csvWriter.writerow({response['sentiment']['document']['label'],
                            tweet.created_at,
                            tweet.text.encode('utf-8')})
    except:
        print('Não foi possivel analisar')
