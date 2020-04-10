#PE59
from time import perf_counter
import enchant
d = enchant.Dict("en_US")
t = perf_counter()

def see_ratio(lis):
    a = ""
    for i in lis:
        a = a + chr(i)
    a = a.split(" ")
    a = [d.check(j) for j in a if j]
    return sum(a)/len(a)
with open("p059_cipher.txt", "r") as f:
    data = f.read()
data = data.split(",")
data = [int(dat) for dat in data if dat]
#ord will give you the unicode number
#chr will give you the ascii character
def checking():
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                unencrypted = [data[p] ^ [i, j, k][p%3] for p in range(len(data))]
                ratio = see_ratio(unencrypted)
                if ratio > 0.5:
                    return sum(unencrypted)

print("El resultado es: {}".format(checking()))
print("The time spent is: {}".format(perf_counter()-t))
