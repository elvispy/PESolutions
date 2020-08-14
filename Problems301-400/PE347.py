#PE347 11109800204052
       
from time import perf_counter
t = perf_counter()
from math import log, sqrt, ceil, floor
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < 5_000_000]


def M(p, q, N):
    #Calculates the biggest number divisible by both p and q, less than N
    #and not divisible by another prime r. If there is no such number, return 0
    if p * q > N:
        raise Exception("Uy Kieto!")
        return "lol"

    maxx = N
    expop = 1
    expoq = 1
    
    while (q ** expoq) * p <= N:
        auxi = N - (p ** expop) * (q ** expoq)
        
        if auxi < 0:
            expoq += 1
            expop = 0
        elif auxi < maxx:
            maxx = auxi
        expop += 1
    #print(p, q, N-maxx)
    return N - maxx


def S(N):
    #Returns the sum over all pairs of distinct primes M(p, q, N)
    aux = ceil(sqrt(N/2))
    res = 0
    for i in range(len(data)-1, 0, -1):
        if data[i] < aux:
            break
        else:
            di = data[i]
            for j in range(i):
                dj = data[j]
                if di * dj > N:
                    break
                else:
                    res += M(dj, di, N)
    idx = 0
    while data[idx] < aux:
        idx+=1

    for i in range(1, idx):
        for j in range(i):
            res += M(data[j], data[i], N)

    return res
                    
              

res = S(10_000_000)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
