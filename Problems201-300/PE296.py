#PE296
from time import perf_counter
from math import gcd, ceil, floor
t = perf_counter()
M = 100_000
MN = M//3


def calc(val):
    #Returns the number of integer tuples (k, j) with
    #k > j s.t. k+j<= val
    if val < 3: return 0
    aux = (val-1)//2
    return aux * (val - aux  - 1)
def checker(val):
    #Function to check whether calc is doing things ok
    res = 0
    for j in range(1, val):
        for k in range(j+1, val - j + 1):
            if j + k <= val and k > j:
                res += 1
    return res
for i in range(1, 20):
    assert calc(i) == checker(i)

# Nums stores the number of coprimes to nums[i]
nums = [1] * (MN + 1)
nums[1] = 0
# cops stores the set of coprime numbers
cops = {}
for i in range(1,MN+1):
    cops[i] = [1]

for a in range(2, MN+1):
    # if a%1_00 == 0: print(a)
    for cop in cops[a]:
        j = 1
        while a * j + cop <= MN:
            if (a*j+cop >= 2 * a):
                nums[a*j+cop] +=1
            cops[a*j+cop].append(a)
            j+=1


def checker2(n):
    #Checks whether nums is storing the correct variables.
    res = 0
    for i in range(1, n+1):
        if 2*i > n: break
        if gcd(i, n) == 1:
            res+=1
    return res
for n in range(1, min(MN//2, 100)):
    assert checker2(n) == nums[n]
# The number of solutions is equal to the number of triples (a, b, c) with ac/(a+b) being
#an integer. Set a = km, b = kn, and we get mc/(m+n), and therefore m+n | c ==> c = j(m+n)
# Since a+b > c, k > j, and (k+j) <= M/(m+n). We need to count the number of quadruples
# with k+j <= M/(m+n), m coprime with n, m < n. calc(M/(m+n)) does the first and nums[m+n]
# the second.
# HOWEVER. We must also assure that km <= kn <= j(m+n), which adds theinequality
# k <= j(m+n)/n. 
res = 0

for mn in range(2, MN+1):
    # if mn%1_00 == 0: print(mn)
    for m in cops[mn]:
        if 2*m > mn:
            break
        if mn *(2*mn-m)/m > M:
            continue
        else:
            n = mn - m
            inter = M*n/(mn * (mn + n))
            j = ceil(n/m)
            while j <= inter:
                res += floor(j*m/n)
                j+=1
            primer = floor(inter + 1)
            ultimo = floor((M/mn - 1)/2)
            res += (ultimo - primer + 1)*(floor(M/mn) - primer - ultimo)

            


def full_checker(M):
    #Checks the number of triplets (a, b, c) a<=b<=c such that BE is integer
    res = 0
    for a in range(1, M):
        for b in range(a, M):
            for c in range(b, a+b):
                if (a*c)%(a+b) == 0 and a+b+c <= M:
                    k = gcd(a, b)
                    #print(b/k, a/k, k, k*c/(a+b))
                    res+=1
    return res

def full_checker2(M: int):
    res = 0
    for mn in range(M//3, 0, -1):
        for n in range(mn-1, mn//2-1, -1):
            if gcd(n, mn) == 1 and 2*n >= mn:
                j = ceil(n/(mn-n))
                while  j <= (M/mn-1)/2:
                    if j<=  n*M/(mn * (mn + n)):
                        #print(n, mn - n, int(M/mn), j)
                        res += int(j*(mn-n)/n)
                    #else:
                    #    #print(n, mn - n, int(M/mn), j)
                    #    res += int(M/mn) - 2*j
                    j+=1
                primer = floor(n*M/(mn * (mn + n)) + 1)
                ultimo = floor((M/mn - 1)/2)
                res += (ultimo - primer + 1)*(floor(M/mn) - primer - ultimo)
    return res


#assert full_checker2(M) == res
    
print("El resultado es: {}".format(res))
#print("El resultado es: {}".format(full_checker2(M)))
#print("El resultado es: {}".format(full_checker(M)))
print("The time spent is: {}".format(perf_counter()-t))
