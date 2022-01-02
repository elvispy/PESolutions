#PE127
from time import perf_counter
t = perf_counter()
M = 120_000 #a, b, c <= M

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if (i and int(i) <= M)]

decoms = [0] * M

aux = [0] * len(data)
'''
N = 1
while N <= M:
    idx = 0
    while idx < len(data):
        whil
'''

def gcd(a, b):
    m = b if b > a else a
    n = a+b-m
    if m%n == 0:
        return n
    return gcd(n, m%n)

cops = {}

for i in range(1,M+1):
    cops[i] = [1]

for a in range(2, M):
    for cop in cops[a]:
        j = 1
        while a * j + cop <= M:
            cops[a*j+cop].append(a)
            j+=1
# assertion block
# assert 2 == 2
res = cops
print("El resultado es: {}".format(res[47]))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
