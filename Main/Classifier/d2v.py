# -*- coding: utf-8 -*-
# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec

# numpy
import numpy

# random
from random import shuffle

# classifier
from sklearn.linear_model import LogisticRegression

class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources

        flipped = {}

        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')

    def __iter__(self):
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    yield LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])

    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    self.sentences.append(LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences

sources = {'train-pos-hindi.txt':'TRAIN_POS', 'train-neg-hindi.txt':'TRAIN_NEG', 'test-pos-hindi.txt':'TEST_POS', 'test-neg-hindi.txt':'TEST_NEG'}
sentences = LabeledLineSentence(sources)

model = Doc2Vec(min_count=1, window=10, size=10, sample=1e-4, negative=5, workers=2)
model.build_vocab(sentences.to_array())
print "Starting"
for epoch in range(10):
    model.train(sentences.sentences_perm())
    print str(epoch) + " Down"

train_pos_len = 0
train_neg_len = 0
test_pos_len = 0
test_neg_len = 0
for sentence in sentences.to_array():
    if str(sentence[1]).__contains__('TRAIN_POS'):
        train_pos_len += 1
    elif str(sentence[1]).__contains__('TRAIN_NEG'):
        train_neg_len += 1
    elif str(sentence[1]).__contains__('TEST_POS'):
        test_pos_len += 1
    elif str(sentence[1]).__contains__('TEST_NEG'):
        test_neg_len += 1
train_arrays = numpy.zeros((train_pos_len+train_neg_len, 10))
train_labels = numpy.zeros(train_pos_len+train_neg_len)

posCount = 0
negCount = 0
i = 0
for sentence in sentences.to_array():
    if str(sentence[1]).__contains__('TRAIN_POS'):
        prefix_train_pos = 'TRAIN_POS_' + str(posCount)
        posCount += 1
        train_arrays[i] = model.docvecs[prefix_train_pos]
        train_labels[i] = 1
        i+=1
    elif str(sentence[1]).__contains__('TRAIN_NEG'):
        prefix_train_neg = 'TRAIN_NEG_' + str(negCount)
        negCount += 1
        train_arrays[i] = model.docvecs[prefix_train_neg]
        train_labels[i] = 0
        i+=1

classifier = LogisticRegression()
classifier.fit(train_arrays, train_labels)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, penalty='l2', random_state=None, tol=0.0001)

test_arrays = numpy.zeros((test_pos_len+test_neg_len, 10))
test_labels = numpy.zeros(test_pos_len+test_neg_len)

posCount = 0
negCount = 0
i = 0
for sentence in sentences:
    if str(sentence[1]).__contains__('TEST_POS'):
        prefix_test_pos = 'TEST_POS_' + str(posCount)
        posCount += 1
        test_arrays[i] = model.docvecs[prefix_test_pos]
        test_labels[i] = 1
        i += 1
    elif str(sentence[1]).__contains__('TEST_NEG'):
        prefix_test_neg = 'TEST_NEG_' + str(negCount)
        negCount += 1
        test_arrays[i] = model.docvecs[prefix_test_neg]
        test_labels[i] = 0
        i += 1

print classifier.score(test_arrays, test_labels)