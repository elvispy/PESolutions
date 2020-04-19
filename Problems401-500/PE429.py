#PE429
from time import perf_counter
from pathlib import Path
from math import floor
t = perf_counter()
PATH = str(Path(__file__).parent.parent / '2T_part1.txt')
mymod = 1_000_000_009
n = 100_000_000

def pot(p):
    i = 1
    res = 0
    while pow(p, i) <= n:
        res += floor(n/pow(p, i))
        i+=1
    i-=1
    return int(res)
with open(PATH, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if (i and int(i) <= n)]

res = 1
for i in data:
    a = pot(i)
    num = pow(i, a, mymod)
    res *= (pow(num, 2)+1)
    res = res%mymod
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
