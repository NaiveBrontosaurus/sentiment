#dependencies
from flask import Flask
from flask import request
import nltk
import pickle

#import trained NLTK classifier
# f = open('classifier.pickle')
# classifier = pickle.load(f)
# f.close()

def determineSentiment(tweet):
  return 'Positive'

app = Flask(__name__)

#define RESTful endpoint for sentiment
@app.route('/sentiment')
def getSentiment():
  tweet = request.args['text']
  return determineSentiment(tweet)

if __name__ == '__main__':
  app.run()
