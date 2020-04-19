#PE577
from time import perf_counter
t = perf_counter()

border = lambda n: 1 if n == 0 else 3*n

def hexagon(n: int) -> int:
    res = 0
    i = 1
    while 3*i <= n:
        res += i * border(n-3*i)
        i+=1
    return res


res = sum([hexagon(i) for i in range(3, 12346)])
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
