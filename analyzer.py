#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import jieba

import jieba.analyse
import nltk


def analysis():
    lyric = []
    with open('resources/lyric/胡歌/胡歌.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            for t in line.split():
                lyric.append(t)
        text = jieba.analyse.extract_tags(f.read(), topK=20, withWeight=False, allowPOS=())
    parser = nltk.CoreNLPParser('http://localhost:9001')


if __name__ == '__main__':
    analysis()
