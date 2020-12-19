#PE125
from time import perf_counter
t = perf_counter()

N = pow(10, 8)
def is_pal(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-i -1]:
            return False
    return True

s = lambda n, l: (n*(n+1)*(2*n+1) - l*(l+1)*(2*l+1))//6

pals = []

l = 0
while s(l+2, l) < N:
    n = l+2
    while s(n, l) < N:
        pals.append(s(n, l))
        n+=1
    l+=1
pals = set(pals)
res = 0
for i in pals:
    if is_pal(i):
        #print(i)
        res += i
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
