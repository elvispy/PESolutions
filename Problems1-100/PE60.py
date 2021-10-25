#PE60
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

def bin_search(lis, val):
    #Looks for val in ordered list. Returns None if not in list
    a = 0
    b = len(lis)-1
    while a < b:
        aux = (a+b)//2
        if lis[aux] < val:
            a = aux
        elif lis[aux] > val:
            b = aux
        else:
            return True
        if aux == a and a == b-1:
            return False
    raise Exception('You shouldnt be here')

def tester(sset, prime):
    if sset == None:
        return False
    #Will test if sset U prime is a valid set.
    for val in sset:
        if bin_search(data, int(str(val) + str(prime))) == False:
            return False
        if bin_search(data, int(str(prime) + str(val))) == False:
            return False
    return True


C = pow(10, 3)
ii = 1
jj = 0

prime_pair_sets = {2:[], 3:[], 4:[], 5:[]}
while prime_pair_sets[5] == []: #Siempre que no haya un conjunto de cinco elementos, buscarlo   
    while data[jj] < C * ii: #ir de a 100mil 
        for sz in range(4, 1, -1): #Crear conjuntos especiales de ii+1 elementos
            for sset in prime_pair_sets[sz]: #Ver si el conjunto set U data[jj] es aceptable o no
                if tester(sset, data[jj]):
                    prime_pair_sets[sz+1].append(sset.union([data[jj]]))
        for pprime in data[:jj]: #Ahora el caso de conjuntos de dos elementos
            if tester(set([pprime]), data[jj]) == True:
                prime_pair_sets[2].append(set([pprime, data[jj]]))
        jj+=1
    ii+=1
    if len(prime_pair_sets[5]) > 0:
        prime_pair_sets[5] = sum(prime_pair_sets[5][0]) # No necesariamente el menor, pero si da el resultado correcto
        break
# assertion block
# assert 2 == 2
res = prime_pair_sets[5][0]
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
