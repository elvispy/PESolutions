#PE710
from time import perf_counter
t = perf_counter()
elmod = pow(10, 6)


sumRn = 3
Rant = [1, 1, 1, 2]
Sant = [1, 1, 1, 2]
TEven = 4 # = T(6)
TOdd = 3 # = T(7)
n = 4
while TEven != 0 and TOdd != 0:
    Rn = (Rant[-1] + Rant[-2] + Rant[-4]) % elmod
    Sn = (2*Sant[-1] + Rant[-2] - Rant[-3]) % elmod
    TEven = (Sn + pow(2, n-3, elmod) - Sant[-2] - Rant[-2]) % elmod
    TOdd = (Sn - Rant[-2])

    #Updates
    n+=1
    Rant = Rant[1:] + [Rn]
    Sant = Sant[1:] + [Sn]



if TEven == 0:
    res = 2 * (n-2)
else:
    res = 2 * n - 3
    

print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
