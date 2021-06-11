#PE123
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]



# assertion block
# assert 2 == 2
res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
