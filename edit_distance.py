# -*- coding: utf-8 -*-
import numpy as np
import time


def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0 for __ in range(m + 1)] for __ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i
        # for i in range(n + 1):
        # print (dp[i])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            onemore = 1 if word1[j - 1] != word2[i - 1] else 0
            # print word1[:i], word2[:j]
            # print 'shanchu', dp[i - 1][j] + 1, 'charu', dp[i][j - 1] + 1, 'tihuan', dp[i - 1][j - 1] + onemore
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + onemore)
    return dp[n][m]


def min_edit_dist(word1, word2):
    len_1 = len(word1)
    len_2 = len(word2)
    x = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]  # the matrix whose last element ->edit distance
    for i in range(0, len_1 + 1):
        # initialization of base case values
        x[i][0] = i
        for j in range(0, len_2 + 1):
            x[0][j] = j
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if word1[i - 1] == word2[j - 1]:
                x[i][j] = x[i - 1][j - 1]
            else:
                x[i][j] = min(x[i][j - 1], x[i - 1][j], x[i - 1][j - 1]) + 1
    return x[i][j]


def retrieve_text(dictname,word1):
    # file = "Dictionary.txt"
    with open(dictname, 'r') as f:
        # ffile = open(file, 'r')
        lines = f.readlines()
        distance_list = []
        sugges = []
        correct = []
        # print(len(lines))
        for i in range(len(lines)):
            dist = minDistance(word1.lower(), lines[i].strip().lower())
            distance_list.append(dist)

        for j in range(len(lines)):
            if distance_list[j] == 0:
                correct.append(lines[j].strip())
                print('correct')
                return correct

            if distance_list[j] == 1:
                sugges.append(lines[j].strip())
                # print(lines[j])
                # print(" ")

    # ffile.close()
    print('建議近似字')
    return sugges

if __name__ == '__main__':
    Dictname = "Dictionary.txt"
    search_word = 'patteran'
    Sugges = retrieve_text(Dictname,search_word)
    print(Sugges)
