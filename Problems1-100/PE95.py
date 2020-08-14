#PE95

import time
val = time.perf_counter()

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < pow(10, 6)]


def n_div2(n):
    if n == 1:
        return 0
    res = 1
    miaux = n
    idx = 0
    
    while n> 1:
        if data[idx] > n:
            break
        exp = 0
        while n%data[idx] == 0:
            exp+=1
            n //= data[idx]
        res *= pow(data[idx], exp+1)-1
        res //= data[idx] - 1
        idx+=1

    return res - miaux
        
def n_div(n):
    if n == 1:
        return 0
    div = 0
    mx = int(n/2)+2
    c = 1
    while c<mx:
        if n%c == 0:
            mx = max(int(n/c), c)
            div += c
            div = div + int(n/c) if c>1 else div
        c+=1
    return div
            
N = 1_000
candidates = list(range(2, N+1))
mc = 5
mcs = 12496
perfect = [1, 6, 28, 496, 8128]
for n in candidates:
    failed = False
    if n == None:
        continue
    chain = [n]
    lol = n_div(n)
    while lol != n:
        if lol < 1000000 and lol>1:
            candidates[lol-2] = None
        else:
            failed = True
            break
        if chain.count(lol) > 0:
            failed = True
            break
        else:
            chain.append(lol)
    
        lol = n_div(lol)
    if len(chain) > mc and not failed:
        mc = len(chain)
        mcs = n
    
    
print(time.perf_counter()-val)
