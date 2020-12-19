#PE733
from time import perf_counter
t = perf_counter()
a_is = [153]
counter = [0] * (10_000_019)
b_is = []
c_is = [0]
counter[153] = 1
while len(a_is) < pow(10, 6):
    
    val = (a_is[-1] * 153) % 10_000_019
    counter[val] += 1
    c_is.append(sum(counter[:val]))
    a_is.append(val)

res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
