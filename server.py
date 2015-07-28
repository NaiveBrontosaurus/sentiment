#dependencies
from flask import Flask
from flask import request
from flask import jsonify
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import pickle

# import trained NLTK classifier + word features
f = open('classifier.pickle')
classifier = pickle.load(f)
f.close()
f = open('word_features.pickle')
word_features = pickle.load(f)
f.close()

def extract_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
    features['contains(%s)' % word] = (word in document_words)
  return features

app = Flask(__name__)

#define RESTful endpoint for sentiment
@app.route('/sentiment')
def getSentiment():
  tweet = request.args['text']
  response = classifier.classify(extract_features(tweet.split()))
  return jsonify(sentiment=response)

if __name__ == '__main__':
  app.run()
