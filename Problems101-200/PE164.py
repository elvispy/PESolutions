#PE
from time import perf_counter
t = perf_counter()
'''
from pathlib import Path
path = Path(__file__).parent.parent / '2T_part1.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data = [int(i) for i in data if i]
'''
def create_dict():
    res = {}
    for i in range(10):
        for j in range(10-i):
            res[(i, j)] = 0
            res[(j, i)] = 0
    return res
def countNums(M, ress = True):
    if ress == True: # If true, return the sum
        summ = 0
        res = countNums(M-1, False)
        #print(res)
        for el in res.keys():
            #print(summ, el)
            summ += (9 - el[0] - el[1]) * res[el]
        return summ
    if M == 2: #Recursive base case
        res = create_dict()
        for el in res.keys():
            res[el] = 1
        return res
    elif M > 2:
        ant = countNums(M-1, False)
        res = create_dict()
        for el in ant.keys():
            for j in range(10-el[0] - el[1]):
                res[(j, el[0])] += ant[el]
        return res

def checker(M):
    ''' To check wheter countNums is working'''
    res = 0
    for n in range(int(pow(10, M-1)), int(pow(10, M))):
        can_sum = True
        for i in range(len(str(n)) - 2):
            if int(str(n)[i]) + int(str(n)[i+1]) + int(str(n)[i+2]) > 9:
                can_sum = False
                break
        if can_sum == True:
            res += 1
    return res


# assertion block
assert checker(3) == countNums(3)
assert checker(4) == countNums(4)
assert checker(5) == countNums(5)
res = countNums(20)
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
