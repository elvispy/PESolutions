#PE689
from time import perf_counter
from math import pi, sqrt, floor
t = perf_counter()

cont = lambda a: sum([pow(2, -len(el)) for el in a])

summ = lambda el: sum([pow(i+1, -2) for i in range(len(el)) if el[i]])

tail = lambda el: pi*pi/6 - summ([1] * len(el))
    

prec = pow(10, -2)
a = [[1], [0]]
p = 0
while cont(a) > prec:
    added = []
    for el in a:
        s = summ(el)
        t = tail(el)
        if s > 1/2:
            p+= pow(2, -len(el))
        elif s+t > 1/2:
            j = floor(sqrt(1/(s+t-1/2)))
            aux = [1] * (j - len(el))
            added.append(el+ aux + [0])
            added.append(el+ aux + [1])
    a = added
    print(cont(a))

print("El resultado es: {}".format(p))
print("The time spent is: {}".format(perf_counter()-t))
