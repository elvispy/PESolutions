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
tests = [2, 3, 5, 7, 11]
primes = []
for i in range(2016 + 2017, 10 ** 11 + 1, 2*2017):
    is_p = True
    for p in tests:
        if pow(p, i-1, i) != 1:
            is_p = False
            break
    if is_p:
        primes.append(i)


# assertion block
# assert 2 == 2
res = primes[-1]
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
