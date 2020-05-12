#PE94
#This algorithm is not working on Python, try PE94.cpp instead
#I left this archive undeleted to show it as an example where
#C++ is more efficient than Python
import time
start = time.perf_counter()
import mpmath as mp
mp.mp.dps = 30

r3 = mp.mpf(1.7320508075688772935274463415058723669428052538104)

def satisfies(x):
    val = mp.ceil(x*r3)
    val2 = mp.mpf(3*x*x+2*x-1)
    if val*val == val2:
        return True
    return False

def satisfies2(x):
    val = mp.floor(x*r3)
    val2 = mp.mpf(3*x*x-2*x-1)
    if val*val == val2:
        return True
    return False

x = 3
res = 0
while (x <= 333_333_333):
    if (satisfies(x)):
        res += 3*x-1
    if satisfies2(x):
        res+= 3*x+1
    x+=2
print(f"El resultado es {res}")
print(time.perf_counter()-start)
