#PE148
from time import perf_counter
from math import floor, log
t = perf_counter()

m7 = lambda i: int(pow(28, i)) #Gives the result when n is of the form pow(7, i)
#this is due to the fractal nature of the problem

def b7(n:int) -> list:
    #Returns a list with the base7 conversion of n
    
    n = int(n)
    aux = log(n)/log(7)
    aux = floor(aux)
    lis = [0] * (aux+1)
    for i in range(aux, -1, -1):
        while pow(7, i) <= n:
            n-= pow(7, i)
            lis[i] +=1
    return lis

def general(n):
    #Now calculates the general solution
    n = int(n)
    lis = b7(n)
    res = 0
    end = 1
    for i in range(len(lis)-1, -1, -1):
        #Beginning with the greatest power of 7, calculates how many
        #non multiples of 7 are in that part. 
        res += end * m7(i) * lis[i] * (lis[i] + 1)/2
        if lis[i]:
            #Calculates how many ends does the new part have.
            end *= lis[i] + 1
    return int(res)
res = general(pow(10, 9))
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
