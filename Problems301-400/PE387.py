#PE
from time import perf_counter
t = perf_counter()
def is_p(n):
    #Weak primality test (it happens to be enough, but I had a plan b)
    n = int(n)
    if n in [2, 3, 5, 7]:
        return True
    if pow(2, n-1, n) != 1:
        return False
    if pow(3, n-1, n) != 1:
        return False
    return True

def strong_Harshad(n):
    #Check whether n is strong Harshad prime
    n = int(n)//sum([int(i) for i in str(n)])

    return is_p(n)
dig = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def Harshad(N):
    #Determines the number of Strong, right truncatble harshad numbers with no more than N digits.
    #It does it recursively, calculating the list of right truncatable Harshad numbers with N-1 digits first.
    pot = dig + []
    candidates = []
    while len(pot[0]) < N:
        newpot = []
        for elem in pot:
            newpot.append( elem + "0")
            for d in dig:
                if is_p(elem + d):
                    if strong_Harshad(elem):
                        candidates.append(elem + d)
                else:
                    j = sum([int(i) for i in elem + d])
                    k = int(elem + d)
                    if k%j == 0:
                        newpot.append(elem + d)
        pot = newpot + []

    
    print(len(candidates))        
            
    return sum([int(i) for i in candidates])




res = Harshad(14)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
