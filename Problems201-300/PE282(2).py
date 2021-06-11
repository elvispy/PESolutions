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
M = pow(14, 8)

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
def split(m):
    p = 1
    while (m%2 == 0):
        p *=2
        m //= 2
    return p, m

def sequence(M):
    p, i = split(M)
    res = [(p, i)]
    M = i
    while (M > 1):
        M = phi(M)
        p, i = split(M)
        M = i
        res.append((p, i))
    return res

A = sequence(M)





def one(n, m):
    #Calculates 2 |^ (n+3) %m

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

def two(n, m = M):
    '''Calculates 2 ||^ (n+3) mod m'''
    if m == 1:
        return 0
    elif n == 0:
        return (2**2**2)%m
    elif n == 1:
        return (2**2**2**2)%m
    elif n == 2:
        return pow(2, 2 ** 2 ** 2 ** 2, m)
    
    p, m = split(m)
    return combine([(0, p), (pow(2, two(n-1, phi(m)), m), m)])
a = 2 ** 2 ** 2 ** 2 ** 2
for i in range(1, 1500):
    try:
        assert two(2, i) == a%i
    except AssertionError:
        print(i)


def three(n):
    '''Calculates 2|||^(n+3) %M
    The idea is that if we want to know 2^2^2^2^...^2 mod m = 2^k * v, 
    we need to know both in mod 2^k and v and then combine them.
    
    if n is big enough (n > 0), mod 2^k is always zero.
    To know mod v, since it is odd, we use euler theorem, so we need to know
    2^2^2 ... ^2 mod phi(m), which we decompose in odd and even part. 

    Thus reducing the modulus which we are checking against. Eventually, m will be 1, and therefore 
    the modulus will be zero. For M = 14^8, this happens in the 10th iteration approximately. 

    '''
    if n == 0:
        return pow(2, 16, M)
    
    A = sequence(M)[::-1] #Everything but the last one (which i know is zero zero)
    x = A.pop(0)
    last = (0, 0) 
    for (p, i) in A:
        res_odd = combine([(last[0], x[0]), (last[1], x[1])])
        last = (0, pow(2, res_odd, i))
        x = (p, i)

    return combine([(last[0], x[0]), (last[1], x[1])])
assert  three(1) == two(100, M)

def four(n):
    '''Calculates 2||||^(n+3) %M'''

    '''This is because four(0) = 2||||^(3) = 2|||^(2||||^(2)) = 2|||^(4) = three(1)
    and four(n) has as many powers of two in its tower as four(0), so four(n) = four(0) mod M'''
    return three(1)

def ackermann(n):
    '''Computes A(n, n)%M'''
    if n == 0:
        return n+1
    elif n == 1:
        return n+2
    elif n == 2:
        return 2*n+3
    elif n == 3:
        return pow(2, n+3, M) - 3
    elif n == 4:
        return two(n) - 3
    elif n == 5:
        return three(n)-3
    elif n == 6:
        return four(n) - 3
    else:
        raise Exception("Not defined!")



res = sum([ackermann(n) for n in range(7)])%M
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
