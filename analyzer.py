#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/9/2019 21:05
import re

import jieba
import matplotlib.pyplot as plt
import nltk
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS, wordcloud

# common sign
SIGN_PATTERN = r'[\s+.!/_,$%^*()"?<>:;\[\]\']+|[：\-+—=！，；“”|。？、~@#￥%…&*（）{}【】《》]'
# stop words
STOP_WORDS = {'陈奕迅', 'Eason', 'Chan', '曲', '词', '的', '在', '了', '是'}


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
        # take the most common x elements
        # lyric = nltk.FreqDist(lyric).most_common(200)
        # lyric = [i[0] for i in lyric]

        back_color = plt.imread('background.jpg')  # 解析该图片
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=200,  # 最大词数
                       mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=100,  # 显示字体的最大值
                       stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
                       font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                       random_state=42,  # 为每个词返回一个PIL颜色
                       # width=1000,  # 图片的宽
                       # height=860  #图片的长
                       )
        wc.generate(' '.join(lyric))
        # 基于彩色图像生成相应彩色
        image_colors = ImageColorGenerator(back_color)
        # 显示图片
        plt.imshow(wc.recolor(color_func=image_colors))
        # 关闭坐标轴
        plt.axis('off')
        plt.show()

        # 绘制词云
        plt.figure()
        plt.imshow(wc.recolor(color_func=image_colors))
        plt.axis('off')
        # 保存图片
        wc.to_file('wordcloud4.jpg')


if __name__ == '__main__':
    analysis()
