#PE124
from time import perf_counter
t = perf_counter()
from math import log
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    aux = []
    for i in data:
        if int(i) > pow(10, 5):
            break
        if i:
            aux.append(int(i))
        
data = aux
del aux

sqfree = [1]
def squarefree(sqfree, N = pow(10, 5), idx = 0):
    #Returns a list with an ordered list of square free numbers
    aux = sqfree + [data[idx] * i for i in sqfree if data[idx] * i <= N]
    aux.sort()
    return aux



def lstsq(decoms, expensive = False, N = 100000):
    #Returns a list of all numbers that have those numbers in their decomposition
    if type(decoms) == type(1):
        decom = []
        for i in data:
            if decoms > 1:
                if decoms%i == 0:
                    decom.append(i)
                    decoms //= i
            else:
                break
        decoms = decom
    ini = [1]  * (len(decoms))
    aux = 1
    for i in decoms:
        aux *= i
    if expensive:
        res = [aux]
    else:
        res = 1
    while True:
        aux *= decoms[0]
        ini[0] += 1
        for idx in range(0, len(decoms)-1):
            
            if aux <= N:
                break
            else:
                aux //= pow(decoms[idx], ini[idx]-1)
                ini[idx] = 1
                aux *= decoms[idx + 1]
                ini[idx+1] += 1
        if aux <= N:
            if expensive:
                res.append(aux)
            else:
                res+=1
        else:
            break

    return res
    

N = 10000
idx = 0
while data:
    if data[idx] > N:
        break
    #print(sqfree)
    sqfree = squarefree(sqfree, N, idx)
    idx += 1

nbs = 0
idx = 0
while nbs < N:
    aux = sqfree[idx]
    decoms = []
    if aux > 1:
        for i in data:
            if aux > 1:
                if aux%i == 0:
                    aux //= i
                    decoms.append(i)
            else:
                break
        nbs += lstsq(decoms)
        
    else:
        nbs+=1
    idx += 1

nb = lstsq(sqfree[idx-1], True)
nb.sort()
res = nb[-(nbs-N + 1)]
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
