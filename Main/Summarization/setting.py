#!/usr/bin/env python3


class Setting():

    def __init__(self):
        pass

    STOP_WORD_PATH = 'stopwords.txt'

    LDA_MODEL_PATH = '../model/lda_all_q.mm'

    LDA_DICT_PATH = '../model/lda_all_q.dict'

    LDA_TOPIC_NUM = 50

    LDA_WORD_FILTER = 0

    LDA_WORD_PROCESSOR = 0

    PRONOUNS = ['it', 'they']

    TOPIC_DICT_PATH = '../model/topic_dict_q.txt'
