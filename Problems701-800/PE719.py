#PE719
from time import perf_counter
t = perf_counter()
def is_S(n):
    maxx = n
    n = str(n)
    for i in range(3, pow(2, len(n)), 2):
        i = bin(i)[2:]
        while len(i) < len(n):
            i = '0' + i
        ant = n[0]
        lis = []
        for c in range(len(n)):
            if i[c] == '1':
                lis.append(int(ant))
                if c < len(n) - 1:
                    ant = n[c + 1]
            else:
                ant = ant + n[c+1]
        #print(lis)
        if pow(sum(lis), 2) == maxx:
            return True
    return False
 
def T(N):
    res = 0
    i = 1
    top = int(pow(N, 1/2)) + 1
    for i in range(1, top, 9):
        if is_S(i*i):
            res += i*i
        if is_S((i+8)*(i+8)):
            res += (i+8)*(i+8)
    '''
        
    while i*i <= N:
        if is_S(i*i):
            res += i*i
        i+=9
    i = 9
    while i*i <= N:
        if is_S(i*i):
            res+= i*i
        i+=9
    '''
    return res



res = T(pow(10, 12))
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
