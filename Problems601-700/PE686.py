#PE686
from time import perf_counter
t = perf_counter()
import mpmath as mp
mp.mp.pretty = True
mp.mp.prec = 1000
#mp.mp.dps = 1000



def mcd(a, b):
    c = a%b
    if c == 0:
        return b
    else:
        return mcd(max(c, b), min(c, b))



def add_approximators(N, C):
    '''
    This function will add all approximators with denominator less than N
    and that are coprime with its numerator 
    '''

    approximators = []

    treshold = mp.log10(mp.mpf(124)/mp.mpf(123))
    for i in range(10, N):
        chute = mp.floor(i * C)

        if mp.absmax(chute/i-C) >= mp.absmax((chute+1)/i - C):
            chute +=1

        if mcd(chute, i) == 1:
            val = mp.frac(i * C)
            if val < treshold:
                approximators.append((i, val))
            elif val > 1-treshold:
                approximators.append((i, val - 1))

    return approximators
            


def p(L, n):

    C = mp.log10(2)
    po = mp.mp.power(10, mp.floor(mp.log10(L)))
    C1 = mp.log10(mp.mpf(L)/po)
    C2 = mp.log10(mp.mpf(L+1)/po)
    k = 1

    while not (C1 <= mp.frac(k * C) < C2):
        k+=1
        auxi = lambda k: mp.frac(k * C) - C1


    approximators = add_approximators(1000, C)
    curr = (k, auxi(k))
    treshold = mp.log10(mp.mpf(L+1)/mp.mpf(L))
    idx = 1
    while idx < n:
        for el in approximators:
            if 0<= curr[1] + el[1] < treshold :
                
                curr = (curr[0] + el[0], auxi(curr[0] + el[0]))
                idx+=1
                #print(curr[0], idx)
                break
    return curr[0]


def brute_force(N):
    '''
    Just to test the actual function
    '''
    k = 1
    idx = 0
    for i in range(N):
        if str(k)[:3] == str(L):
            idx+=1
            print(mp.nstr(mp.log10(k)/C), idx)
        k*=2


res = p(123, 678910)

        
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
