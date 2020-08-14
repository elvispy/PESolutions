#PE487
from time import perf_counter
from math import sqrt
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
idx = 0
while True:
    if int(data[idx]) > 50000:
        break
    idx += 1
data = [int(i) for i in data[:idx]]

def is_p(n):
    for i in data:
        if i >= sqrt(n):
            return True
        elif n%i == 0:
            return False
    return True
primes = []
for i in range(int(2*pow(10, 9))+1, int(2*pow(10, 9) + 2000), 2):
    if is_p(i):
        primes.append(i)


res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
