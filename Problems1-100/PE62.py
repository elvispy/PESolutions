#PE62
from time import perf_counter
t = perf_counter()

def sett(a):
    #Returns a typle (we need lists!) with the characteristic of the number (two perm have the same characteristics)
    res = []
    for i in range(10):
        res.append(str(a).count(str(i)))

    return tuple(res)

def perms(target = 5, nbdig = 1, chute = 1):
    #This function returns
    # a) A list of cubes which are permutations of each other, if they have the length of target
    # and number of digits equal to nbdig
    #a) An integer if no cubes attained target but will serve as a guess from where to start next loop
    #c) False if something went wrong.
    maxs = {(0, 1, 0, 0, 0, 0, 0, 0, 0, 0):[1]}
    alls = dict()

    while True:
        a = pow(chute, 3)
        resset = sett(a)
        if sum(resset) == nbdig:
            if resset in alls.keys():
                alls[resset].append(a)
            else:
                alls.setdefault(resset,[a])

            if len(alls[resset]) > len(list(maxs.values())[0]):
                maxs = {resset:alls[resset]}
                if len(list(maxs.values())[0]) == target:
                    #print(maxs)
                    return list(maxs.values())[0]
            elif len(alls[resset]) == len(list(maxs.values())[0]):
                maxs.setdefault(resset, alls[resset])
            
        elif sum(resset) == nbdig + 1:
            return chute
        else:
            return False

        chute += 1
            
def result(target):
    #This function returns the minimum cube with the property of problem 62
    nbdig = 1
    chute = 1
    res = perms(target)
    while type(res) != type([]):
        if res == False:
            raise Exception("Check your code my friend.")
        elif type(res) == type(0):
            nbdig += 1
            chute = res
            res = perms(target, nbdig, chute)

    return min(res)

res = result(5)
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
