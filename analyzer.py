#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import nltk
from nltk.corpus import stopwords
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
        stoplist = stopwords.words('english')
        print(lyric)
        result = nltk.FreqDist(lyric)
        print(result.most_common(10))


if __name__ == '__main__':
    analysis()
