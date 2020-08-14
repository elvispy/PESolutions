#PE451
from time import perf_counter

'''
from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

'''
t = perf_counter()


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def sols(p, q):
    l = [p[0] * modinv(p[0], q[0]), q[0] * modinv(q[0], p[0])]
    res = []
    for i in p[1]:
        for j in q[1]:
            res.append((j * l[0] + i * l[1])%(p[0]*q[0]))
    res = list(set(res))
    res.sort()
    return [p[0] * q[0], res]
def sols2(n):
    aux = [([i, [1, i-1]] if i%2 else [i, [1, i//2-1, i//2+1, i-1]]) for i in n]
    while len(aux) > 1:
        aux = [sols(aux[0], aux[1])] + aux[2:]
    return aux[0]
res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
