#PE296
from time import perf_counter
import math
t = perf_counter()

def mcd(a, b):
    c = min(a, b)
    d = a+b-c
    if c == 0:
        return d
    else:
        return mcd(c, d%c)

res = 0
for d in range(1, 33333):
    print(d)
    for v1 in range(1, math.floor(100_000/3*d)+1):
        for v2 in range(v1, math.floor(100_000/d-v1) + 1):
            if mcd(v2, v1) == 1:
                if math.floor(pow(10, 5)/(v1+v2) - d) - d >= math.ceil(d*v2/(v1+v2)):
                    res += math.floor(pow(10, 5)/(v1+v2) - d) - math.ceil(d*v2/(v1+v2)) + 1


print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
