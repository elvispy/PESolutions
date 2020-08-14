#PE425
from time import perf_counter


from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < pow(10, 7)]


t = perf_counter()

res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
