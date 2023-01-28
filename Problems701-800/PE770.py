#PE770
from time import perf_counter
from math import comb
import numpy as np
t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''
'''
#Tried recursivity but didnt work :P
def find_min(tp: tuple= (2, 2)) -> float:
    if tp[0] == 0:
        return 1
    if tp[1] == 0:
        return pow(2, tp[0])
    if not( tp in coefs ):
        C1 = find_min((tp[0], tp[1] - 1))
        C2 = find_min((tp[0] - 1, tp[1]))
        coefs[tp] =  2  / (1/C1 + 1/C2)
    
    return coefs[tp]
'''
'''
It can be shown that n = g(X) has to satisfy

2^2n/(2^(2n-1) + ncr(2n, n)/2) >= X

Which is equivalent to (2-X) 2^(2n-1) >= X/2 ncr(2n, n)
'''
def naive_tester(X):
    n = 1
    while (2-X)*pow(2, 2*n-1) < X/2 * comb(2*n, n):
        n+=1
    return n

def find_min(X):
    # Minimum value for n
    '''
    Using 
    https://math.stackexchange.com/questions/2700734/lower-bounds-for-2n-choose-n
    @robjohn, we can see that 
    (2-X) 2^(2n-1) >= X/2 ncr(2n, n) >= 
    X/2 4^n/sqrt(pi(n + 1/pi))
    iff
    sqrt(pi(n + 1/pi)) >= X/(X-2)
    This approximation, stronger than Stirling's
    is sharp enough to give the exact result even
    for X = 1.9999
    '''
    n = int((X/(2-X)) ** 2 /np.pi - 1/np.pi + 1)
    return n



# assertion block
assert naive_tester(1.7) == find_min(1.7)
assert naive_tester(1.9) == find_min(1.9)
res = find_min(1.9999)
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
