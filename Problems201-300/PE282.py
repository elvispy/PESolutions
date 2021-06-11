#PE282
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'

M = pow(7, 8)
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data2 = []
    for i in data:
        if i and int(i) < M:
            data2.append(int(i))
        else:
            break
                
    del data


def phi(n):
    #Euler function phi(n)
    if n == 1:
        return 1
    res = 1

    for p in data2:
        aux = 0
        while (n%p == 0):
            aux += 1
            n //= p
        if aux > 0:
            res *= pow(p, aux-1) * (p-1)
        if (n == 1):
            break

    return res
assert phi(6)  ==  2
assert phi(10) == 4


def combine(lists) -> int:
    '''
    List is a set of tuples with two elements (k, n)

    combine will return the smallest non-negative integer p such that n|(p-k)
    '''
    if len(lists) == 1:
        return lists[0][0]
    n1 = lists[0][1] 
    n2 = lists[1][1]
    k1 = lists[0][0]
    k2 = lists[1][0]
    inv1 = pow(n2, phi(n1)-1, n1)
    inv2 = pow(n1, phi(n2)-1, n2)
    res = (k1 * n2 * inv1 + k2 * n1 * inv2)%(n1*n2)
    return combine([(res, n1*n2)] + lists[2:])
assert combine([(2, 3), (3, 4)]) == 11

def one(n, m):
    #Calculates 2 |^ (n+3)

    v = 0
    while pow(m, 1, pow(2, v)) == 0:
        v+=1

    n1 = pow(2, v-1)
    n2 = m//n1
    if n+3 >= n1:
        k1 = 0
    else:
        k1 = n1

    k2 = pow(2, (n+3)%phi(n2), n2)
    return combine([(k1, n1), (k2, n2)])
assert one(1, 14) == 2
def split(m):
    p = 1
    while (m%2 == 0):
        p *=2
        m //= 2
    return p, m
def two(n, m):
    '''Calculates 2 ||^ (n+3) mod m'''
    if m == 1:
        return 0
    elif n == 0:
        return (2**2**2)%m
    elif n == 1:
        return (2**2**2**2)%m
    
    p, m = split(m)
    return combine([(0, p), (pow(2, two(n-1, phi(m)), m), m)])

a = 2 ** 2 ** 2 ** 2 ** 2
for i in range(1, 1500):
    try:
        assert two(2, i) == a%i
    except AssertionError:
        print(i)

periodos = []

for p in data2[:10]:
    j = 0
    res = []
    aux = two(j, p)
    while not(aux in res):
        res.append(aux)
        j+=1
        aux = two(j, p)
    periodos.append([j])

res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
