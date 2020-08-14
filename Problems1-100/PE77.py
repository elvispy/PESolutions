#PE77
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / 'pprimes.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

ant = [None, None, [[1]], [[0, 1]], [[2]]]

def nbSums(N = 0) -> int:
    #This function will return the number of of linear combination of primes which
    #sum up to N. If N == 0, then it will just add another layer.

    if N == 0:
        N = len(ant)

    while len(ant) <= N:
        res = []
        i = 0
        NN = len(ant)
        while data[i] < NN - 1:
            aux1 = ant[-data[i]]

            for el in aux1:
                if len(el) > i + 1:
                    continue
                elif len(el) == i + 1:
                    aux2 = el.copy()
                    aux2[-1] += 1

                elif len(el) < i + 1:
                    aux2 = el.copy()
                    while len(aux2) < i + 1:
                        aux2 = aux2 + [0]
                    aux2[-1] = 1
                res.append(aux2)

            i+=1

        if data[i] == NN:
            aux3 = [0] * (i + 1)
            aux3[-1] = 1
            res.append(aux3)

        ant.append(res)
            


    return len(ant[-1]) <= 5000





while nbSums():
    pass


print("El resultado es: {}".format(len(ant) - 1))
print("The time spent is: {}".format(perf_counter()-t))
