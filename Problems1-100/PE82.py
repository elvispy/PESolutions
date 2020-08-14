#PE82
from time import perf_counter
t = perf_counter()
with open("p082_matrix.txt") as f:
    content = f.read()

rows = content.split("\n")[:-1]
data = [[int(i) for i in row.split(",")] for row in rows]


def minn(tabla, unvisited):
    for i in [j for j in tabla.keys() if j in unvisited]:
        if type(tabla[i][0]) == type(0):
            if 'm' in dir():
                if tabla[i][0] < m:
                    m = tabla[i][0]
                    res = i
            else:
                m = tabla[i][0]
                res = i
    return res
            
            

def dijkstra(ini, tipo = 1):
    if tipo != 1:
        ini = (0, 0)
    aux = len(data)
    unvisited = []
    for i in range(aux):
        for j in range(aux):
            unvisited.append((i, j))
    tabla = {i:["infty", ()] for i in unvisited}
    tabla[ini] = [0, ()]
    while unvisited:
        vertex = minn(tabla, unvisited)
        if tipo == 1:
            neighbors = set([(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]), (vertex[0], vertex[1] + 1)])
        else:
            neighbors = set([(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]), (vertex[0], vertex[1] + 1), (vertex[0], vertex[1]-1)])
        for el in neighbors:
            if (-1 < el[0] and el[0] < aux and -1<el[1] and el[1] < aux):
                if type(tabla[el][0]) != type(0) or tabla[vertex][0] + data[el[0]][el[1]] < tabla[el][0]:
                    tabla[el] = [tabla[vertex][0] + data[el[0]][el[1]], vertex]

        print("Lol", len(unvisited))
        unvisited.remove(vertex)
    if tipo == 1:
        return min([tabla[i][aux-1] for i in range(aux)])
    else:
        return tabla[aux-1][aux-1]
    
                        

res = []
for i in range(len(data)):
    print(i)
    res.append(dijkstra((0, i)))
res = min(res)
print(f"The result is: {res}")
print("The time spent is: {}".format(perf_counter()-t))
