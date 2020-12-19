#PE725
from time import perf_counter
t = perf_counter()
N = 3
MM = pow(10, 16)

#NO FUNCIONA!!! :(

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2



def take(n, r):
    #returns the number of ways we can distribute r equal balls into n
    #distinct boxes
    if r == 0:
        return 1
    if n == 0:
        return 0
    
    return ncr(n+r-1, n-1) % MM

def nb(n, r):
    '''Return the number of ways of distributing r balls into n boxes
    in such a way that no single box contain all the r balls'''
    if r == 0:
        return 1
    if n == 0:
        return 0
    
    return (take(n, r) - n) % MM

def sumd(n, r):
    ''' Return the sum of the digits in every position in the nb(n, r)
    ways of distributing r balls into n boxes without allowing all balls
    to be in one place'''
    if n == 0 or r == 0:
        return 0
    return ((r*(take(n, r) - n))//n) % MM

def sumd2(n, r):
    ''' Return the sum of the digits in every position in the take(n, r) ways
    of distributing r balls into n boxes '''

    if n == 0 or r == 0:
        return 0
    return ((r*take(n, r))//n) % MM

def F(n, j, d):
    '''Returns the total sum of numbers with n digits with total sum of the
    digits equal to j and d-offset to the left without allowing all digits
    to be in one place'''

    return (sumd(n, j) * (pow(10, n) - 1) * pow(10, d) // 9) % MM


def F2(n, j, d):
    '''Returns the total sum of numbers with n digits with total sum of the
    digits equal to j and d-offset to the left '''
    

    return (sumd2(n, j) * (pow(10, n) - 1) * pow(10, d) // 9) % MM

res = 0
for k in range(2, 10):
#the value of the biggest digit
    #print("Lets begin with ", k)
    for m in range(1, N+1):
        # The position of the biggest digit
        for p in range(0, k+1):
            #the sum of the digits to the right of the biggest digit

            if p in [0, k]: #the biggest digit is on the side
                #first the contribution of the digit in the m-th position
                res += pow(10, m-1, MM) * nb(m-1, p) * nb(N-m, k-p) * k

                #Contribution to the right
                res += F(m-1, p, 0) * nb(N - m, k-p)

                #Contribution to the left
                res += F(N - m, k-p, m) * nb(m-1, p)
                #print("Here!")

            else:# not distributed "equally"

                #first the contribution of the digit in the m-th position
                res += pow(10, m-1) * take(m-1, p) * take(N - m, k-p) * k

                #Contribution to the right
                res += F2(m-1, p, 0) * take(N - m, k-p)

                #Contribution to the left
                res += F2(N - m, k-p, m) * take(m-1, p)
                #print("hum")

            res %= MM
        #print(res, m)

'''
for k in range(1, 10):
    val = (N-1) * k * sum([pow(10, i) for i in range(N)])
    val %= MM
    res += val
'''
val = 45 * (N-1) * (pow(10, N)-1) //9
val %= MM
res += val

res %= MM



print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
