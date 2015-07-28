import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import csv
import random
import pickle

#Assume pos_tweets and neg_tweets are data sets that exist
pos_tweets = []
neg_tweets = []

f = open('trainingandtestdata/training.1600000.processed.noemoticon.csv')
csv_f = csv.reader(f)
for row in csv_f: 
  if row[0] == "0":
    neg_tweets.append((row[5], 'negative'))
  else:
    pos_tweets.append((row[5], 'positive'))


pos_tweets_filtered = random.sample(pos_tweets, 1000)
neg_tweets_filtered = random.sample(neg_tweets, 1000)


tweets = []
for (words, sentiment) in pos_tweets_filtered + neg_tweets_filtered:
  words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
  tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
  all_words = []
  for (words, sentiment) in tweets:
    all_words.extend(words)
  return all_words

def get_word_features(wordlist):
  wordlist = nltk.FreqDist(wordlist)
  word_features = wordlist.keys()
  return word_features

def extract_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
    features['contains(%s)' % word] = word in document_words
  return features

word_features = get_word_features(get_words_in_tweets(tweets))

#serialize word_features to be used for REST server
f = open('word_features.pickle', 'wb')
pickle.dump(word_features, f)
f.close()

cutoff = len(tweets)*3/4

training_set = nltk.classify.apply_features(extract_features, tweets[:cutoff])
test_set = nltk.classify.apply_features(extract_features,tweets[cutoff:])

#train classifier
classifier = NaiveBayesClassifier.train(training_set)
print 'train on %d instances, test on %d instances' % (len(training_set), len(test_set))

#serialize classifier to be used for REST server
f = open('classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()

print 'accuracy:', nltk.classify.util.accuracy(classifier, test_set)
classifier.show_most_informative_features()
