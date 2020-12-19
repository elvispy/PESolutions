#PE174
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if (i and int(i) < 1_100_000)]

def nextt(n, s):
    s *= 2
    n[0] += 1
    i = 0
    while s > 1_000_000:
        if data[i] > 1_000_00:
            return None
        s = s//pow(data[i], n[i])
        n[i] = 0
        i += 1
        s *= data[i]
        n[i] += 1

    return s
            

n = [0] * 80_000

s = 1
c = 0
while s:
    c += 1
    s = nextt(n, s)
    
    






res = c
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
