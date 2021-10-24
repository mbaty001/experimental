import random
import time

def most_common_number(int_list):
    '''
    very unefficient 
    we interate over the set then on the list - then using count
    '''
    max = -1
    max_el = None
    for el in set(int_list):
        if int_list.count(el) > max:
            max_el = el
            max = int_list.count(el)
    return max_el

def moda2(lista):
    zliczenia = dict()
    for i in range(len(lista)):
        try:
            zliczenia[lista[i]] += 1
        except KeyError:
            zliczenia[lista[i]] = 1
    maks = -1
    liczba_maks = -1
    for item in zliczenia.items():
        if item[1] > maks:
            liczba_maks = item[0]
            maks = item[1]
    return liczba_maks

def moda3(lista):
    '''' the winner '''
    zliczenia = dict()
    for i in range(len(lista)):
        try:
            zliczenia[lista[i]] += 1
        except KeyError:
            zliczenia[lista[i]] = 1
    maks = -1
    liczba_maks = -1
    for (co, ile) in zliczenia.items():
        if ile > maks:
            liczba_maks = co
            maks = ile
    return liczba_maks

def moda(lista):
    zliczenia = dict()
    for i in range(len(lista)):
        if lista[i] in zliczenia:
            zliczenia[lista[i]] += 1
        else:
            zliczenia[lista[i]] = 1
    maks = -1
    liczba_maks = -1
    for (co, ile) in zliczenia.items():
        if ile > maks:
            liczba_maks = co
            maks = ile
    return liczba_maks

a_list = []
for i in range(12138442):
    a_list.append(random.randint(0,100))
for f in (moda, moda2, moda3):
    start = time.time()
    print(f'{f}: {f(a_list)}')
    end = time.time()
    print(end-start)
