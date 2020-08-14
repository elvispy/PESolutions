#PE686
from time import perf_counter
t = perf_counter()
import mpmath as mp

def nextt(a, info = []):
    if type(a) == type(list()):
        res = []
        for i in a:
            res = res + nextt(i)
        return list(set(res))
    else:
        a = str(a)
        res = []
        if not info:
            info = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in info:
            aux = a + i
            aux = int(aux)
            aux *= 2
            res.append(str(aux)[:3])
        return list(set(res))

ini = 123

res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
