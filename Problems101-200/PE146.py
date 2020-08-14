#PE146
from time import perf_counter
t = perf_counter()
'''The strategy of this problem is to check for modules to reduce computational time
For example, analyzing mod 7 we get that n = 3, 4 mod 7 in order to the numbers not to be multiples of 7'''
mods = [10, 220, 290, 430, 550, 620, 640, 920, 1130, 1180, 1270, 1340, 1390, 1460, 1550, 1600, 1810, 2090, 2110, 2180, 2300, 2440, 2510, 2720]
N = 150_000_000
def is_composite(n):
    #Returns True if n is composite, False if the test is inconslusive.
    #More tecnically, it tests if n is a Fermat pseudoprime for bases 2 and 3
    #According to OEIS, there is only one pair of twin fermat pseudoprimes of base 2
    
    if pow(2, n-1, n) != 1:
        return True
    if pow(3, n-1, n) != 1:
        return True
    return False

i = 0
res = 0
beware = 0
while 2730*i <= N:
    aux = [(2730*i + j)*(2730*i + j) for j in mods]
    rem = [1, 3, 7, 9, 13, 27]
    for el in aux:
        if any([is_composite(el + y) for y in rem]):
            pass
        else:
            if is_composite(el + 21):
                print([el+y for y in rem])
                res+= pow(el, 1/2)
            else:
                beware += 1

    i+=1
                
    
    


print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
