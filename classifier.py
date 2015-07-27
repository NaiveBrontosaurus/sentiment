import csv 
def loadCsv(filename):
  lines = csv.reader(open(filename, "rb"))
  dataset = list(lines)
  for i in range(len(dataset)):
    dataset[i] = [x for x in dataset[i]]
  return dataset

filename = 'trainingandtestdata/training.1600000.processed.noemoticon.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows').format(filename, len(dataset))

import random 
def splitDataset(dataset, splitRatio):
  trainSize = int(len(dataset) * splitRatio)
  trainSet = []
  copy = list(dataset)
  while len(trainSet) < trainSize: 
    index = random.randrange(len(copy))
    trainSet.append(copy.pop(index))
    return [trainSet, copy]
