import math
from time import perf_counter
t = perf_counter()
N = 10_000

def gcd(lis):
    lis = list(lis)
    if len(lis) == 2:
        a = max(lis)
        b = min(lis)
        while a%b:
            lis = [a - b, b]
            a = max(lis)
            b = min(lis)
        return b
    
    rest = lis[2:]
    return gcd([gcd([lis[0], lis[1]])] + rest)

def nextFrac(n, a = 1, c = 0, d = 1):
    """Recieves n, a, c, d and returns
    a list with the values of ai, a, c, d"""
    b = math.sqrt(n)
    
    try:
        ai = (a*b + c) // d
        vals = [d*a, d*(ai*d-c), a*a*n-(c-ai*d)**2]
        g = gcd(vals)
        vals = [int(i/g) for i in vals]
    except:
        print(ai, a, c, d)
        Exception("Something went wrong")

    return [ai] + vals

def calc_period(n):
    firstfrac = nextFrac(n)
    contFrac = []
    while True:
        firstfrac = nextFrac(n, firstfrac[1], firstfrac[2], firstfrac[3])
        contFrac.append(firstfrac)
        if len(contFrac)%2 == 0:
            l = len(contFrac) // 2
            has_period = True
            if contFrac[l-1] != contFrac[2*l-1]:
                has_period = False
            else:
                for i in range(l-1):
                    if contFrac[i][0] != contFrac[i+l][0]:
                        has_period = False
                        break
            if has_period:
                return l
                    
                
    
    

def contFrac(n, k = 100, simple = False):
    cf = []
    a = 1
 
    c = 0
    d = 1
    ai = 0

    for i in range(k):
        ai, a, c, d = nextFrac(n, a, c, d)
        cf.append([ai, a, c, d])
        
    if simple == False:
        return cf
    else:
        return [a[0] for a in cf]
# Usage

res = 0
for i in set(range(1, N+1)) - set([i*i for i in range(int(math.sqrt(N)) +2)]):
    res += calc_period(i)%2

print(f"El resultado es: {res}")
print("Tiempo tomado: {}".format(perf_counter()-t))
