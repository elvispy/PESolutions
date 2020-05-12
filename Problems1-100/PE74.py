#PE74
from time import perf_counter
t = perf_counter()
known = []
for i in range(1, 1_000_001):
    known.append(set([i]))

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

def sumfact(n):
    n =str(n)
    return sum([fact(int(i)) for i in n])
def chain(n):
    aux = n
    res = {n}
    while True:
        aux = sumfact(aux)
        #print(aux)
        if aux < n:
            return res.union(known[aux-1])
        elif aux in res:
            return res
        res = res.union({aux})
for i in range(1, 1_000_000):
    known[i-1] = chain(i)

lol = max([len(i) for i in known])
res = sum([len(i) == lol for i in known])
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
