#PE
import json
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
class structure:
    def __init__(self, empty = False):
        self.struc = {}
        for i in range(10):
            for j in range(i, 10):
                aux = (i, j)
                self.struc[aux] = {}
                for k in range(i, j+1):
                    if i == j and empty  == False:
                        self.struc[aux][k] = 1
                    else:
                        self.struc[aux][k] = 0
        del self.struc[(0, 0)] #There are no pandigital numbers only using the zero character!

    def __repr__(self):
        res = ""
        for key in self.struc:
            res = res + f"({key[0]}, {key[1]}): "
            for digit in self.struc[key]:
                res = res + f"{digit}:{self.struc[key][digit]}, "
            res = res + f", total = {sum(self.struc[key].values())}"
            res = res + "\n"
        return res
    @property
    def pandigital(self):
        #for key in self.struc[(0, 9)]:
        #    print(key, self.struc[(0, 9)][key])
        return sum(self.struc[(0, 9)].values())

    def copy(self, other):
        for key in other.struc:
            for digit in other.struc[key]:
                self.struc[key][digit] = other.struc[key][digit]
        


def special(n):
    # Returns the number of pandigital one-step numbers below 10^n
    res = 0
    a = structure()
    for i in range(1, n):
        b = structure(True)
        for key in a.struc:
            for digit in a.struc[key]:
                if digit == 0:
                    b.struc[key][digit + 1] += a.struc[key][digit]
                elif key == (9, 9):
                    b.struc[(8, 9)][8] += a.struc[key][digit]
                elif digit == 9:
                    b.struc[key][digit - 1] += a.struc[key][digit]
                else:
                    b.struc[(min(key[0], digit-1), key[1])][digit-1] += a.struc[key][digit]
                    b.struc[(key[0], max(key[1], digit + 1))][digit+1] += a.struc[key][digit]
        a.copy(b)
        res += a.pandigital
    #print(n)
    #print(a)
    #print("--------------------")

    return res


# assertion block
assert special(1) == 0
assert special(2) == 0
assert special(3) == 0
assert special(10) == 1
assert special(11) == 4

res = special(40)
print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
