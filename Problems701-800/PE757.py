#PE757
from time import perf_counter
from numpy import floor, sqrt
t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''
# It is possible to show that the stealthy numbers are the ones that can be expressed as
# N = q(q+1)c(c+1), with q >= 1, c >= 1

def count_stealthy(M = 1e+14) -> int:
    c = 1
    #res = 0
    result = []
    #plotter = []
    while (c*(c+1))**2 <= M:
        #R = M/(c*(c+1))
        ##aux = floor((-1 + sqrt(1+4*R))/2)
        #res += (aux - c + 1) if (aux >= c) else 0
        q = c
        while q*c*(q+1)*(c+1) <= M:
            #plotter.append(q*c*(q+1)*(c+1))
            result.append(int(q*c*(c+1)*(q+1)))
            #print(q*c*(q+1)*(c+1), q, c)
            q+=1
        c+=1
        #plotter.sort()
    #print(plotter)
    return len(set(result))

def ineficcient_stealthy(M):
    I = 4
    res = 0
    plotter = []
    while I <= M:
        A = []
        for a in range(1, int(sqrt(I))+1):
            if I%a == 0: # If divisor
                A.append(a + I/a) # Add divisors
                if len(A) > 1:
                    if abs(A[-1]-A[-2]) == 1: # Check if the sum differs by one
                        plotter.append(I)
                        res += 1
                        break
        I += 1  
    plotter.sort()
    #print(plotter)      
    return res
# assertion block
for j in range(2, 5):
    assert count_stealthy(10**j) == ineficcient_stealthy(10**j)
assert count_stealthy(1e+6) == 2851
res = count_stealthy()
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
