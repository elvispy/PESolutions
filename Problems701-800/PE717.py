#PE717
from time import perf_counter
import mpmath as mp

t = perf_counter()
mp.mp.dps = 100
mp.mp.pretty = True
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i and int(i) < pow(10, 7)]

data[0] = 0

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
'''
milis = [2]
for i in range(7):
    milis = [pow(milis[0], 10)] + milis


def poten(p):
    #"Efficient" way of calculating pow(2, p), using milis
    res = 1
    for i in range(-1, -len(str(p))-1, -1):
        res *= pow(milis[i], int(str(p)[i]))
    return res
'''
last = [8, 3]

def g(p, ant = 0):
    global last
    if ant == 0:
        m = pow(2, p)
    else:
        m = last[0] * pow(2, p - ant)
        last = [m, p]
    num = - pow(2, pow(2, p, p-1), p)
    
    res = modinv(p, m) * num
    return (res % m) % p

def G(N):
    res = 0
    for i in range(1, len(data)):
        if data[i] >= N:
            break
        
        res += g(data[i], data[i-1])

    return res

res = G(pow(10, 7))
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
