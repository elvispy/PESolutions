#PE61
from time import perf_counter
t = perf_counter()

P3n = lambda n: int(n*(n+1)/2)
P4n = lambda n: n*n
P5n = lambda n: int(n*(3*n-1)/2)
P6n = lambda n: n*(2*n-1)
P7n = lambda n: int(n*(5*n-3)/2)
P8n = lambda n: n * (3*n-2)

L3n = [P3n(i) for i in range(1000) if len(str(P3n(i))) == 4]
L4n = [P4n(i) for i in range(1000) if len(str(P4n(i))) == 4]
L5n = [P5n(i) for i in range(1000) if len(str(P5n(i))) == 4]
L6n = [P6n(i) for i in range(1000) if len(str(P6n(i))) == 4]
L7n = [P7n(i) for i in range(1000) if len(str(P7n(i))) == 4]
L8n = [P8n(i) for i in range(1000) if len(str(P8n(i))) == 4]
L = [[], [], [], L3n, L4n, L5n, L6n, L7n, L8n]

#We will try to solve it by backtracking
sets = [8, 7, 6, 5, 4, 3]
result = [0, 0, 0, 0, 0, 0]

f2 = lambda num: int(str(num)[0] + str(num)[1]) 
def solve(sets):
    l = sum([j!=0 for j in sets])
    if l == 0:
        if result[-1]%100 == f2(result[0]):
            print("El resultado es: {}".format(sum(result)))
            
    elif l == 6:
        i = sets[0]
        sets[0] = 0
        for j in L[i]:
            result[0] = j
            solve(sets)
    else:
        for i in sets:
            lol = i
            idx = sets.index(i)
            for j in L[i]:
                if f2(j) == result[5-l]%100:
                    result[6-l] = j
                    sets[idx] = 0
                    solve(sets)
                    sets[idx] = lol
                

solve(sets)       

print("The time spent is: {}".format(perf_counter()-t))
