#PE346
from time import perf_counter
t = perf_counter()

#Repunit 111...11_a with n digits
rep = lambda a, n: sum([pow(a, i) for i in range(n)])

strong = [1]

a = 2
n = 3
M = pow(10, 12) #Max number allowed.
while rep(2, n) <= M:
    a = 2
    while rep(a, n) <= M:
        strong.append(rep(a, n))
        a += 1
    n+=1

print("I did it")
res = sum(set(strong))
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
