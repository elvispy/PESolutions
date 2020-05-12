#PE521
from time import perf_counter
from math import floor, sqrt, ceil
from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
t = perf_counter()
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < 1_000_000]

def smpf(n, pj, idx = -1):
    """Returns the numbers between 1 and n s.t. smpf == pj"""
    if n < pj:
        return 0
    elif n< pj*pj:
        return 1
    if idx == -1:
        idx = data.index(pj)
    res = 0
    for i in range(idx):
        res += smpf(floor(n/pj), data[i], i)

    return floor(n/pj) - res

def S1(n):
    r = floor(sqrt(n))
    res = 0 
    for i in data:
        if i > n:
            break
        res += smpf(n, i) * i
    return res

res = S1(100)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
