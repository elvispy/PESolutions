#PE751
from time import perf_counter
from math import log10
from sympy import Rational, floor, Float

t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''
# b1 = [[2, 3], 2] # Interval open to the right



def fixed_point(interval, guess):
    # This algorithm will find a fixed point for the algorithm described in the problem
    if len(guess) >= 26:
        print(float(guess))
        return None
    interval[1] -= 1e-15
    low_end  = floor(interval[0]) * (1 + interval[0] - floor(interval[0]))
    high_end = floor(interval[1]) * (1 + interval[1] - floor(interval[1]))
    vals = []
    int_vals = []
    for x in range(floor(low_end), floor(high_end)+1):
        vals.append(floor(interval[0]) + (x/floor(interval[0]) - 1))
        int_vals.append(x)
    vals.append(interval[1])

    for i in range(len(int_vals)):
        if vals[i] <= float(guess + str(int_vals[i])) <= vals[i+1]:
            fixed_point([vals[i], vals[i+1]], guess + str(int_vals[i]))
    
class chain():
    f = lambda x: floor(x) * (1 + x - floor(x))
    def __init__(self, lis):
        if type(lis[0]) != list:
            lis = [lis]

        self.chains = [[Float(str(a)), Float(str(b))] for a, b in lis]
        self.secure = 1

    def advance_one(self):
        mychains = []
        last = [chain.f(self.chains[-1][0]), chain.f(self.chains[-1][1])]
        #decimal_place =  # round(log10(self.chains[0][1] - self.chains[0][0]))-1
        securebet = str(self.chains[0][0])[:self.secure+1] 
        #if str(self.chains[0][1])[abs(decimal_place)] == "1": securebet = securebet + '0'
        for x in range(floor(last[0]), floor(last[1]) + 1):
            first = [Float(securebet + str(x)), Float(securebet + str(x+1))] 
            lis = [first]
            for _ in range(len(self.chains)):
                lis.append([chain.f(lis[-1][0]), chain.f(lis[-1][1])])
            A = chain(lis)
            A.secure = A.is_consistent()
            if A.secure >= 0:
                mychains.append(A)
        return mychains

    def is_consistent(self):
        #for i in range(len(self.chains)-1):
        #    assert(chain.f(self.chains[i][0]) - self.chains[i+1][0] < 1e-10) 
        #    assert(chain.f(self.chains[i][1]) - self.chains[i+1][1] < 1e-10)
        #    assert(floor(self.chains[i][0]) == floor(self.chains[i][1]))
        guess = str(floor(self.chains[0][0])) + "." 
        for i in range(1, len(self.chains)):
            guess = guess + str(floor(self.chains[i][0]))
        #guess = guess.rstrip('0')
        if self.chains[0][0] != Float(guess): return  - 1
        #if not (self.secure == len(guess) - 1): return False
        return len(guess) - 1
# assertion block
# assert 2 == 2
res = chain([Float("2.0", 30), Float("2.9999999", 30)])
res = res.advance_one()
while len(str(res[0].chains[0][0])) < 25:
    new_res = []
    for el in res:
        new_res = new_res + el.advance_one()
    res = new_res.copy()

    

print("El resultado es: {}".format(res[0].chains[0][0]))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
