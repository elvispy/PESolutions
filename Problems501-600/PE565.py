#PE565
from time import perf_counter
t = perf_counter()
div_2016 = [2, 3, 4, 6, 7, 8, 9, 12, 14, 16, 18, 21, 24, 28, 32, 36, 56, 63, 72, 84, 96, 112, 126, 144, 168, 224, 252, 288, 336, 504, 672, 1008, 2016]

from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]

def allowed_pot(p, base_prime = 2017, maxx = pow(10, 11)):
    #Returns the minimal power of p such that p^pow makes the sum of divisord multiple of 2017
    if p == base_prime:
        return 0
    if p%base_prime != 1:
        for l in div_2016: #range(2, base_prime):
            if pow(p, l-1) > maxx:
                return 0
            if pow(p, l, base_prime) == 1:
                return l-1
            
    else:
        for l in div_2016: #range(2, base_prime):
            if ((pow(p, l)-1)//(p-1))%base_prime == 0:
                return l-1
            if pow(p, l-1) > maxx:
                return 0
        raise Exception("Cuidadin que no hemos concluido nada")

# If p > pow(10, 11/2) = 316227, then the mas allowed pot is == 1
#So, (p^2-1)/(p-1)

primes_with_powers = []   
i = 0
while data[i] < 316227:
    x = allowed_pot(data[i])
    if x > 0:
        primes_with_powers.append(pow(data[i], x))
        if pow(data[i], 2*x+1) < pow(10, 11):
            print("Not tight")

    i+=1

while True:
    try:
        if data[i]%2017==2016:
            primes_with_powers.append(data[i])
            if pow(data[i], 3) < pow(10, 11):
                print("Not tight")
    except IndexError:
        i-=1
        break
    i+=1

#Now we need to locate all the primes =-1 mod 2017 between pow(10, 8) and pow(10, 11)
'''
aux = pow(10, 8) + 2016 - pow(10, 8, 2017)

LIS = range(aux, pow(10, 11), 2017)

def is_prime(p):
    i = 0
    while data[i] <= pow(p, 1/2) + 1:
        if p%data[i] == 0:
            return False
        i+=1
    return True


new_LIS = []
for el in LIS:
    if is_prime(el):
        new_LIS.append(el)

for el in LIS:
    if (el%2 != 0) and (el%3 != 0) and (el%5 != 0) and (el%7 != 0) and (el%11 != 0):
        new_LIS.append(el)

new_new_LIS = []
for el in new_LIS:
    if pow(2, el-1, el) == 1:
        new_new_LIS.append(el)
'''
res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
