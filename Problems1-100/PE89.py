#PE89
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent / 'p089_roman.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    #data = [i[1:-1] for i in data if i]

mydict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def rmn_to_nb(s):
    if len(s) == 1:
        return mydict[s]
    res = 0
    for el in range(len(s)-1):
        if mydict[s[el]]>= mydict[s[el+1]]:
            res+= mydict[s[el]]
        else:
            res-= mydict[s[el]]
    return res + mydict[s[-1]]

def nb_to_rmn(n):
    if n == 0:
        return ""
    elif n >= 1000:
        return "M" + nb_to_rmn(n-1000)
    elif n >= 900:
        return "CM" + nb_to_rmn(n-900)
    elif n >= 500:
        return "D" + nb_to_rmn(n-500)
    elif n >= 400:
        return "CD" + nb_to_rmn(n-400)
    elif n >= 100:
        return "C" + nb_to_rmn(n-100)
    elif n >= 90:
        return "XC" + nb_to_rmn(n-90)
    elif n >= 50:
        return "L" + nb_to_rmn(n-50)
    elif n >= 40:
        return "XL" + nb_to_rmn(n-40)
    elif n >= 10:
        return "X" + nb_to_rmn(n-10)
    elif n == 9:
        return "IX"
    elif n >= 5:
        return "V" + nb_to_rmn(n-5)
    elif n == 4:
        return "IV"
    elif n >=1:
        return "I" + nb_to_rmn(n-1)
res = 0
for el in data:
    if rmn_to_nb(el) != rmn_to_nb(nb_to_rmn(rmn_to_nb(el))):
        print(el)
    res -= len(nb_to_rmn(rmn_to_nb(el))) - len(el)

print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
