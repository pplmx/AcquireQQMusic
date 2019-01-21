#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import jieba
import nltk
import pyhanlp

# common sign
SIGN_PATTERN = r'[\s+.!/_,$%^*()"?<>:;\[\]\']+|[：\-+—=！，；“”|。？、~@#￥%…&*（）{}【】《》]'
# stop words
CHINESE_STOP_WORDS = ['的', '地']


def analysis():
    parser = nltk.corenlp.CoreNLPParser('http://localhost:9001')
    with open('resources/lyric/木小雅/木小雅.txt', 'r', encoding='utf-8') as f:
        # to split chinese sentence to word
        lyric = list(parser.tokenize(f.read()))
        # filter common sign
        lyric = list(filter(lambda x: not re.match(SIGN_PATTERN, x), lyric))
        # word frequency
        result = nltk.FreqDist(lyric)
        print(result.most_common(10))
        jieba.tokenize(f.read())
        naive_bayes_classifier = pyhanlp.JClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
        naive_bayes_classifier = pyhanlp.SafeJClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
        naive_bayes_classifier = pyhanlp.LazyLoadingJClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
        print(pyhanlp.HanLP.segment('你好，欢迎在Python中调用HanLP的API'))


if __name__ == '__main__':
    analysis()
