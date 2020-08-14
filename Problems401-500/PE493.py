#PE493
from time import perf_counter
t = perf_counter()

def Prob(C, R, i):
    #C is the number of colours remaining and i is the number of balls of one colour we're
    #expecting to draw from R remeaining draws
    #There are 10 balls of each colour initially.
    if i > R:
        return 0
    res = 1
    num1 = 1
    den1 = 1
    num2 = 1
    for j in range(i):
        num1 *= (10-j)*(R-j)/(j+1)
    for j in range(10):
        den1 *= (10*C - j)
    for j in range(10-i):
        num2 *= (10*C - R - j)

    return num1*num2/den1
        
        

def Expected(C, R):
    #Returns the expected number of distinct colours in an urn with 10*C balls and R draws

    
    #Small cases
    if R == 0:
        return 0
    if C == 1:
        if R > 10:
            return 0
        if R == 0:
            return 0
        else:
            return 1
    elif R == 1:
        return 1
    
    res = 0
    for i in range(min(11, R+1)):
        if  i == 0:
            res+= Prob(C, R, i)*Expected(C-1, R)
        else:
            res += Prob(C, R, i) * (1 + Expected(C-1, R-i))

    return res



res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
