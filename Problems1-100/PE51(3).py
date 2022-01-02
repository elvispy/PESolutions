#PE51
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
class nb():
    def __init__(self, n):
        if isinstance(n, int):
            n = list(str(n))
        self.digits = [(int(i) if i else None) for i in n ]

    @property
    def nb_to_int(self):
        return sum([10 ** (i) * val for i, val in enumerate(self.digits) if val])

    def __repr__(self):
        return "".join([(str(i) if i else "*") for i in self.digits[::-1]])

    def setter(self, tupp):
        for idx, val in tupp:
            self.digits[idx] = val
        print(self)


# assertion block
# assert 2 == 2

a = nb([1, 2, 3, None, 4])
a.setter([(1, 7), (2, None)])
res = 0
print("El resultado es: {}".format(a))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
