#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
import json
import string

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

# Beginning of Application    
def applyMultinomialNB(inHand, outHand):
    # Reading one line at a time from inHandle
    for review in inHand:
        review = review.decode('utf-8').strip()
        review   = clean_text(review)
        print review
        review   = review.split()
        review   = [x for x in review if not x in stopWords]
        score    = dict()
        # Calculating contribution of each word for each class
        for c in ['Positive', 'Negative']:
            # We start with Prior
            score[c] = math.log(database[c][0])
            # Add the weights (evidence) added by each word
            for word in review:
                try:
                    score[c] += math.log(database[c][1][word])
                except KeyError:
                    pass
        # All weights have been calculated for each class.
        # Identifying the class Now.
        maxKey, maxValue = None, None
        for key, value in score.items():
            if maxValue == None or value > maxValue:
                maxKey = key
                maxValue = value
        # End of computing class.
        # Copy this result into output file.
        print maxKey
#End of Application 
       
testFile = sys.argv[1]
fname = 'nboutput.txt'
inHandle  = open(testFile, 'r')
outHandle = open(fname, 'w')
# Load StopWords into memory
getStopWords()
# Load learnt model into memory
database = json.load(open('nbmodel.txt', 'r'))
'''
for key in database:
    for word in database[key][1]:
        print word, database[key][1][word]
'''
applyMultinomialNB(inHandle, outHandle)