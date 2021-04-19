#PE NOT FINISHED
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

data = data[:20001]

ci = [1] #ci[j] = |pi^{-1}(j)| with j <= 20000
for i in range(1, len(data)):
    ci.append(data[i]-data[i-1])

MOD = 1_004_535_809
def T(n, k):
    idx = 1
    res = ci
    while idx < k:
        
        resaux = []
        for i in range(n+1):
            miaux = 0
            for j in range(i+1):
                miaux += (ci[j] * res[i-j])
                miaux %= MOD
            resaux.append(miaux)
        res = resaux
        idx+=1
        
        print(idx)
        #print(resaux)
    return res[n] % MOD
res = T(20000, 20000)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
