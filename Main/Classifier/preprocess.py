# -*- coding: utf-8 -
import re
import os
# import time
# start_time = time.time()
# dir = "F:\CSCI 544 NLP\NLP Project\Code\doc2vec\\aclImdb\\train\\unsup\\"
# op = open('train-unsup.txt', 'w')
# for i in os.listdir(dir):
#     with open(dir+i) as f:
#         for line in f:
#             line = line.replace('.', '')
#             line = line.replace('!', '')
#             line = line.replace(',', '')
#             line = line.replace('*', '')
#             line = line.replace('\"', '')
#             line = line.replace('\'', '')
#             line = line.replace('<br />', '')
#             line = line.lower()
#             op.write(line+"\n")
# op.close()
# print time.time() - start_time

def cleanText(text):
    text = text.decode('utf-8')
    text=re.sub(r'(\d+)',r'',text)
    text=text.replace(u',','')
    text=text.replace(u'"','')
    text=text.replace(u'(','')
    text=text.replace(u')','')
    text=text.replace(u'"','')
    text=text.replace(u':','')
    text=text.replace(u"'",'')
    text=text.replace(u"‘‘",'')
    text=text.replace(u"’’",'')
    text=text.replace(u"''",'')
    text=text.replace(u".",'')
    text=text.replace(u"।",'')
    text=text.replace(u"\\",'')
    text=text.replace(u"!",'')
    text=text.replace(u"~",'')
    text=text.replace(u"/",'')
    return text

posReviews = []
negReviews = []
testPosReviews = []
testNegReviews = []
dir = "F:\CSCI 544 NLP\NLP Project\Code\doc2vec\HindiReviews\\Train\\"
for i in os.listdir(dir):
    with open(dir+i) as f:
        for line in f:
            l = line.split("#####")
            if int(l[1]) > 3:
                posReviews.append(cleanText(l[0]))
            else :
                negReviews.append(cleanText(l[0]))

dir = "F:\CSCI 544 NLP\NLP Project\Code\doc2vec\HindiReviews\\Test\\"
for i in os.listdir(dir):
    with open(dir+i) as f:
        for line in f:
            line = line.decode('utf-8')
            l = line.split(u"।")
            tag = l[1].split('##')
            if tag[0].strip() == 'POSITIVE':
                testPosReviews.append(cleanText(l[0].encode('utf-8')))
            else :
                testNegReviews.append(cleanText(l[0].encode('utf-8')))


op = open('train-pos-hindi.txt', 'w')
for review in posReviews:
    op.write(review.encode('utf-8')+"\n")
op.close()

op = open('train-neg-hindi.txt', 'w')
for review in negReviews:
    op.write(review.encode('utf-8')+"\n")
op.close()

op = open('test-pos-hindi.txt', 'w')
for review in testPosReviews:
    op.write(review.encode('utf-8')+"\n")
op.close()

op = open('test-neg-hindi.txt', 'w')
for review in testNegReviews:
    op.write(review.encode('utf-8')+"\n")
op.close()