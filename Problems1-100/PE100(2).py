#PE100
from time import perf_counter
import mpmath as mp
mp.mp.pretty = True
mp.mp.prec = 10000
t = perf_counter()
''' He let B the number of blue balls and T the total.
We have B = aT, where 0<a<1. The probability is equal to
(B/T) * (B-1)/(T-1) = 1/2, Replacing B = aT, and solving the
second order polynomial we see that a is integer iff
2T^2 + 2T + 1 = q^2, for some q odd. We again solve for integer solutions
and get that 2q^2-1 has to be a square, say k^2
2q^2 = k^2 + 1
Wolfram alpha XD Says that this is a diophantine equation with general solution
equal to
k = -1/2 * [(1+sqrt(2)) * pow(3-2*sqrt(2), n) + (1-sqrt(2)) * pow(3+2*sqrt(2), n)]

and we have the equality k = 2T + 1, we have that
k>= 2 * pow(10, 12) + 1
Also we have the relation B = ceil(T/sqrt(2))

'''
s2 = mp.sqrt(2)
f = lambda n: ((s2-1) * mp.power(3 + 2*s2, n) - (1+s2) * mp.power(3-2*s2, n))/2 + 2
kmin = 2 * pow(10, 12) + 1
i = 0

while f(i) < kmin:
    i+=1

g = lambda i: (f(i)-1)/2
h = lambda i: mp.ceil(g(i)/s2)


print("El resultado es: {}".format(h(i)))
print("The time spent is: {}".format(perf_counter()-t))
