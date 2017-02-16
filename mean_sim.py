#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys 
 
# 学習済みモデルのロード
model = word2vec.Word2Vec.load_word2vec_format("./word2vec/contents_wakati.bin", binary=True)
 
# 入力された単語から近い単語をn個表示する
def s(word1, word2, n=30):
    cnt = 1 # 表示した単語の個数カウント用
    # 学習済みモデルからcos距離が最も近い単語n個(topn個)を表示する
    result = model.similar_by_vector((model[word1] + model[word2]) / 2, topn = n)
    for r in result:
        print cnt,'　', r[0],'　', r[1]
        cnt += 1
 
if __name__ == '__main__':
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    word1 = unicode(word1, 'utf-8')
    word2 = unicode(word1, 'utf-8')
    s(word1, word2)
