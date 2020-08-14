#PE117
from time import perf_counter

t = perf_counter()
def F(k):
    if k< 0:
        return 0
    elif k<2:
        return 1
    elif k == 2:
        return 2
    elif k == 3:
        return 4
    else:
        aux = k//2
        data = [F(aux), F(aux-3), F(aux-2), F(aux-1)]
        if k%2==0:
            return pow(data[0], 2)+ pow(data[-1], 2) + 2*data[-1]*data[-2] + pow(data[-2], 2) + 2*(data[-1]*data[-3])
        else:
            return pow(data[0], 2) + 2*(data[0] * data[-1]) + pow(data[-1], 2) + 2*data[0] * data[-2] + 2*data[0]*data[-3] + 2*data[-1]*data[-2]
print("HOla misamigos") 
print("El resultado es: {}".format(F(50)))
print("The time spent is: {}".format(perf_counter()-t))
