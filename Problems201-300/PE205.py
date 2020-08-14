#PE205
from time import perf_counter
import mpmath as mp
mp.mp.pretty = True
mp.mp.dps = 50
t = perf_counter()

def probs(nb, si):
    if nb == 1:
        return [0] + [1] * si
    res = [0] * (nb*si + 1)
    ant = probs(nb-1, si)
    for j in range(len(ant)):
        for k in range(1, si+1):
            res[j + k] += ant[j]
    return res

def probwin(lis1, lis2):
    s1 = sum(lis1)
    s2 = sum(lis2)
    res = mp.mpf(0)
    den = mp.mpf(s1 * s2)
    for i in range(len(lis1)):
        for j in range(0, i):
            res += mp.mpf(lis1[i] * lis2[j]) / den
    return res
res = probwin(probs(9, 4), probs(6, 6))
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
