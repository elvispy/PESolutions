#PE144
from time import perf_counter
t = perf_counter()
import mpmath as mp
mp.mp.dps = 15
mp.mp.pretty = True
p1 = (mp.mpf(0.0071073169499659053943932), mp.mpf(9.999989897204050830))
p2 = (mp.mpf(1.4), mp.mpf(-9.6))

def next_point(p1, p2):
    T = (p2[1]/10, -4*p2[0]/10)
    N = (4*p2[0]/10, p2[1]/10)
    diff = (p1[0] - p2[0], p1[1] - p2[1])

    pint = lambda p1, p2: p1[0]*p2[0] + p1[1]*p2[1]
    smul = lambda p1, alfa: tuple([alfa*i for i in p1])
    sadd = lambda p1, p2: (p1[0] + p2[0], p2[1] + p1[1])
    ssub = lambda p1, p2: (p1[0] - p2[0], p1[1] - p2[1])

    ndir = ssub(smul(N, pint(diff, N)), smul(T, pint(diff, T)))
  
    t = -2*ndir[1]*p2[1]-8*ndir[0]*p2[0]
    t = t/(4*ndir[0]*ndir[0] + ndir[1]*ndir[1])
    res = sadd(smul(ndir, t), p2)
    return res
res = 0
while not(abs(p2[0]) <= 0.01 and p2[1] > 0):
    res+=1
    aux = p2
    p2 = next_point(p1, p2)
    p1 = aux
    #print(res)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
