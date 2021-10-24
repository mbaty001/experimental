import math

def blind_multiplication(base, exponent):
    '''' 
    blind multiplication(2, 500)
    real    0m0.022s
    user    0m0.012s
    sys     0m0.004s
    '''
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    return base * blind_multiplication(base, exponent-1)

def wise_multiplication(base, exponent):
    '''
    wise_multiplication(2, 1000000) 
    real    0m1.679s
    user    0m1.104s
    sys     0m0.020s
    '''
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1

    half = wise_multiplication(base, exponent//2)
    if exponent % 2 == 0:
        return  half*half
    else:
        return half*half*base
    
#print(blind_multiplication(2, 500))
print(wise_multiplication(2, 1000000))