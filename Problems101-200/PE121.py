#PE121
from time import perf_counter
t = perf_counter()
from math import floor
def dist(n):
    res = {i:0 for i in range(n+1)}
    res[0] = 1
    
    for i in range(2, 2+n):
        aux = dict()
        for j in res.keys():
            if j == 0:
                aux.update({0:res[0] * (i-1)})
            else:
                aux.update({j:(res[j] * (i-1) + res[j-1])})
        res = aux

    return res
        
        
def bet(n):
    distt = dist(n)
    b = 0
    a = 0
    for i in range(n+1):
        if 2*i > n:
            a+=distt[i]
        b+= distt[i]

    p = floor((b-a)/a) + 1

    return p
            
        
res = bet(15)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
