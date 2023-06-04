#PE689
from time import perf_counter
from math import pi, sqrt, floor
t = perf_counter()


# Recursive solution
def measure(prob, order = 1, max_order = 25, maximum = pi*pi/6, current = 0):
    if current + maximum <= prob:
        return 0
    elif max_order == order:
        estimator = floor((prob - current) * (max_order ** 2))
        return pow(2,-(order - 1)) * pow(2, -estimator)
    if current > prob:
        return pow(2, -(order-1))
    
    return measure(prob, order + 1, max_order, maximum-pow(order, -2), pow(order, -2) + current
                   ) + measure(prob, order + 1, max_order, maximum-pow(order, -2), current)
    
result = measure(0.5)

print("El resultado es: {}".format(result))
print("The time spent is: {}".format(perf_counter()-t))
