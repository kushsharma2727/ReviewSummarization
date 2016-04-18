#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import glob

if len(sys.argv) != 2: exit(0)
stopWords = dict()

# Beginning of getStopWords
def getStopWords():
    ''' Read stopwords from stopWords.txt in current directory.
        It creates a dictionary for faster reading.
    '''
    fname = 'stopWords.txt'
    fhand = open(fname, 'r')
    for word in fhand:
        word = word.decode('utf-8')
        word = word.strip()
        stopWords[word] = None
# End of getStopWords
        
# Beginning of clean_text
def clean_text(text):
    ''' Doing what string.translate should do '''  
    text=text.replace(u"।", '')
    text=text.replace(u'\\ ','')
    text=text.replace(u'! ','')
    text=text.replace(u'@ ','')
    text=text.replace(u',','')
    text=text.replace(u'"','')
    text=text.replace(u'(','')
    text=text.replace(u')','')
    text=text.replace(u'"','')
    text=text.replace(u"'",'')
    text=text.replace(u"‘‘",'')
    text=text.replace(u"’’",'')
    text=text.replace(u"''",'')
    text=text.replace(u".",'')
    return text
# End of clean text

# Beginning of extract Vocab
def extractVocab(path):
    ''' Dictionary of all the words in the history.'''  
    V  = dict()
    N  = 0
    NC = dict()
    rating = None
    docs = glob.glob(path + '*.txt')
    for fname in docs:
        fhand = open(fname, 'r')
        # We are reading from one line here.
        for line in fhand:
            line   = line.decode('utf-8').strip()
            # We are only going to have one match which is expected to be integer.
            line   = line.split('#####')
            rating = int(line[1])
            review = line[0]
            review   = clean_text(review)
            review   = review.split()
            review   = [x for x in review if not x in stopWords]
            for word in review:
                V[word] = V.get(word, 0)
            if rating > 3:
                label = 'Positive'
            else:
                label = 'Negative'
            # Will help find total number of reviews for this class.
            NC[label] = NC.get(label, 0) + 1
        # End of Reading one file. Ok to close that file.
        fhand.close()
    # Total of all reviews.
    N = sum(NC.values())
    return V, N, NC
# End of extractVocab

# Beginning of counting frequency
def countTokenInClass(textC, path, category = 'Positive'):
    '''Frequency of words calculation for given class '''
    result = 0
    docs = glob.glob(path + '*.txt')
    for fname in docs:
        fhand = open(fname, 'r')
        # We are reading from one line here.
        for line in fhand:
            line   = line.decode('utf-8').strip()
            line   = line.split('#####')
            rating = int(line[1])
            if category == 'Positive' and rating < 4:
                continue
            if category == 'Negative' and rating > 3:
                continue
            review = line[0]
            review   = clean_text(review)
            review   = review.split()
            review   = [x for x in review if not x in stopWords]
            for text in review:
                result += 1
                textC[text] = textC.get(text, 0) + 1
        # End of reading file
        fhand.close()
    # End of reading all files.
    return result
# End of counting frequency

# Beginning of Traning
def train(path):
    ''' Traning Bayes model. Main function '''

    V, N, NC = extractVocab(path)
    for label in ['Positive', 'Negative']:
        # Prior of label
        prior = float(NC[label]) / N
        textC = V.copy()
        # List of all tokens in label class and their frequency
        Tct   = countTokenInClass(textC, path, label)
        # Probability Calculation and Smoothing
        for text in textC:
            textC[text] = float(textC[text] + 1) / (Tct + len(V))
        # Updating the result into final database
        database[label] = (prior, textC)
    # End of counting for all classes
    '''
    for key in database:
        for word in database[key][1]:
            print word, database[key][1][word]
    '''

# End of Training

# Get the list of stopWords
getStopWords()
# Dealing with only two types of classes here.
database = {'Positive' : {}, 'Negative' : {}}
# File name to read all the data. Only one file this time.
path    = sys.argv[1]
train(path)
# Dumping dictionary in nbmodel.txt
json.dump(database, open('nbmodel.txt', 'w'))