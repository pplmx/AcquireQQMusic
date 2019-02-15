#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import jieba
import nltk

# common sign
SIGN_PATTERN = r'[\s+.!/_,$%^*()"?<>:;\[\]\']+|[：\-+—=！，；“”|。？、~@#￥%…&*（）{}【】《》]'
# stop words
STOP_WORDS = {'陈奕迅', 'Eason', 'Chan'}


def analysis():
    with open('resources/lyric/陈奕迅/陈奕迅.txt', 'r', encoding='utf-8') as f:
        # Stanford CoreNLP
        # to split chinese sentence to word
        # parser = nltk.corenlp.CoreNLPParser('http://localhost:9001')
        # lyric = list(parser.tokenize(f.read()))

        # jieba
        # return generator (text, start_idx, end_idx)
        lyric = jieba.tokenize(f.read())
        # return the list of tuple, so map it
        lyric = list(map(lambda x: x[0], lyric))

        # HanLP

        # 基础分词
        # basic_tokenizer = pyhanlp.JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")

        # 标准分词
        # pyhanlp.HanLP.segment('你好，欢迎在Python中调用HanLP的API')

        # 最短路径分词(速度快,几倍于 N-最短)
        # viterbi_segment = pyhanlp.JClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')
        # shortest_segment = viterbi_segment().enableCustomDictionary(
        #     False).enablePlaceRecognize(True).enableOrganizationRecognize(True)

        # N - 最短路径分词(效果好, 对命名实体识别能力强)
        # n_short_segment = pyhanlp.JClass('com.hankcs.hanlp.seg.NShort.NShortSegment')
        # n_shortest_segment = n_short_segment().enableCustomDictionary(False).enablePlaceRecognize(
        #     True).enableOrganizationRecognize(True)

        # filter common sign
        lyric = list(filter(lambda x: not re.match(SIGN_PATTERN, x), lyric))
        # filter single chinese word
        # lyric = list(filter(lambda x: len(x) > 1, lyric))
        # filter defined stop words
        lyric = [i for i in lyric if i not in STOP_WORDS]
        print(nltk.FreqDist(lyric).most_common(10))


if __name__ == '__main__':
    analysis()
