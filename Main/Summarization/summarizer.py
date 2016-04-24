from __future__ import division
from utility import tfidf, tokenize_docs, tf, filt_word, sents_stats
from collections import defaultdict
import math

class KLSum():

    def __init__(self):
        pass

    def greedy_sum(self, sentences):
        all_tokens, sents = sents_stats(sentences, filt_word)
        pd = tf(all_tokens)
        summary = []
        sum_freq = defaultdict(int)
        while len(summary) < 0.25 and len(sents) > 0:
            kl_vals = [self.KL(s, sum_freq, pd) for s in sents]
            min_idx = min((val, idx) for (idx, val) in enumerate(kl_vals))[1]
            #print(kl_vals[min_idx])
            sent = sents.pop(min_idx)
            if self.is_valid(sent):
                summary.append(sent)
                self.update_sum_freq(sum_freq, sent[1])
        return summary

    def KL(self, sentence, sum_freq, global_freq):
        sent_freq = sentence[1]
        kl_sum = 0
        for token in sent_freq:
            p = sum_freq[token] + sent_freq[token]
            q = global_freq[token]
            kl_sum += p * math.log(float(p) /float(q))
        return kl_sum

    def update_sum_freq(self, sum_freq, sen_freq):
        for t in sen_freq:
            sum_freq[t] += sen_freq[t]

    def is_valid(self, sentence):
        #print(sum(sentence[1].values()))
        return sum(sentence[1].values()) > 0 and len(sentence[0].split()) > 2

if __name__ == '__main__':
    handle1 = open("reviews.txt","r")
    docs=''
    while True:
        strline = handle1.readline()
        if not strline:
            break
        strline = strline.strip()
        docs+=strline.decode('utf-8')

    #from pymongo import MongoClient
    #db = MongoClient().yelp
    #reviews = db.review.find({"business_id": "2e2e7WgqU1BnpxmQL5jbfw"})
    #print reviews
    #docs = [d['text'] for d in reviews]
    #print docs
    #reviews = db.review.find({"business_id": "2e2e7WgqU1BnpxmQL5jbfw"})
    #ratings = [d for d in reviews]
    kl = KLSum()
    for i, s in enumerate(kl.greedy_sum(docs)):
        print(s[0])
        print '\n'
