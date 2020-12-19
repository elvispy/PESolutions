#PE297
from time import perf_counter
t = perf_counter()

fibbo = [1, 2, 3, 5]
S_k = [0, 1, 2, 5]

def idx(lis, val):
    #Returns the gre
    if val < lis[0]:
        return 0
    if val > lis[-1]:
        return len(lis)-1
    hi = len(lis)-1
    lo = 0
    guess = (hi + lo)//2
    while lo < hi:
        if lis[guess] < val:
            lo = guess
            guess = (hi + lo+1)//2
            if lis[lo + 1] > val:
                return lo
        elif lis[guess] > val:
            hi = guess
            guess = (hi + lo)//2
            if lis[hi-1] < val:
                return hi-1
        else:
            return guess
    while lis[guess] >= val:
        if guess == 0:
            return guess
        guess-=1
    return guess
        

def S(n, fib_known = [], S_k_known = []):
    if n < 0:
        raise Exception("Lolazo bro")
    #Returns the sum of s(k) for all  k < n
    while fib_known[-1] + fib_known[-2] <= n:
        S_k_known = S_k_known + [S_k_known[-1] + 1 + S_k_known[-2] + fib_known[-2] - 1]
        fib_known = fib_known + [fib_known[-1] + fib_known[-2]]
    #print(fib_known)
    #print(S_k_known)
    aux = idx(fib_known, n)
    #print(fib_known, n, aux)
    #return False
    if n == fib_known[aux]:
        return S_k_known[aux]
    else:
        return S_k_known[aux] + S(n-fib_known[aux], fib_known, S_k_known) + (n - fib_known[aux] - 1) + 1
    

res = S(pow(10, 17), fibbo, S_k) 
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
