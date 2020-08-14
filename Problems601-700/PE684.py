#PE
from time import perf_counter
t = perf_counter()
from math import sqrt
import mpmath as mp
mp.mp.dps = 30
mp.mp.pretty = True

elmod  = 1_000_000_007
def fibbo(n):
    Phi = (1+mp.sqrt(5))/2
    phi = (1-mp.sqrt(5))/2
    res = (mp.power(Phi, n) - mp.power(phi, n))/mp.sqrt(5)
    res = mp.nint(res)
    return int(res)
fibbolis = [fibbo(i) for i in range(2, 91)]

s = lambda n: (n%9+1)*pow(10, n//9, elmod) -1
S1 = lambda k: sum([s(i) for i in range(1, k+1)])
def S2(k):
    kp = k+1
    if k%9 == 8:
        res = 5 * (pow(10, kp//9, elmod)-1)-kp
        return res
    else:
        aux = kp + 8 - kp%9
        aux2 = sum([s(l) for l in range(kp, aux+1)]) % elmod
        return (S2(aux) - aux2)%elmod



res = 0
for i in range(89):
    #print(i)
    res += S2(fibbolis[i])
    res = res%elmod
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
