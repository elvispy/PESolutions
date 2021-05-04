#PE145
from time import perf_counter
t = perf_counter()

def ways(parity, lleva, z_allowed = True):
    c = 0
    if z_allowed:
        for i in range(10):
            for j in range(10):
                if (i+j)%2 == parity:
                    if (i+j > 9) == bool(lleva):
                        c+=1
                        #print(i, j)
    else:
        for i in range(1, 10):
            for j in range(1, 10):
                if (i+j)%2 == parity:
                    if (i+j > 9) == bool(lleva):
                        c+=1
                        #print(i, j)
    return c

def reversible(n):
    """Return the number of reversible elements with n digits"""
    res = 1
    if n%2 == 0:
        #If n is even, all pairs are (1, 0)
        for i in range(n//2):
            if i == 0:
                res *= ways(1, 0, False)         
            else:
                res *= ways(1, 0)
     
        return res
    else:
        #The only possibility is (1, 1).
        '''
        If the first is (0, 1) or (0, 0), then the first digit wont be
        odd.
        If the first digit it (1, 0), then the digit in the middle wont
        be odd.
        Also, the digit in the middle has to be different than (1, 1)
        as they are equal. This happens only when n = 4k+3

        '''

        if n%4 == 1:
            return 0

        res = 5 if n > 1 else 4 #there are 5 possibilities
        

        #Now the rest
        for i in range(n//2):
            if i%2 == 0:
                a, b = (1, 1)
            else:
                a, b = (0, 0)

            if i == 0:
                res *= ways(a, b, False)

            else:
                res *= ways(a, b)
        return res

def brute(n):
    '''
    For brute-force testing purposes
    '''
    c = 0
    evens = ["0", "2", "4", "6", "8"]
    for i in range(1, n):
        if i%10 != 0:
            aux = str(i + int(str(i)[::-1]))
            if any([(j in aux) for j in evens]):
                pass
            else:
                c+=1
    return c


def rev_below(n):
    #All reversible numbers with n digist or less
    return sum([reversible(i) for i in range(1, n+1)])
print(reversible(8))
#print("El resultado es: {}".format(rev_below(9)))
print("The time spent is: {:.3f}".format(perf_counter()-t))
