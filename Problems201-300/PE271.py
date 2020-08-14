#PE271
from time import perf_counter
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
t = perf_counter()
sets = []
def sett(n):
    #Returns the set of solutions for x^3 = 1 mod n
    res = [1]
    for i in range(2, n):
        if pow(i, 3, n) == 1:
            res.append(i)
    return res


def addd(idxs, coefs):
    idxs[0] += 1
    for i in range(len(idxs)-1):
        if idxs[i] >= len(coefs[i]):
            idxs[i] %= len(coefs[i])
            idxs[i+1] += 1


def modd(coefs, idxs, decom, n):
    res = 0
    exp = 1
    for i in decom:
        exp *= (i-1)
    for i in range(len(decom)):
        aux = 1
        for j in range(len(decom)):
            if j == i:
                aux *= coefs[i][idxs[j]]
                aux %= n
            else:
                aux *= pow(decom[j], exp, n)
        res += aux
    return res%n

            
def S(n):
    #Calculates the result S(n) for square free numbers
    decom = []
    for i in primes:
        if n%i == 0:
            decom.append(i)
    coefs = [sett(i) for i in decom]
    idxs = [0] * len(decom)
    addd(idxs, coefs)
    res = 0
    while True:
        try:
            res += modd(coefs, idxs, decom, n)
            addd(idxs, coefs)
        except IndexError:
            break
    return res
        
    
n = 13_082_761_331_670_030
res = S(n)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
