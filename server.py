#dependencies
from flask import Flask
from flask import request
import nltk
import pickle

# import trained NLTK classifier + word features
f = open('classifier.pickle')
classifier = pickle.load(f)
f.close()
f = open('word_features.pickle')
word_features = pickle.load(f)
f.close()

def extractFeatures(document):
  document_words = set(document)
  features = {}
  for word in word_features:
    features['contains(%s)' % word] = (word in document_words)
  return features

def determineSentiment(tweet):
  return 'Positive'

app = Flask(__name__)

#define RESTful endpoint for sentiment
@app.route('/sentiment')
def getSentiment():
  tweet = request.args['text']
  return classifier.classify(extract_features(tweet))

if __name__ == '__main__':
  app.run()
