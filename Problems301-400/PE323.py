#PE323
from time import perf_counter
import mpmath as mp
t = perf_counter()
mp.mp.dps = 30
mp.mp.pretty = True

def binom(n, m):
    if m in [0, n]:
        return mp.mpf('1')
    else:
        res = mp.mpf('1')
        for i in range(m+1, n+1):
            res *= mp.mpf(str(i))
        for i in range(1, n-m+1):
            res /= i
        return res

#These two values were calculated by hand
resources = [0, 2]
def prob(i, n):
    """Probability of i digits needed to get to n ones"""
    return binom(n, i)/mp.mp.power(2, n)
def F(n):
    """Calculate F(n) recursively"""
    aux = len(resources)
    if aux > n:
        return resources[n]
    else:
        miaux = sum([prob(i, aux)*(resources[i] +1) for i in range(aux)])
        miaux += prob(aux, aux)
        miaux /= 1-prob(aux, aux)
        resources.append(miaux)

        #Ask again for the nth place
        return F(n)

print("El resultado es: {}".format(F(32)))
print("The time spent is: {}".format(perf_counter()-t))
