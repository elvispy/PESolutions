#PE191
from time import perf_counter
t = perf_counter()


def F(n, bol = True) -> int:
    """This function returns the number of acceptable strings that
    can be awarded with the prize in an n-day semester.
    """
    res = 0
    #Here some base cases
    if n == 0:
        return 1
    elif n == 1:
        if bol:
            return 3
        else:
            return 2
    elif n == 2:
        if bol:
            return 8
        else:
            return 4
    elif n == 3:
        if bol:
            return 22
        else:
            return 7


    if bol:
        #First we count the strings with one late arrival
        
        for i in range(n):
            res += F(i, False) * F(n-1-i, False)

        #Now strings with no late arrivals.
        res += F(n, False)

        return res
    else:
        #Recursion rules!
        return 2*F(n-1, False) - F(n-4, False)
        


res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
