#PE78

from time import perf_counter
t = perf_counter()
M = 1_000_000

dist = {i:{1:1} for i in range(1, 1_000_000)}

def p(n, ret = True):
    # Recursive definition of p, on the number of distributions with t
    #the highest value being m
    
    if len(dist[n]) < n:
        p(n-1, ret=False)
    for m in range(2, n):
        if m not in dist[n]:
            dist[n][m] = 0
        ii = n - m
        for jj in range(1, min(ii, m) + 1):
            dist[n][m] += dist[ii][jj]
    dist[n][n] = 1            
    
    if ret: return sum(dist[n].values())

dist2 = {0:{1:1}, 1:{1:1}}

def p2(n, ret = True):
    if n-1 not in dist2:
        p2(n-1, ret = False)
    if n not in dist2:
        dist2[n] = {i:0 for i in range(1, n+1)}
        for ii in range(1, n):
            if ii == 1:
                dist2[n][ii] = 1
            else:
                dist2[n][ii] = dist2[n][ii-1] + dist2[n-ii][min(n-ii, ii)]
        dist2[n][n] = dist2[n][n-1] + 1
    if ret: return dist2[n][n]

n = 1
while dist2[n][n]%M != 0:
    n+=1
    p2(n)
    if n%10_000 == 0: print(n)
print("El resultado es: {}".format(n))
#print({a:b for a, b in dist2.items() if a <= 8})
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))


    
