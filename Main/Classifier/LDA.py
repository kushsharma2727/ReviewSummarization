# -*- coding: utf-8 -*-
from gensim import corpora, models
import gensim
import codecs
import os

from HindiTokenizer import Tokenizer

# Restaurant-ID map: Map between restaurant and manually assigned ID
# ID - Aspect Map: For each restaurant, under each aspect, the sentences that are present: As positive and negative
#                   [id][aspect][sentiment] = [list of sentences]
#

def removeStopWords(list):
    f = codecs.open("stopwords.txt",encoding='utf-8')
    stopwords=[x.strip() for x in f.readlines()]
    tokens=[i for i in list if unicode(i) not in stopwords]
    return tokens

texts = []
documents = {}

for i in os.listdir("Reviews"):
    if i.endswith(".txt"):
        with open("Reviews\\"+i) as f:
            documents[i] = []
            for line in f:
                l = line.split('#####')[0]
                t = Tokenizer(l)
                t.generate_sentences()
                for s in t.sentences:
                    if not s.strip() == '':
                        documents[i].append(s)
                t.tokenize()
                tokens = removeStopWords(t.tokens)
                # qwe.extend(tokens)
                texts.append(tokens)
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
model = gensim.models.ldamodel.LdaModel(corpus, num_topics=9, id2word = dictionary, passes=100)
val = model.print_topics(num_topics=8, num_words=10)
print val
for value in val:
    a,b=value
    print b

# docs = ["यहाँ के कर्मचारी प्रशिक्षित नहीं है", "इस भोजनालय की सामान्य साफ़ सफाई पर भी मुझे संदेह है", "खाने का स्वाद अच्छा है पर इतने पैसों के लायक नहीं है", "इस स्थापना उत्कृष्ट है", "इस  जगह पर बहुत शोर  है", "मुझे वास्तव में इस जगह से प्यार करना चाहता था"]
# texts2 = []
# for doc in docs:
#     t = Tokenizer(doc)
#     t.tokenize()
#     tokens = removeStopWords(t.tokens)
#     texts2.append(tokens)
# new_corp = [dictionary.doc2bow(text) for text in texts2]
# topic_vec = model[new_corp]
#
# for j in range(len(topic_vec)):
#     max = -1
#     t = -1
#     for i in range(len(topic_vec[j])):
#         a, b = topic_vec[j][i]
#         if max == -1 or max < b:
#             max = b
#             t = i
#     print t

outputTokens = []
length = 0
for doc in documents:
    length += len(documents[doc])
    for sentence in documents[doc]:
        t = Tokenizer(sentence.encode('utf-8'))
        t.tokenize()
        outputTokens.append(removeStopWords(t.tokens))
corpus = [dictionary.doc2bow(text) for text in outputTokens]
topic_vec = model[corpus]
j = -1

directory = "op1"
if not os.path.exists(directory):
    os.makedirs(directory)
for doc in documents:
    f = open(directory+'\\'+doc, 'w')
    for sentence in documents[doc]:
        j += 1
        max = -1
        t = -1
        for i in range(len(topic_vec[j])):
            try:
                a, b = topic_vec[j][i]
                if max == -1 or max < b:
                    max = b
                    t = i
            except IndexError:
                print "i = " + str(i) + " j = " + str(j)
        f.write(sentence.encode('utf-8') + "#####" + str(t)+"\n")
    f.close()
print "length"
print length
print "Topics"
print len(topic_vec)
# print "count"
# print count