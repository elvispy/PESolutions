#PE
from time import perf_counter
t = perf_counter()
from mpmath import mp
sqrt = mp.sqrt
floor = mp.floor
mp.dps = 100

M = 1_000

def mmax(M):
    # Returns the value of D which maximines the 
    # fundamental solution of x2-Dy2=1
    i = 1
    D = 1
    m = 0
    res = 0
    while D <= M:
        if D == i*i:
            i+=1
            D+=1
            continue
        L, _ = primitive_solution(D)
        if L > m:
            m = L
            res = D
        D+=1
    return res

def primitive_solution(D):
    '''
    Calculates the primitive solution of x2-Dy2=1
    via continued fractions of sqrt(D)
    for more info, consult section 3.2 of 
    Titu Andreescu's Introduction to Diophantine Equations
    '''
    sD = sqrt(D)
    a0 = floor(sD)
    end = 2* a0
    continued = [a0]
    sD -= a0
    #rem = sD
    sD = 1/sD
    ak = -1
    while ak != end:
        ak = floor(sD)
        continued.append(ak)
        sD -= ak
        #if abs(sD-rem) < 1e-:
        #    break
        if sD > 0:
            sD = 1/sD
    m = len(continued) - 1
    if m%2 == 0:
        N = m-1
    else:
        N = 2*m-1
    pk = continued[(N-1)%m+1]
    qk = 1
    for ii in range(N-1, 0, -1):
        pk, qk = continued[(ii-1)%m + 1] * pk + qk, pk
    pk, qk = continued[0] * pk + qk, pk

    return pk, qk

# Assertion blocks
assert primitive_solution(3) == (2, 1)
assert primitive_solution(5) == (9, 4)
assert primitive_solution(6) == (5, 2)
assert primitive_solution(7) == (8, 3)
assert primitive_solution(46) == (24335, 3588)
assert primitive_solution(61) == (1766319049, 226153980)
assert mmax(7) == 5
a, b = primitive_solution(951)
assert a**2 - 951 * b**2 == 1


print("El resultado es: {}".format(mmax(M)))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
