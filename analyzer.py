#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import jieba

import jieba.analyse


def analysis():
    lyric = []
    with open('resources/lyric/胡歌/胡歌.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            for t in line.split():
                lyric.append(t)
        text = jieba.analyse.extract_tags(f.read(), topK=20, withWeight=False, allowPOS=())
    print(text)
    # frequent = nltk.FreqDist(lyric)
    # for key, val in frequent.items():
    #     print('%s=======%s' % (key, val))
    # frequent.plot(20, cumulative=False)


if __name__ == '__main__':
    analysis()
