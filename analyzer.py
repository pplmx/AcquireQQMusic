#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import jieba

import jieba.analyse
from nltk.parse import corenlp


def analysis():
    lyric = []
    with open('resources/lyric/木小雅/木小雅.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line == 'NextSong2start':
                continue
            for t in line.strip().split():
                lyric.append(t)
        text = jieba.analyse.extract_tags(f.read(), topK=20, withWeight=False, allowPOS=())
    parser = corenlp.CoreNLPParser('http://localhost:9001')
    parser.tokenize(lyric)


if __name__ == '__main__':
    analysis()
