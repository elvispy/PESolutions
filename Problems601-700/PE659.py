#Projec Euler problem 659
from math import ceil
import time
from pathlib import Path
start = time.perf_counter()
path = Path(__file__).parent.parent / "2T_part1.txt"
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i)%4 ==1]


def P(k):
    n = 4*k*k+1
    d = 1
    while n > 1:
        d+=4
        while n%d == 0:
            n /= d
        
        if d*d > n and n > 1:
            return int(n)
    return int(d)
            
#print(sum([P(i) for i in range(1, 10_001)]))
print(time.perf_counter()-start)
