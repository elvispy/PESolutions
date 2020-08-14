#PE504
from time import perf_counter
from math import ceil, sqrt, floor
import mpmath as mp
mp.mp.dps = 30
t = perf_counter()

def miceil(a, b, l):
    #this function calculates ceil(-l*a/b), in a precise manner
    c = floor(a*l/b)
    if b*c <= l*a and l*a < b*(c+1):
        return -c
    elif b*(c+1) <= l*a and l*a < b*(c+2):
        return -c-1
    elif b*(c-1) <= l*a and l*a < b*c:
        return -c+1
    
def firstQ(a, b):
    #This function calculates the number of points strictly inside the triangle
    #(0, 0), (a, 0), (0, b)
    a  = abs(a)
    b = abs(b)
    res = (a-1)*(b-1)
    aux = a/b
    for l in range(1, b):
        res += miceil(a, b, l)

    return res

results = []

for i in range(100):
    results.append([])
    for j in range(100):
        results[i].append(firstQ(i+1, j+1))

def insideQuad(A, B, C, D):
    #This function calculates the number of points strictly inside the cuadrilateral ABCD
    #And returns true if its a perfect square
    res = results[A-1][B-1] + results[B-1][C-1] + results[C-1][D-1] + results[D-1][A-1]

    res += A + B + C + D - 3
    aux = ceil(sqrt(res))
    if aux*aux == res:
        return True
   
    return False

def nbQuad(n):
    #This function counts the number of desired qwuadrilaterals
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if insideQuad(i+1, j+1, k+1, l+1):
                        res += 1
    return res


res = nbQuad(100)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
