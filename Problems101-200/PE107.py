#PE107
from time import perf_counter
t = perf_counter()

from pathlib import Path
path = Path(__file__).parent / "p107_network.txt"
with open(path, "r") as f:
    data = f.read()
    data = data.split("\n")
    data2 = []
    for el in data:
        data2.append(el.split(","))

edges = []
total = 0
#Lets define the structures. Edges is a list contaning the weight
#and the two vertices
for i in range(len(data2)):
    for j in range(i+1, len(data2[i])):
        if data2[i][j] != "-":
            
            val = [int(data2[i][j]), set([i, j])]
            total+= val[0]
            for m in range(len(edges)):
                
                if edges[m][0] > val[0]:
                    edges = edges[:m] + [val] + edges[m:]
                    break
            else:
                edges.append(val)
        
def return_tree(i, f):
    #Returns the tree in the forst that contains the leaf i
    for e in f:
        if i in e:
            return e
    raise Exception("Cuidadin no se encuentra")
forest = [{i} for i in range(40)]
res = 0

for e in edges:
    val = e[0]
    if len(forest) != 1:
        v1, v2 = e[1]
        v1 = return_tree(v1, forest)
        v2 = return_tree(v2, forest)
        if v1 == v2:
            res+=val
        else:
            forest.remove(v1)
            forest.remove(v2)
            forest.append(v1.union(v2))
    else:
        res+=val
                
                
    

print("El resultado es: {}".format(res))
print("The time spent is: {}".format(perf_counter()-t))
