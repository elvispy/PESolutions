#PE650
from time import perf_counter
t = perf_counter()
N = 20_000
elmod = 1_000_000_007
from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

def expd(n, p):
    '''Returns the maximum exponent of p that divides n'''
    res = 0
    e = 1
    while pow(p, e) <= n:
        res+= n // pow(p, e)
        e+=1
    return res
info = []
def aux(n):
    #Returns the prime decomposition of n!, in list form
    j = 0
    xd = []
    while data[j] <=n:
        xd.append(expd(n, data[j]))
        j+=1
    return xd
for i in range(N+1):
    info.append(aux(i))

def D(k):
    if k < 2:
        return 1
    if k == 2:
        return 3
    Bn = [(k+1)*i for i in info[k]]
    np = len(Bn)
    for m in range(k+1):
        for l in range(np):
            try:
                Bn[l] -= 2*info[m][l]
            except IndexError as e:
                break

    #now lets calculate the divisors
    res = 1
    for i in range(np):
        res *= pow(data[i], Bn[i]+1, elmod)-1
        res %= elmod
        res *= pow(data[i]-1, elmod-2, elmod)
        res %= elmod
    return res

def S(n):
    res = 0
    for k in range(1, n+1):
        res += D(k)
        res %= elmod
    return res

print(f"Now I will calculate, at {perf_counter()-t}")
print("El resultado es: {}".format(S(20_000)))
print("The time spent is: {}".format(perf_counter()-t))
