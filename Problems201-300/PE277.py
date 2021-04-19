#PE277
from time import perf_counter
t = perf_counter()

def mcd(a, b):
    a = abs(a)
    b = abs(b)
    while max(a, b)%min(a, b) != 0:
        a, b = max(a, b)%min(a, b), min(a, b)

    return min(a, b)

def reduce(a, b):
    c = mcd(a, b)
    return [a//c, b//c]

class frac():
    
    def __init__(self, num, den):
        if den < 0:
            num *= -1
            den *= -1
        if den == 0:
            raise Exception("Not a valid fraction!")
        elif num == 0:
            self.num = 0
            self.den = 1
        else:
            self.num, self.den = reduce(num, den)

    def __repr__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        if type(other) == type(1):
            other = frac(other, 1)
        # a/b + c/d = (ad +bc)/bd
        return frac(self.num * other.den + self.den * other.num,
                    self.den * other.den)
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) == type(1):
            other = frac(other, 1)
        return frac(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __le__(self, other):
        if type(other) == type(0):
            other = frac(other, 1)
        return self.num * other.den <= self.den * other.num


class expression():

    def __init__(self):
        self.k = [1, 0]

    def __repr__(self):
        return "{} * k + {}".format(self.k[0], self.k[1])

    def apply_D(self):
        self.k = [self.k[0] * 3, self.k[1] * 3]

    def apply_U(self):
        self.k = [self.k[0] * frac(3, 4),
                  self.k[1] * frac(3, 4) + frac(-1, 2)]

    def apply_d(self):
        self.k = [self.k[0] * frac(3, 2),
                  self.k[1] * frac(3, 2) + frac(1, 2)]

    def show(self, val):
        return val * self.k[0] + self.k[1]


    

s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
s = s[::-1]

k = expression()

for c in s:
    if c == "d":
        k.apply_d()
    elif c == "D":
        k.apply_D()
    elif c == "U":
        k.apply_U()

#It so happens that they both have same denominator, so we want to solve
# (pk+q)/r in naturals, for p, q, r given integers
from math import log
p = k.k[0].num
q = k.k[1].num
n = k.k[0].den
p = p%n #Mod pow(2, 22)
phin = pow(2, log(n, 2) - 1) #Little fermat theorem here
p = pow(p, int(phin - 1), n) #The inverse, we are using that they are coprime
modk = (-q * p) % n
while k.show(modk) <= pow(10, 15): #If too small, add one mod more
    modk += n

def check(n): #To debud and check that indeed begins with the desired sequence
    if type(n) == type(frac(1, 1)):
        n = n.num
    while n != 1:
        if n%3 == 0:
            print("D", end = "")
            n /= 3
        elif n%3 == 1:
            print("U", end = "")
            n = (4*n++2)/3
        elif n%3 == 2:
            print("d", end = "")
            n = (2*n - 1)/3
res = k.show(modk)
print("\nEl resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
