#PE82
from time import perf_counter
t = perf_counter()

with open("p082_matrix.txt") as f:
    data = f.read()
data = data.split("\n")
mat = []
for i in data:
    mat.append(i.split(","))
mat = mat[:-1]
for i in range(80):
    for j in range(80):
        if j < 79:
            mat[i][j] = [int(mat[i][j]), -1, [-1, -1]]
        else:
            mat[i][j] = [int(mat[i][j]), int(mat[i][j])
res = 0
print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
