# -*- coding: utf-8 -*-
import numpy as np
import time
import pandas as pd

#載入字典為全域共用
Dictname = "Dictionary.txt"
f = open(Dictname, 'r')
dict_words = f.readlines()

def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    #初始化編輯距離陣列內容為0
    dp = [[0 for __ in range(m + 1)] for __ in range(n + 1)]
    # 初始化編輯距離xy邊界
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i
    #2個For迴圈 開始計算2個字串編輯距離
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #若比對字元不相等則cost設為1，相同則為0
            cost = 1 if word1[j - 1] != word2[i - 1] else 0
            #紀錄最小編輯距離於dp[i,j]
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    #列印編輯距離陣列計算後內容
    # list_col = list(' ' + word1)
    # list_index = list(' ' + word2)
    # pdp = pd.DataFrame(dp,index=list_index,columns=list_col)
    # print(pdp)
    #回傳本次計算2個字串最小編輯距離
    return dp[n][m]

def retrieve_text(word1, ed=2):
    #存放字典每個字串計算後與比對字串最小編輯距離
    distance_list = []
    #存放近似字 編輯距離>=1
    matrix = []
    for __ in range(ed):
        matrix.append([])

    for i in range(len(dict_words)):
        #先將字典取出之字串及欲比對之字串轉成小寫
        #及字典取出之字串換行符號刪除
        dist = minDistance(word1.lower(), dict_words[i].strip().lower())
        distance_list.append(dist)

    #當distance_list存在0時，代表字典內有相同的字串
    #若無則將編輯距離<=ed 對應的字典存於近似字的陣列中
    if min(distance_list) == 0:
        k = distance_list.index(min(distance_list))
        print('***字串與字典內容相符***')
        print(dict_words[k])
        return 'found word'
    else:
        for j in range(len(dict_words)):
            for i in range(ed):
                if distance_list[j] == i + 1:
                    matrix[i].append(dict_words[j].strip())

    print(' %s 建議近似字:' %(word1))
    for i in range(ed):
        print('編輯距離為: %s   數量: %s' % (str(i + 1), len(matrix[i])))
        print(matrix[i])

    return matrix

if __name__ == '__main__':
    # search_word為欲比對字串
    search_word = 'window'
    # search_word = 'goodmon'
    # med 如果單詞拼寫錯，列出其最近的單詞，其中計算的編輯距離小於或等於給定字典中的3，
    # 以編輯距離的升序列出單詞
    med = 3
    retrieve_text(search_word, med)
    # minDistance('kitten', 'sitting')
    # minDistance('distance', 'distance')
