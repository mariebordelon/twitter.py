



import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
lst = []
pol = []

tweetfile = open("tweets_small.json", "r")

tweetData = json.load(tweetfile)

tweetfile.close()

sum = 0

for x in range(len(tweetData)):
    lst.append(TextBlob(tweetData[x]["text"]))
    sum += TextBlob(tweetData[x]["text"]).polarity

print(sum)

for x in range(len(tweetData)):

    lst.append(TextBlob(tweetData[x]["text"]))
    pol.append(TextBlob(tweetData[x]["text"]).polarity)

print(pol)
