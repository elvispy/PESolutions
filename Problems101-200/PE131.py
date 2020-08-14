#PE131
from time import perf_counter
from math import sqrt
t = perf_counter()
def is_p(p):
    for j in range(2, int(sqrt(p))+1):
        if p%j == 0:
            return False
    return True

def count_Primes(N):
    res = 0
    j = 1
    aux = 7
    while aux <= N:
    
        if is_p(aux):
            res += 1
        j+=1
        #print(aux)
        aux = 3*j*j+3*j+1
    return res


res = count_Primes(1_000_000)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
