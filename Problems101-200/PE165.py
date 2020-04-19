#PE165
from time import perf_counter
t = perf_counter()
sn = 290797
i = 1
ti = []
lines = []
while i <= 20_000:
    sn_1 = (sn * sn) % 50515093
    ti.append(sn_1%500)
    sn = sn_1
    if not i%4:
        lines.append([(ti[0], ti[1]), (ti[2], ti[3])])
        ti = []
    i+=1
res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
