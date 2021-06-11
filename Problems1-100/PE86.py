#PE86
from time import perf_counter
from pythtriples import *
from math import floor, ceil
t = perf_counter()
''' 
The idea is that the shortest path has length (a^2 + (b+c)^2)^(1/2)
so this program finds all pythagorean triples x, y, z and then makes a bijection intro triples with 
a >= b >= c
'''

def cases(M, A):
    if A <= M:
        return floor(A/2)
    else:
        return ceil((2*M-A+1)/2)
def int_routes(M):
    res =0
    lis = pythagoreanTriplets(int(M*pow(5, 1/2)))
    #print(lis)
    for el in lis:
        #print(lis)
        if el[0] <= M and 2*el[0] >= el[1]:
            #print(el)
            res += cases(el[0], el[1])
        if el[1] <= M:
            #print(el)
            res += cases(el[1], el[0])
    return res

def minn_int_routes(I):
    b = 1
    while int_routes(b) < I:
        b*=2
    a = b//2
    c = floor((b-a)/2 + a)
    while (b-a)>1:
        if int_routes(c) < I:
            a = c
        else:
            b = c
        c = floor((b-a)/2 + a)

    return b

        

    
assert cases(5, 3) == 1
assert int_routes(100) == 2060
assert int_routes(99) == 1975
assert minn_int_routes(43) == 16
assert minn_int_routes(44) == 18

res = minn_int_routes(1_000_000)

print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
