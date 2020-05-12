#PE98
from time import perf_counter
from math import ceil, floor
t = perf_counter()
from pathlib import Path
path = Path(__file__).parent / 'p098_words.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split(",")
    data = [i[1:-1] for i in data if i]

def squares(w1, w2):
    """This function takes two words as inputs, and
    returns the maximum pair of squares that can be set to obey
    the rules of problem 98"""
    if len(w1) != len(w2) or set(w1) != set(w2):
        return 0
    for a in set(w2):
        if w2.count(a) != w1.count(a):
            return 0
    res = [0]
    l = len(w1)
    cotainf = ceil(pow(10, (l-1)/2))
    cotasup = floor(pow(10, l/2)) + 1
    for i in range(cotainf, cotasup):
        bijec = dict()
        aux = str(i*i)
        valid = True
        for j in range(l):
            bijec.setdefault(w1[j], aux[j])
            if aux[j] != bijec[w1[j]]:
                valid = False
                break
        if len(bijec.values()) != len(set(bijec.values())):
            valid = False
        if valid and bijec[w2[0]] != "0":
            num2 = ""
            for k in w2:
                num2 = num2 + bijec[k]
            num2 = int(num2)
            sq = pow(num2, 1/2)
            sq = int(sq)
            if sq*sq == num2:
                num1 = ""
                for k in w1:
                    num1 = num1 + bijec[k]
                num1 = int(num1)
                res.append(max([num1, num2]))
    return max(res)
    

res = 0
for i in range(len(data)-1):
    #print(i)
    for j in range(i+1, len(data)):
        aux = squares(data[i], data[j])
        if aux > res:
            res = aux
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
