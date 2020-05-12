#PE100
from time import perf_counter
import mpmath as mp
t = perf_counter()
mp.mp.dps = 100
q = mp.power(10, 12)

while True:
    p = mp.ceil(mp.fdiv(q, mp.sqrt(2)))
    if 2*p*(p-1) == q*(q-1):
        break
    q+=1

print("El resultado es: {}".format(q))
print("The time spent is: {}".format(perf_counter()-t))
