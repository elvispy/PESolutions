#PE
from time import perf_counter
t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''

def maxx(N):
    n = 2
    while (n-1)/(pow(2, n)-2) >= 1/N:
        n+=1
    #Now pow(2, k) is a cantidate.
    '''
    For every n, we now have that (n-1)/v = P(v'), and
    P(v') < 1/N
    (n-1)/v < 1/N
    ==>
    v > N(n-1)
    v = N(n-1) + 1
    m = (v+1) * v
    '''
    k = N*(n-1) + 2
    return k*(k-1)
m = maxx(12345)
print("El resultado es: {}".format(m))
print("The time spent is: {}".format(perf_counter()-t))
