# -*- coding: utf-8 -*-
import time
import re
from collections import Counter

# 21行python拼寫檢查器,程式開始
def words(text):
    return re.findall(r'\w+', text.lower())
    # findall函數作用（可查看用戶手冊）在這裏就是用來將txt中的每一個單詞進行分離，在返回一個字符串列表


WORDS = Counter(words(open('big.txt').read()))
# 這裏的WORDS就是一個無序的集合，裏面存儲的是K-V:K是單詞，V是單詞在txt中出現的次數。這個是由Count函數使得的

def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N
    # P這個函數是用來計算word這個詞在txt樣本中出現的概率，當word沒有出現過，WORDS[word]會返回0

def known(words):
    # known這個函數返回一個集合，集合的內容是即在words這個集合中，又在WORDS中的單詞
    return set(w for w in words if w in WORDS)

def edits1(word):
    # edits1函數的作用是返回對word這個單詞一次編輯後可能得到的所有結果的集合
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    # splits 在這裏就是由tuple組成的list，每一個tuple是word單詞的分解形式
    # 這裏面字符串索引得認真去研究一波，比如word[0:0]結果是空字符，word[aN:aN]結果也是很空字符
    deletes = [L + R[1:] for L, R in splits if R]
    # 這裏面的R如果是空字符，就判斷為False
    # deletes 在這裏的作用就是得到word刪掉一個字母的所有字符的集合
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    # transposes 在這裏的作用就是將word單詞中任意兩個字母調換一次位置後得到的所有單詞的集合
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    # replaces 在這裏的用途是將word單詞中刪掉一個字母後可能得到的單詞的集合
    inserts = [L + c + R for L, R in splits for c in letters]
    # inserts 在此處的作用是插入一個字母到word單詞中後可能得到的單詞的集合
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    # edits2函數的作用是返回對word這個單詞進行兩次編輯後可能得到的所有結果的集合
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def candidates(word):
    # candidates函數返回的內容：如果word在txt中出現過，則就返回word，如果沒有的話，就返回對word編輯一次後獲得的字符集中在txt中出現過的字符構成的集合，如果還是沒有的話就返回二次編輯的，如果二次編輯的也沒有的話，就返回word
    # 看了寫這個代碼的人的解釋，這個函數算是一個錯誤模型，用來保證所獲得的結果是比較可信的
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def correction(word):
    return max(candidates(word), key=P)

def spelltest(tests, verbose=True):
    start = time.time()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction( {} ) => {} ( {} ); except {} ( {} )'.format(wrong, w, WORDS[w], right, WORDS[right]))

    dt = time.time() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second'.format(good / n, n, unknown / n, n / dt))


def Testset(lines):
    return [(right, wrong) for (right, wrongs) in (line.split(':') for line in lines) for wrong in wrongs.split()]


if __name__ == '__main__':
    spelltest(Testset(open('spell-testset1.txt')))
