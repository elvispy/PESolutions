#PE500
from time import perf_counter
t = perf_counter()
from math import log
num = [1] * 500500
#Open the first primes
with open("D:\\GITRepos\\PESolutions\\pprimes.txt", "r") as f:
    data = f.read()
    data = [int(i) for i in data.split("\n") if i]
    data = data[:500500]


def lstonum(lis):
    """Returns a number modulo 500500507, given a list of powers"""
    xd = 1
    for i in range(len(lis)):
        xd *= pow(data[i], pow(2, lis[i])-1)
        xd = xd%500500507
    return xd

def price(i, agg = True):
    if agg:
        return num[i] * log(2) + log(log(data[i]))
    else:
        return (num[i]-1) * log(2) + log(log(data[i]))

changed = True

while changed:
    changed = False
    aux = len(num) -1
    priceaux = price(aux, False)
    for j in range(aux + 1):
        if price(j) < priceaux:
            num[-1] -=1
            num[j] +=1
            changed = True
            if num[-1] == 0:
                num = num[:-1]
            break
            
print("El resultado es: {}".format(lstonum(num)))
print("The time spent is: {}".format(perf_counter()-t))

