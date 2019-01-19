#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import jieba
import nltk
from nltk.parse import corenlp

# common sign
SIGN_PATTERN = r'[\s+.!/_,$%^*()"?<>:;\[\]\']+|[：\-+—=！，；“”|。？、~@#￥%…&*（）{}【】《》]'
# stop words
CHINESE_STOP_WORDS = ['的', '地']


def analysis():
    parser = corenlp.CoreNLPParser('http://localhost:9001')
    with open('resources/lyric/木小雅/木小雅.txt', 'r', encoding='utf-8') as f:
        # to split chinese sentence to word
        lyric = list(parser.tokenize(f.read()))
        # filter common sign
        lyric = list(filter(lambda x: not re.match(SIGN_PATTERN, x), lyric))
        # word frequency
        result = nltk.FreqDist(lyric)
        print(result.most_common(10))
        jieba.tokenize(f.read())


if __name__ == '__main__':
    analysis()
