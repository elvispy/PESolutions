
import mpmath as mp
mp.mp.pretty = True
mp.mp.dps = 100
mod = mp.power(10, 9)
def sumsq(num, k):
    lacon = mp.mpf(2_000_000_001/3)
    e1 = mp.ceil((num+0.5)/(k+1))-1;
    
    e1 = e1%mod
    val1 = (e1*(e1+1)/2)%mod 
    val1 = ((2*e1+1)* val1) %mod
    val1 = (val1*lacon)%mod;

    e2 = mp.ceil((num+0.5)/k)-1;
    e2 = e2%mod;
    val2 = (e2*(e2+1)/2)%mod
    val2 = ((2*e2+1)* val2)%mod;
    val2 = (lacon*val2)%mod
    
    res = (k*(val2-val1))%mod
    #print(val2-val1)
    return res

n = mp.power(10, 15)

for i in range(1, 10):
    print(sumsq(n, i))

