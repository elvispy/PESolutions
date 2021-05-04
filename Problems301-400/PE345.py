matrix = [[7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
          [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
          [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
          [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
          [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
          [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
          [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
          [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
          [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
          [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
          [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
          [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
          [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
          [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
          [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]]
#An element is not usable if there is another element in its same row/column which is always better as a permutation element.
usable = []
for i in range(len(matrix)):
    usable.append([])

    for j in range(len(matrix[i])):
        usable[i].append(True) #They are all usable to begin with


def compare(matrix, c1, c2): #Compare if two cells at positions c1, c2 are comparable
    history = list()
    if c1[0] == c2[0]:
        for i in range(len(matrix)):
            if i != c1[0]:
                condition = (matrix[c1[0]][c1[1]] + matrix[i][c2[1]] > matrix[c2[0]][c2[1]] + matrix[i][c1[1]])
                history.append(condition)
        if all(history) and (len(history) > 0):
            return True
        elif (not any(history)) and (len(history) > 0):
            return False
        else:
            return None
    elif c1[1] == c2[1]:
        for i in range(len(matrix)):
            if i != c1[1]:
                condition = (matrix[c1[0]][c1[1]] + matrix[c2[0]][i] > matrix[c2[0]][c2[1]] + matrix[c1[0]][i])
                history.append(condition)
        if all(history) and (len(history) > 0):
            return True
        elif not any(history) and (len(history) > 0):
            return False
        else:
            return None
    else:
        raise Exception("THey should share at least one row or column!")



def chosen(matrixx, usablee, i, j):
    #Returns a matrix without the ith row and jth column
    res = []
    n_usable = []
    for el in range(len(matrixx)):

        if el != i:
            res.append(matrixx[el][0:j] + matrixx[el][(j+1):])
            n_usable.append(usablee[el][0:j] + usablee[el][(j+1):])
    return res, n_usable

def update_usable(matrix, usable):
    #We put false whenever we know we cant use an element.
    sz = len(matrix)

    for i in range(sz):
        for j in range(sz):
            if usable[i][j]:
                for k in range(sz):
                    if k != i and usable[k][j]:
                        res = compare(matrix, (i, j), (k, j))
                        if res != None:
                            if res == False:
                                usable[i][j] = False
                            elif res == True:
                                usable[k][j] = False

                    if k != j and usable[i][k]:
                        res = compare(matrix, (i, j), (i, k))
                        if res != None:
                            if res == False:
                                usable[i][j] = False
                            elif res == True:
                                usable[i][k] = False

    return usable

def tentative(matrix):
    #We try a naive tentative
    return sum([max(el) for el in matrix])


usable = update_usable(matrix, usable)
#Find tentative valid max:
equis = matrix.copy()
de = usable.copy()
maxx = 0
while len(equis) > 1:
    tent = max([equis[0][j] for j in range(len(equis[0])) if de[0][j]])
    idx = equis[0].index(tent)
    equis, de = chosen(equis, de, 0, idx)
    #for el in equis:
    #    print(el)
    #print(tent)
    maxx+=tent
maxx += equis[0][0]
maxx = [0]

def recursive_sol(my_matrix, my_usable, bynow = 0):

    if len(my_matrix) == 1:
        if my_matrix[0][0] + bynow > maxx[0]:
            maxx[0] = my_matrix[0][0] + bynow
    elif len(my_matrix)%3 == 0:
        if tentative(my_matrix) + bynow <= maxx[0]:
            return None
        
    sz = len(my_matrix)
    #usable = update_usable(matrix, usable)
    min_R = min([sum(el) for el in usable]) #Row with least booleans
    min_C = min([sum([my_usable[i][j] for i in range(sz)]) for j in range(sz)]) #Column with least booleans

    if min(min_R, min_C) == 0:
        return 0
    else:
        if min_R < min_C:
            idx = [sum(el) for el in my_usable].index(min_R)
            for i in range(sz):
                if my_usable[idx][i]:
                    equis, de = chosen(my_matrix, my_usable, idx, i)
                    recursive_sol(equis, de, bynow + my_matrix[idx][i])
        else:
            idx = [sum([my_usable[i][j] for i in range(sz)]) for j in range(sz)].index(min_C)
            for i in range(sz):
                if my_usable[i][idx]:
                    equis, de = chosen(my_matrix, my_usable, i, idx)
                    recursive_sol(equis, de, bynow + my_matrix[i][idx])

recursive_sol(matrix, usable)

print(f"The result is {maxx[0]}")



