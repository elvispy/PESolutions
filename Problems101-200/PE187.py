#PE187
from time import perf_counter
t = perf_counter()
from pathlib import Path
from math import sqrt, floor
from bisect import bisect_left

n = pow(10, 8)
def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


path = str(Path(__file__).absolute().parent.parent / "2T_part1.txt")
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
data = data[:3001134]
res = len(data)

for i in range(1, 1229):
    aux = floor(pow(10, 8)/data[i])
    posaux = binary_search(data, aux)
    while posaux == -1:
        aux -=1
        posaux = binary_search(data, aux)
    res+= posaux - i + 1
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
