#PE101
from time import perf_counter
t = perf_counter()

def simplify(num, den):
    
    a = max(abs(num), abs(den))
    b = min(abs(num), abs(den))
    if abs(num) <= 0:
        return [0, 1]
    if abs(den)<=0:
        raise Exception("Denominador no puede ser cero")
    while a > b and b > 0:
        a, b = max(a%b, b), min(a%b, b)
    assert num/a == int(num/a)
    if den < 0:
        a = -a
        
    return [int(num/a), int(den/a)]

def int2rat(other):
    try:
        other.den
        return other
    except AttributeError:
        i = 0
        while int(other) != other and i < 100:
            other *=10
            i+=1
        return rational(other, pow(10, i))
    raise Exception("Cuidadin bro")

class rational:

    def __init__(self, num, den):
        #Sign always on the numerator
        self.num, self.den = simplify(num, den)
        
    def __repr__(self):
        
        if self.den == 1:
            res = str(self.num)
        else:
            res = "{}/{}".format(self.num, self.den)
        return res

    def __add__(self, other):
        other = int2rat(other)
        return rational(self.num*other.den+self.den*other.num, self.den*other.den)

    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        other = int2rat(other)
        return rational(self.num*other.num, self.den*other.den)
            
   
    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, real):
        aux = int2rat(pow(self.den, real))
        aux = rational(aux.den, aux.num)
        return int2rat(pow(self.num, real)) * aux

    def __abs__(self):
        return abs(self.num/self.den)

    def __eq__(self, other):
        return (self.num == other.num) and (self.den == other.den)


class Polynomial:

    def __init__(self, coefs):
        self.coefs = [int2rat(i) for i in coefs]


    def __call__(self, val):
        try:
            res = [0] * len(val)
            for j in range(len(val)):
                i = 0
                for coef in self.coefs:
                    res[j] += coef*pow(val[j], i)
                    i+=1
                    
        except TypeError:
            
            i = 0
            res = 0
            for coef in self.coefs:
                res+= coef*pow(val, i)
                i+=1
        return res

    def __add__(self, other):
        if len(self.coefs) > len(other.coefs):
            aux1 = self.coefs
            aux2 = other.coefs + [rational(0, 1)] * (len(self.coefs) - len(other.coefs))
        elif len(self.coefs) < len(other.coefs):
            aux1 = self.coefs + [rational(0, 1)] * (len(other.coefs) - len(self.coefs))
            aux2 = other.coefs
        else:
            aux1 = self.coefs
            aux2 = other.coefs
        res = list()
        for j in range(len(aux1)):
            res = res + [aux1[j] + aux2[j]]

        return Polynomial(res)
    def __mul__(self, other):
        res = [rational(0, 1)] * (len(self.coefs) + len(other.coefs) - 1)
        for i in range(len(self.coefs)):
            for j in range(len(other.coefs)):
                res[i+j] += self.coefs[i]*other.coefs[j]
        #res = [int(lol) for lol in res]
        return Polynomial(res)

    def __rmul__(self, other):
        return self.__mul__(other)
    def __repr__(self):

        #We begin with the isolated term
        res = str(self.coefs[0])
        
        
        for i in range(1, len(self.coefs)):
            if abs(self.coefs[i]) <= 0:
                continue
            res = res + " + {}*x^{}".format(self.coefs[i], i)
        if abs(self.coefs[0]) <= 0:
            res = res[4:]
        return res


    @staticmethod
    def interpolate(points):
        res = Polynomial([0])
        for i in range(len(points)):
            aux = Polynomial([1])
            for j in range(len(points)):
                if i == j:
                    aux *= Polynomial([points[i]])
                else:
                    aux *= Polynomial([-j-1, 1])
                    aux *= Polynomial([rational(1, i-j)])
            res += aux

        return res



oriPol = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
points = oriPol(range(1, 12))
print(points)
bestPols = [Polynomial.interpolate(points[:i]) for i in range(1, len(points)+1)]
res = 0
for pol in bestPols[:-1]:
    print("Grado {}: {}".format(len(pol.coefs)-1, pol(range(1, 12))))
    i = 1
    while pol(i) == oriPol(i):
        i+=1
    res+= pol(i)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
