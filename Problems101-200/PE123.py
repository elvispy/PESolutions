#PE123
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [1] + [int(i) for i in data if i]

def rem(nth, pn = None):
    if pn == None:
        pn = data[nth]
    if nth%2 == 0:
        return 2
    else:
        return (2*nth*pn)%(pn**2)

M = 1e+10
raw = lambda nth: 2*nth*data[nth]
i = 7037
while raw(i) < M:
    i+=2 # Only odd primes work


# assertion block
assert rem(i) >= M
assert rem(7037) == pow(data[7037] - 1, 7037, data[7037] ** 2) + pow(data[7037] + 1, 7037, data[7037] ** 2)
assert rem(7035) < 1e+9

print("El resultado es: {}".format(i))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
