#PE650(2)
from time import perf_counter
t = perf_counter()
N = 20_000
elmod = 1_000_000_007
from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < 20000]

C = len(data)
def decom(n):
    '''Decomposes n into its prime factors (in list form)'''
    aux = n
    i = 0
    res = [0] * C
    while aux > 1:
        while not (aux%data[i]):
            aux //= data[i]
            res[i] +=1
        i+=1
    return res
            

def expd(n, p):
    '''Returns the maximum exponent of p that divides n'''
    res = 0
    e = 1
    while pow(p, e) <= n:
        res+= n // pow(p, e)
        e+=1
    return res
info = []
decoms = [[0] * C, [0] * C]
def aux(n):
    #Returns the prime decomposition of n!, in list form
    if n < 2:
        return [0] * C
    cma = decom(n)
    decoms.append(cma)
    res = [ (cma[i] + info[n-1][i]) for i in range(C)]

    return res

for i in range(N+1):
   info.append(aux(i))


def D(Bk):
    #Calculates the sum of the divisors given the decomposition of Bk in list form
    res = 1
    for i in range(C):
        if Bk[i] == 0:
            continue
        res *= pow(data[i], Bk[i]+1, elmod)-1
        res %= elmod
        res *= pow(data[i]-1, elmod-2, elmod)
        res %= elmod
    return res

def S(n):
    res = 1
    Bk = [0] * C
    for i in range(2, n+1):
        
        Bk = [Bk[j] + i*decoms[i][j] - info[i][j] for j in range(C)]
        res += D(Bk)
        res %= elmod
        #print(Bk[:10])
    return res
        
    

print(f"Now I will calculate, at {perf_counter()-t}")
print("El resultado es: {}".format(S(20_000)))
print("The time spent is: {}".format(perf_counter()-t))
