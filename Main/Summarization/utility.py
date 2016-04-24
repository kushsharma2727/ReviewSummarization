#!/usr/bin/env python3
import sys
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
import re
import math
from setting import Setting


def progressbar(it, prefix="", size=30, count=None):
    if count is None:
        count = len(it)
    if count == 0:
        count = 1

    def _show(_i):
        x = int(size * _i / count)
        sys.stdout.write("%s[%s%s] %i/%i\r" %
                         (prefix, "#" * x, "." * (size - x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()


def dsum(dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return ret


def filt_word_alpha(word):
    if word.lower() in stop_words:
        return False
    return word.isalpha()


def filt_word(word):
    if word.lower() in stop_words:
        return False
    if re.sub('[^0-9a-zA-Z]+', ' ', word) == ' ':
        return False
    return True


def process_word(word):
    return re.sub('[0-9]+', '9', word)


def pos_tag_text(text):
    sentences = sent_tokenize(text)
    sents = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        text = [word for word in tokens]
        tagged_text = nltk.pos_tag(text)
        sents.append({'tokenized': [{'word': word, 'pos': tag}
                                    for word, tag in tagged_text], 'raw': sentence})
    return sents


def tokenize_text(text, doc_idx, word_filter=lambda x: True):
    tokens = []
    sents = sent_tokenize(text)
    tokenized_sents = []
    for i, s in enumerate(sents):
        words = [w for w in word_tokenize(s) if word_filter(w)]
        tokens.extend(words)
        tokenized_sents.append((s, FreqDist(words), doc_idx, i))
    return tokens, tokenized_sents


def tokenize_docs(docs, word_filter=lambda x: True):
    all_tokens = []
    token_sets = []
    sentences = []
    for i, doc in enumerate(docs):
        tokens, sents = tokenize_text(doc, i, word_filter)
        sentences.extend(sents)
        all_tokens.extend(tokens)
        token_sets.extend(set(tokens))
    return all_tokens, token_sets, sentences


def sents_stats(sents, word_filter=lambda x: True):
    tokenized_sents = []
    tokens = []
    for i, s in enumerate(sent_tokenize(sents)):
        words = word_tokenize(s)
        tokens.extend(words)
        tokenized_sents.append((s, FreqDist(words)))
    return tokens, tokenized_sents


def tf(all_tokens, *args):
    return FreqDist(all_tokens)


def tfidf(all_tokens, token_sets, doc_count, *args):
    tf, id_count = FreqDist(all_tokens), FreqDist(token_sets)
    tfidf = {}
    for w in tf:
        tfidf[w] = tf[w] * math.log((doc_count + 1) / (FreqDist[w] + 1))
    return tfidf


def extract_stop_words(token_cursor):
    result = []
    stop_set = stopwords.words('english')
    for t in token_cursor.limit(300):
        if t['_id'] not in stop_set:
            result.append(t['_id'])
    return sorted(result)


def read_stop_words():
    words = set()
    with open(Setting.STOP_WORD_PATH, 'r') as f:
        for line in f:
            words.add(line.strip())
    return words


def read_topic_dict(path):
    topic_dict = {}
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            item = line.strip()
            if len(item) > 0 and item != 'unknown':
                topic_dict[i] = item
    return topic_dict


def select_topics(topics, topic_dict):
    result = set()
    for t in topics:
        if t[0] in topic_dict and t[1] > 0.2:
            result.add(topic_dict[t[0]])
    return result

stop_words = set(stopwords.words('english')) | read_stop_words()

word_filters = [filt_word, filt_word_alpha]

word_processors = [lambda x: x, process_word]

if __name__ == '__main__':
    print(stop_words)
