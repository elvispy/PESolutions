def is_good(a):
    a = str(a)
    l = sum([int(j) for j in a])
    for j in a:
        if 2*int(j) == l:
            return True
    return False

lis = []
N = 5
for i in range(10, int(pow(10, N))):
    if is_good(i):
        lis.append(i)
        
def sum_max(d):
    #Returns the sum of the numbers with maximum digit equal to d (not repeated)
    res = 0
    for a in lis:
        v = str(a)
        s = sum([int(j) for j in v])
        s //= 2
        if s == d and v.count(str(d)) == 1:
            print(a)
            res += a
    print("---")
    return res
def repeated_max():
    res = 0
    for a in lis:
        if str(a).count("0") == len(str(a)) - 2:
            res += a
    return res



import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2
