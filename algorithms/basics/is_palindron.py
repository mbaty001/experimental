def is_palindron(word):
    '''
    watch out - word[::-1] - creates a new object in memory
    in case of long words we need the same number of memory 
    '''
    return word == word[::-1]

def is_palindron2(word):
    ''' 
    it is slower about 100 times than is_palindron when we compare all the letters
    it is faster about 100 times than is_palindron when it is not palindron by checkking first letter
    '''
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n-i-1]:
            return False
    return True

for word in ('anna', 'kajak', 'krzysztof'):
    print (f'{word}: {is_palindron(word)}')
    print (f'{word}: {is_palindron2(word)}')
