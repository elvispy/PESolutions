#PE134
from time import perf_counter

t = perf_counter()


from pathlib import Path
from math import log, floor

a = Path(__file__).parent.parent / "pprimes.txt"
with open(a, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < 1_000_005]
data = data[2:]


def minn(p1, p2):
    val = floor(log(p1, 10)) + 1
    a = (-p1 * pow(10, p2 - 1 - val, p2) )%p2
    return pow(10, val) * a + p1

res = 0

for i in range(len(data)-1):
    l = minn(data[i], data[i+1])
    res += l
    

print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
