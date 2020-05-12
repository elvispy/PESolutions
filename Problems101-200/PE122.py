#PE122
from time import perf_counter
t = perf_counter()

def minn(ii):
    global res
    global mk
    if ii%2 == 0:
        mk = finalres[ii//2 -1] + 1
        return None
    fixlen = len(res)
    if res[-1] >= ii/2:
        if ii-res[-1] in res and len(res) < mk:
            mk = len(res)
            #print(ii, res, mk)

    elif fixlen <mk:
        for i in range(fixlen-1, -1, -1):
            for j in range(fixlen-1, i-1, -1):
                aux = res[i] + res[j]
                if aux > res[-1] and (not (aux in res)) and aux < ii:
                    res.append(aux)
                    minn(ii)
                    res = res[:-1]

    
finalres = [0, 1]
for ii in range(3, 201):
    print(ii)
    res = [1, 2]
    mk = 2*len(bin(ii))
    minn(ii)
    finalres.append(mk)
    
print("The result is: {}".format(sum(finalres)))
print("TIme spent: {}".format(perf_counter()-t))
