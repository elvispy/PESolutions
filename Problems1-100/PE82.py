#PE82
from time import perf_counter
t = perf_counter()
with open("p082_matrix.txt") as f:
    content = f.read()

rows = content.split("\n")[:-1]
data = [[int(i) for i in row.split(",")] for row in rows]
data2 = []
for i in range(len(data)):
    col = []
    for j in range(len(data[i])):
        col.append(data[j][i])
    data2.append(col)

def minn(col1, col2):
    #This function returns a list with the shortest path in
    #every index
    res = []
    for i in range(len(col1)):
        minalt = col2[i] + col1[i]

        if i > 0:
            #Here we need to take advantage of previous computations
            if res[-1][1]:
                if res[-1][0] - col1[i-1] == col1[i] + col2[i]:
                    res.append([res[-1][0] - col1[i-1], False])
                else:
                    res.append([res[-1][0] - col1[i-1], True])
            else:
                if res[-1][0] < col2[i]:
                    res.append([res[-1][0] + col1[i], False])
                else:
                    idxdown = 1
                    pathdown = col1[i]
                    while i + idxdown < len(col1):
                        pathdown += col1[i+idxdown]
                        if pathdown >= minalt:
                            break
                        elif pathdown + col2[i + idxdown] < minalt:
                            minalt = pathdown + col2[i + idxdown]

                        idxdown += 1

                    if minalt == col1[i] + col2[i]:
                        res.append([minalt, False])
                    else:
                        res.append([minalt, True])
                      
        else:
                 
            idxdown = 1
            pathdown = col1[i]
            while i + idxdown < len(col1):
                pathdown += col1[i+idxdown]
                if pathdown >= minalt:
                    break
                elif pathdown + col2[i + idxdown] < minalt:
                    minalt = pathdown + col2[i + idxdown]

                idxdown += 1

            if i == 0 and minalt < col1[0] + col2[0]:
                is_down = True
            else:
                is_down = False

            res.append([minalt, is_down])

    return [el[0] for el in res]

while len(data2) > 1:
    data2 = data2[:-2] + [minn(data2[-2], data2[-1])]


            

    


res = min(data2[0])
print(f"The result is: {res}")
print("The time spent is: {}".format(perf_counter()-t))
