#PE120
from time import perf_counter
t = perf_counter()

res = 0
for a in range(3, 1001):
    res += pow(a, 2) - a
    if a%2 == 0:
        res -= a




print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
