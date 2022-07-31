#PE788
from time import perf_counter
t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''
M = 1_000_000_007 # Prime to take modulus.

'''
Sea D(N) la función a determinar.
Tenemos que D(N) = Z(N) + M(N), donde M(N) son los numeros tal que el cero no es el digito que mas se repite,
y Z(n) los numeros donde el cero es el que mas se repite.

sea z(n) la cantidad de numeros dominantes donde el cero es el que mas se repite y que tiene exactamente n digitos
analogamente para m(n).

Seguidamente, z(n) es la suma de b(n, k), donde b(n, k) es la cantidad de numeros con k ceros iguales.
'''
def ncr(n, r, p):
    # initialize numerator
    # and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
            p - 2, p)) % p

def D(N):
    # Number of dominating numbers with less than N+1 digits.
    return sum([a(N, k) + b(N, k) for k in range(1, N+1)])
def a(N, k):
    # Number of dominating numbers in which the repeated digit its not a zero and appears exactly k times.
    #if k < N/2: return 0
    e = min(N, 2*k-1)
    return (ncr(e, k, M) * pow(9, e-k + 1, M) )% M

def b(N, k):
    # Number of dominating numbers with less than N+1 digits in which the repeated digit it is a zero.
    if k>= N: return 0
    e = min(N, 2*k-2)
    return (ncr(e, k, M)  * pow(9, e-k+1, M) )% M



# assertion block
assert ncr(2022, 5, 7) == 6
assert b(2, 1) == 0
assert a(2, 1) == 9
assert a(2, 2) == 9
assert b(3, 2) == 9
assert a(3, 1) == 9
assert a(3, 2) == 81
assert a(3, 3) == 9

assert D(2) == 18
assert D(4) == 603
res = D(2022)
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
