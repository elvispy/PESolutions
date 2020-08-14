#PE516
from time import perf_counter
from math import sqrt
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")

idx = 0
while True:
    if data[idx]:
        if len(data[idx]) > 6:
            break
    idx += 1
data = [int(i) for i in data[:(idx + 1)]]


def is_p(n):
    for i in data:
        if n%i == 0:
            return False
        if i >= sqrt(n):
            return True
    return True

def special_primes(N):
    #Returns a list of primes s.t. p- is 5-smooth
    num = [3, 0, 0]
    ps = [2, 3, 5]
    aux = 8
    res = []
    while True:
        aux *= 2
        num[0] += 1
        for idx in range(2):
            if aux < N:
                break
            else:
                aux //= pow(ps[idx], num[idx])
                num[idx] = 0
                aux *= ps[idx + 1]
                num[idx+1] += 1
        if aux < N:
            if is_p(aux+1):
                res.append(aux+1)
        else:
            break
        
    res.sort()
    
    return res


def add(pos, aux, sp, L):
    nprimes = len(sp)
    for j in range(len(pos)-1, -1, -1):
        aux = 1
        auxpos = []
        for l in range(len(pos)):
            if l < j:
                aux*= sp[pos[l]]
                auxpos.append(pos[l])
            else:
                for i in range(j, len(pos)):
                    try:
                        aux*= sp[pos[j] + i-j+1]
                        auxpos.append(pos[j] + i - j + 1)
                    except IndexError:
                        aux = L + 1
                        break
                if aux <= L:
                    return [auxpos, aux]
    return -1
            

def S(L = pow(10, 12)):
    elmod = pow(2, 32)
    sp = special_primes(L)
    res = 0
    nb = 0
    pos = []
    aux = 1

    ps = [2, 3, 5]
    while aux <= L:
        #In this loop, nb is changing

        while True:
            #in this loop, both pos and aux are changing
            num = [0, 0, 0]
            vaux = 1
            

            while True:
                #In this while we're handling with p = 2, 3, 5
                
                if vaux * aux <= L:
                    res += vaux * aux
                    res %= elmod
                    
                    #print(vaux * aux)
                else:
                    break
                vaux *= 2
                num[0] += 1
                for idx in range(2):
                    if vaux * aux <= L:
                        break
                    else:
                        vaux //= pow(ps[idx], num[idx])
                        num[idx] = 0
                        vaux *= ps[idx + 1]
                        num[idx+1] += 1
                

                

            preres = add(pos, aux, sp, L)
            if preres == -1:
                break
            else:
                [pos, aux] = preres
            

        nb += 1
        pos = list(range(nb))
        aux = 1
        for i in pos:
            aux *= sp[i]

    return res
    
        

        

res = S()
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
