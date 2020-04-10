#PE91
from time import perf_counter
t = perf_counter()
res = 0
maxx = 50
for x1 in range(maxx+1):
    for y1 in range(maxx+1):
        for x2 in range(maxx+1):
            for y2 in range(maxx+1):
                if x1 + y1 == 0 or x2 + y2 == 0:
                    continue
                elif x1 == x2 and y1 == y2:
                    continue
                elif x1*x1 + y1*y1 == x1*x2 + y1*y2:
                    res+=1
                    
res += maxx*maxx
print("El resultado es {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
