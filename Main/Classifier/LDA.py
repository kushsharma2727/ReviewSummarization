# -*- coding: utf-8 -*-
from gensim import corpora, models
import gensim
import codecs
import collections

from HindiTokenizer import Tokenizer

# Restaurant-ID map: Map between restaurant and manually assigned ID
# ID - Aspect Map: For each restaurant, under each aspect, the sentences that are present: As positive and negative
#                   [id][aspect][sentiment] = [list of sentences]
#

def removeStopWords(list):
    f=codecs.open("stopwords.txt",encoding='utf-8')
    stopwords=[x.strip() for x in f.readlines()]
    tokens=[i for i in list if unicode(i) not in stopwords]
    return tokens

texts = []
qwe = []
with open("hindiRevs.txt") as f:
    for line in f:
        l = line.split('#####')[0]
        t = Tokenizer(l)
        t.tokenize()
        freq = t.generate_freq_dict()
        print freq
        tokens = removeStopWords(t.tokens)
        qwe.extend(tokens)
        texts.append(tokens)
# counter = collections.Counter(qwe)
# for key in counter.iterkeys():
#     print key.encode('utf-8') + " " + str(counter[key])
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
model = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=1000)
val = model.print_topics(num_topics=20, num_words=20)
print val
for value in val:
    a,b=value
    print b

docs = ["यहाँ के कर्मचारी प्रशिक्षित नहीं है", "इस भोजनालय की सामान्य साफ़ सफाई पर भी मुझे संदेह है", "खाने का स्वाद अच्छा है पर इतने पैसों के लायक नहीं है", "इस स्थापना उत्कृष्ट है", "इस  जगह पर बहुत शोर  है", "मुझे वास्तव में इस जगह से प्यार करना चाहता था"]
texts2 = []
for doc in docs:
    t = Tokenizer(doc)
    t.tokenize()
    tokens = removeStopWords(t.tokens)
    texts2.append(tokens)
new_corp = [dictionary.doc2bow(text) for text in texts2]
topic_vec = model[new_corp]

for j in range(len(topic_vec)):
    max = -1
    t = -1
    for i in range(len(topic_vec[j])):
        a, b = topic_vec[j][i]
        if max == -1 or max < b:
            max = b
            t = i
    print t