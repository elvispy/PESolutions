#PE162
from time import perf_counter
t = perf_counter()


def H(n: int, bol: bool):
    '''This function returns the number of hexadecimal numbers
    with at most n digits, where the set of digits of the number
    has a cardinal intersection equal to 1 with the set {0, 1, A}.
    bol specifies if '0' is the digit present
    '''
    if n < 1:
        raise Exception("LolH")
    elif n == 1:
        if bol:
            return 0
        else:
            return 2
    else:
        res = 14 * H(n-1, bol)
        aux = pow(13, n-1)
        if bol:
            return res + aux
        else:
            return res + 2 * pow(13, n-1)
        

def G(n: int, bol: bool):
    '''This function returns the number of hexadecimal numbers
    with exactly n digits, where the set of digits of the number
    has a cardinal intersection equal to 2 with the set {0, 1, A}.
    bol specifies if '0' is the digit missing.
    '''
    if n < 2:
        raise Exception("LolG")
    elif n == 2:
        return 2
    else:
        res = 15 * G(n-1, bol)
        if bol:
            return res + H(n-1, False)
        else:
            return res + 2 * H(n-1, True) + H(n-1, False)
        
    

def F(n):
    '''This function returns the number of hexadecimal numbers
    with exactly n digits and with at least one 1, one 0 and one A.
    '''
    if n < 3:
        raise Exception("LolF")
    elif n == 3:
        return 4
    else:
        res = 16 * F(n-1)
        return res +  G(n-1, True) + G(n-1, False)

def final(N):
    '''This function returns the number of hexadecimal numbers
    with at most n digits and with at least one 1, one 0 and one A.
    (In hexadecimal)
    '''
    return hex(sum([F(i) for i in range(3, N+1)]))[2:].upper()


res = final(16)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
