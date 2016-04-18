#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
import json
import os
import glob

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
def applyMultinomialNB(path):
    aspects = ['Food', 'Service', 'Value', 'Ambience']
    sentiments = ['Positive', 'Negative']
    # One directory have one file. So this is fine.
    fname = glob.glob(path + '*.txt')[0]
    # Open restaurant file for reading.
    inHand = open(fname, 'r')
    out    = dict()
    # directories and files.
    for aspect in aspects:
        dirpath = path + aspect
        os.makedirs(dirpath)
        for sentiment in sentiments:
            filepath = dirpath + '/' + sentiment + '.txt'
            fhand    = open(filepath, 'w')
            out[filepath] = fhand

    # Reading one line at a time from inHandle
    for line in inHand:
        line = line.decode('utf-8').strip()
        line = clean_text(line)
        line = line.split('#####')
        review = line[0]
        aspect = line[1]
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
        # Copy this result into output file.
        # name of the output file = path + aspect + maxKey
        outFile = path + aspect + '/' + maxKey + '.txt'
        # File handle corresponding to this file.
        fhand = out[outFile]
        fhand.write(review)

    # Closing all the open files.
    inHand.close()
    for fname in out:
        fhand = out[fname]
        fhand.close()

#End of Application 
       
path = sys.argv[1]
# Load StopWords into memory
getStopWords()
# Load learnt model into memory
database = json.load(open('nbmodel.txt', 'r'))
'''
for key in database:
    for word in database[key][1]:
        print word, database[key][1][word]
'''
applyMultinomialNB(path)