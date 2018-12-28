# -*- coding: utf-8 -*-
import numpy as np
import time

Dictname = "Dictionary.txt"
f = open(Dictname, 'r')
dict_words = f.readlines()
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0 for __ in range(m + 1)] for __ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 1 if word1[j - 1] != word2[i - 1] else 0
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[n][m]

def retrieve_text(word1):
    distance_list = []
    sugges = []
    correct = []

    for i in range(len(dict_words)):
        dist = minDistance(word1.lower(), dict_words[i].strip().lower())
        distance_list.append(dist)

    for j in range(len(dict_words)):
        if distance_list[j] == 0:
            correct.append(dict_words[j].strip())
            print('correct')
            return correct
        if distance_list[j] == 1:
            sugges.append(dict_words[j].strip())

    print('建議近似字')
    return sugges
#相似度：1-1/Math.Max(“ivan1”.length,“ivan2”.length) =0.8
if __name__ == '__main__':

    search_word = 'patteran'
    Sugges = retrieve_text(search_word)
    print(Sugges)
