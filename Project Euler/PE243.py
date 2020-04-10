#PE243
from time import perf_counter
t = perf_counter()
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
i =-1
a = 1
l = 1
while a > 15499/94744:
    i+=1
    l*=data[i]
    a *= (data[i]-1)/data[i]

rat_max = 15499/(94744*a)
n_min = 1/(rat_max-1)

#Since n_min/l is approximately 4.6, we need to multiply l by 4 to obtain at least n_min, so we can obtain a value less than 15499/94744
l = 4*l

print("la multiplicacion final sale {}".format(a*l/(l-1)))
print(a*l/(l-1) < 15499/94744)
print("The time spent is: {}".format(perf_counter()-t))
