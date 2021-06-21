#PE79
from time import perf_counter
t = perf_counter()
'''
Idk wth this script works
'''

from pathlib import Path
path = Path(__file__).parent / 'p079_keylog.txt'
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")[:-1]
    # data = [int(i) for i in data if i]
data = [list(i) for i in data]
knownMin = 10 * len(data[0])

def dynamic_check(data) -> int:
    res = 0
    while len(data) > 0:
        firsts = [el[0] for el in data]
        counter = [firsts.count(str(i)) for i in range(10)]
        maxx = max(counter)
        midx = str(counter.index(maxx))
        print(midx, end = '')
        res += 1
        data2 = []
        for el in data:
            if el == [midx]:
                continue
            elif el[0] == midx:
                data2.append(el[1:])
            else:
                data2.append(el)
        data = data2.copy()
        del data2
    return res




# assertion block
# assert 2 == 2
print("El resultado es: ", end='')
dynamic_check(data)

