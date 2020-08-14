#PE457
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    dat = []
    for i in data:
        if i:
            if int(i) < pow(10, 7):
                dat.append(int(i))

res = 0 + 5
dat = dat[2:]
mods = [3] * len(dat) #f(4)




res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
