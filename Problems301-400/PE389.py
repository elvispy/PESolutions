#PE389
from time import perf_counter
t = perf_counter()


# PE 389
import numpy as np

"""
This problem may be solved by noting that the measurable space may be divided into subspaces in which
every subset is the sum of j i.i.d. n-sided die. The distribution of this sum is the j-convolution 
of a n-sided die.
where p_1 is the probability of throwing j dice, and Dn is the distribution of an n-th sided die: Var(Dn) = (n^2-1)/12
"""

dice = [4, 6, 8, 12, 20]

# data[i][j] is the probability distribution of rolling j i-sided dices. (beginning at zero)
data = {dice[0]:{1:np.array([0.0] + [1/dice[0]] * dice[0], dtype=np.float64)}}
m = dice[0]
data[dice[0]]["total"] = data[dice[0]][1]
data[dice[0]][0] = np.array([1.0] + [0.0] * dice[0], dtype = np.float64)

for idx, item in enumerate(dice):
    if idx > 0:
        for el in range(m+1):
            if el == 0:
                data[item] = dict()
                data[item][0] = np.array([1.0] + [0.0] * item, dtype = np.float64)

            elif el == 1:
                data[item][1] = np.array([0.0] + [1/item] * item, dtype = np.float64)
                
            else:
                data[item][el] = np.convolve(data[item][el-1], data[item][1])

        m *= item
    #dice[item][0] is the probability distribution of the dices thrown
    if 0 < idx:
        l = sorted(data[item].values(), key=len)
        ss = np.zeros(l[-1].shape, dtype = np.float64)
        previous_total = data[dice[idx-1]]["total"]
        for nb_sum in range(len(previous_total)):
            ss[:len(data[item][nb_sum])] += data[item][nb_sum] * previous_total[nb_sum]
        
        data[item]["total"] = ss.copy()

EX2 = 0
E2X = 0
for nb_sum in range(len(data[dice[-1]]["total"])):
    E2X += data[dice[-1]]["total"][nb_sum] * (nb_sum**2) 
    EX2 += data[dice[-1]]["total"][nb_sum] * nb_sum 
EX2 = EX2**2
total_variance = E2X - EX2

res = total_variance

print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
