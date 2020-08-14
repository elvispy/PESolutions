#PE381
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

data = data[2:]
def S(p):
    inv2 = -pow(2, p-2, p)
    inv3 = -pow(3, p-2, p)
    inv4 = -pow(inv2, 2, p)
    return (inv2 * (1 + inv3 * (1 + inv4)) ) % p

res = 0

for i in data:
    res += S(i)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
