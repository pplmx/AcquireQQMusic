#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import imageio
import jieba
import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud

# show Chinese word.
plt.rcParams['font.sans-serif'] = ['SimHei']
# show plus and minus sign.
plt.rcParams['axes.unicode_minus'] = False

# common sign.
SIGN_PATTERN = r'[\s+.!/_,$%^*()"?<>:;\[\]\']+|[：\-+—=！，；“”|。？、~@#￥%…&*（）{}【】《》]'
# stop words
STOP_WORDS = {'陈奕迅', 'Eason', 'Chan', 'Eric', '黄伟文', 'Live',
              '曲', '词', '的', '在', '了', '是', '都', '也', '这',
              '要', '有', '人', '再', '就', '不', '着', '会', '到',
              '让', '多', '又'}


def draw_bar2(data: list, x_desc: str, y_desc: str, title: str, data2=None):
    """
        draw histogram based on word frequency
    :param data: such as [('没有', 872), ('一个', 675), ('什么', 580)]
    :param x_desc: to describe x axis info
    :param y_desc: to describe y axis info
    :param title:
    :param data2: control group, like as data
    :return:
    """
    # create histogram
    plt.bar(range(len(data)), [i[1] for i in data],
            facecolor='#9999ff', align='center')
    plt.bar(range(len(data2)), [-i[1] for i in data2],
            facecolor='#ff9999', align='center')

    # set x axis
    plt.xticks(range(len(data)), [i[0] for i in data])

    # set x axis desc
    plt.xlabel(x_desc)

    # set y axis desc
    plt.ylabel(y_desc)

    # set title
    plt.title(title)

    # show
    plt.show()


def draw_bar(data: list, x_desc: str, y_desc: str, title: str, data2=None):
    """
        draw histogram based on word frequency
    :param data: such as [('没有', 872), ('一个', 675), ('什么', 580)]
    :param x_desc: to describe x axis info
    :param y_desc: to describe y axis info
    :param title:
    :param data2: control group, like as data
    :return:
    """
    # create histogram
    plt.bar(range(len(data)), [i[1] for i in data], align='center')
    if data2 is not None:
        # like [1, 3, 5] and [a, b, c], merged into [1, a, 3, b, 5, c]
        if len(data) == len(data2):
            temp = []
            for idx, val in enumerate(data):
                temp.append(val)
                temp.append(data2[idx])
            data = temp
    plt.bar(range(len(data)), [i[1] for i in data], align='center')

    # set x axis
    plt.xticks(range(len(data)), [i[0] for i in data])

    # set x axis desc
    plt.xlabel(x_desc)

    # set y axis desc
    plt.ylabel(y_desc)

    # set title
    plt.title(title)

    # show
    plt.show()


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
        lyric2 = list(filter(lambda x: len(x) == 1, lyric))
        lyric = list(filter(lambda x: len(x) > 1, lyric))
        # filter defined stop words
        lyric = [i for i in lyric if i not in STOP_WORDS]
        lyric2 = [i for i in lyric2 if i not in STOP_WORDS]
        # take the most common elements
        # [('没有', 872), ('一个', 675), ('什么', 580)]
        lyric = nltk.FreqDist(lyric).most_common()
        lyric2 = nltk.FreqDist(lyric2).most_common()
        draw_bar(lyric[:10], x_desc='The Most Frequent Words', y_desc='Words Frequency', title='Words Frequency', data2=lyric2[:10])
        print(len(lyric))
        # filter somewhat frequency is not very high
        lyric = list(filter(lambda tup: tup[1] > 10, lyric))
        print(len(lyric))

        back_color = imageio.imread('Saber1.jpg')  # 解析该图片
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=1000,  # 最大词数
                       mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=1000,  # 显示字体的最大值
                       stopwords=set(),  # 使用内置的屏蔽词，再添加'苟利国'
                       font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                       random_state=42,  # 为每个词返回一个PIL颜色
                       width=3840,  # 图片的宽
                       height=2160  # 图片的长
                       )
        wc.generate_from_frequencies(dict(lyric))
        # save wordcloud
        wc.to_file('Saber1-wc.jpg')


if __name__ == '__main__':
    analysis()
