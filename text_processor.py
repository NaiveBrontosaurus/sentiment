import csv

f = open('pos_tweets.csv', 'rU')
csv_f = csv.reader(f)

pos_tweets = []
for row in csv_f:
  pos_tweets.append(row[0])

import re
import string

removeRT = []

for tweet in pos_tweets:
  if not 'RT' in tweet and not 'free' in tweet and not 'FREE' in tweet:
    removeRT.append(tweet)

removePunctuation = []

for tweet in removeRT:
  removePunctuation.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split()))

removeSmallWords = []

for tweet in removePunctuation:
  newTweet = ' '.join(word for word in tweet if len(word)>3)
  removeSmallWords.append(newTweet)


print len(removeSmallWords)
removeSmallWords = sorted(set(removeSmallWords))

import random 

randomProcessed = random.sample(removePunctuation, 20000)

text_file = open('output.txt', 'w')
for tweet in randomProcessed:
  text_file.write(tweet + '\n')
text_file.close()


