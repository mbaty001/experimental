import time
import random
import string

def is_anagram1(word1, word2):
    '''
    looks elegenat but we are creatig new objects, may be a problem with long words
    '''
    return sorted(word1) == sorted(word2)

def is_anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    chars1 = {}
    chars2 = {}
    for char in set(word1):
        chars1[char] = word1.count(char)
    for char in set(word2):
        chars2[char] = word2.count(char)

    return chars1 == chars2

def czyAnagram(napis1, napis2):
    n = len(napis1)
    if n != len(napis2):
        return False
    slownik1 = dict()
    slownik2 = dict()
    for i in range(n):
        if napis1[i] in slownik1:
            slownik1[napis1[i]] += 1
        else:
            slownik1[napis1[i]] = 1
        if napis2[i] in slownik2:
            slownik2[napis2[i]] += 1
        else:
            slownik2[napis2[i]] = 1
    return slownik1 == slownik2


word1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1024554))
for f in (is_anagram1, is_anagram2, czyAnagram):
    start = time.time()
    print(f'{f}: {f(word1, word1)}')
    end = time.time()
    print(end - start)

''''
<function is_anagram1 at 0x7f3310f45550>: True
0.510333776473999
<function is_anagram2 at 0x7f3310eff0d0>: True
0.14369511604309082
<function czyAnagram at 0x7f3310ecb5e0>: True
0.8148620128631592
'''
    