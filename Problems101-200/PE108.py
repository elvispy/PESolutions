#PE108
from time import perf_counter
from mpmath import log, exp, nint
import mpmath as mp
mp.mp.pretty = True
mp.mp.dps = 50
t = perf_counter()


primes = [ 2,         3,         5,         7,        11,        13,        17,        19 ,

        23,        29,        31,        37,        41,        43,        47,        53, 

        59,        61,        67,        71,        73,        79,        83,        89 ]
primes = [log(i) for i in primes]
'''
Teoric considerations
We will show that the number of solutions of 1/x+1/y=1/n is equal to the number of solutions for
x*y*z = n, with gcd(x, y) = 1

That formula can be derived.
F(alfa1, alfa2, \dots, alfan) = \sum 2^(|A|-1) \prod_x\inA x
where the summation is over all subsets of {alfa1, alfa2, \dots, alfan}

Then I divide all tuples into subsets, groping them by
1) Number of elements
2) Sum of the elements

And find the optimal element in every subset
'''

def lst_to_nb(el, exact = False):
    #Devolve o logaritmo do numero com os expoentes na lista el
    if exact:
        res = 1
        for i in range(len(el)):
            res *= pow(nint(exp(primes[i])), el[i])
    else:
        #print(el)
        res = 0
        for i in range(len(el)):
            #print(primes[i], el[i], res)
            res += primes[i]* el[i]
        
    
    return res



def F(alfa_is):
    '''
    Devolve a quantidade de soluções para 1/x + 1/y = 1/n onde
    n = \prod pow(p_i, alfa_is[i])
    '''
    if len(alfa_is) == 0:
        return 1
    res = 1
    for i in alfa_is:
        res = (res-1) * (2*i+1) + (i+1)
    
    return res



def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def dist(N, r):
    '''
    Returns the distributions of N+r identical objects into N identical boxes with no box empty.
    '''
    res = []
    for i in accel_asc(r):
        if len(i)>N:
            continue
        else:
            i = [j+1 for j in i] + [1] * (N - len(i))
            res.append(sorted(i, reverse = True))
    return res

v = 40#lst_to_nb([3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])

def G(N, S, M, minn = v):
    '''
    Devolve o menor valor para log(n) < v
    tal que (A) F(a1, a2, ... ,an) >= M com (B) \sum a_n = S
    n = \prod pow(p_i, alfa_is[i])

    Devolve -1 se a menor tupla satisfazendo (B) e maior que v
    Devolve 0 se a maior tupla satisfazendo (B) satisfaz F(alfas) < M
    ou se S < N.

    Devolve minn se o menor log(n) nao e melhorado
    Se nao, devolve minn', o logaritmo de log(n) melhorado.
    '''
    if S < N:
        return 0

    #We check if the minimum is good
    v = [(S-N + 1)] + [1] * (N-1)
    if lst_to_nb(v) > minn:
        return -1

    #First we check if the maximum is good
    alfas = [S//N] * N
    Sp = S%N
    for i in range(Sp):
        alfas[i] += 1
    if F(alfas) < M:
        return 0
    
    
    #Now lets check the optimal element
    dists = dist(N, S-N)
    for el in dists:
        if lst_to_nb(el) > minn:
            continue
        elif F(el) <= M:
            continue
        else:
            minn = lst_to_nb(el)
    
    return minn


#M = 1_000 # For PE108
M = 4_000_000 # For PE110
N = 1
S = N


while True:
    
    X = G(N, S, M, v) #Tentamos melhorar no grupo N, S
    if X > 0: #Se nao empioramos
        v = X #Atualizamos o valor
    elif X == -1:#Se -1, o menor possivel e maior que o valor otimo ja obtido, entao nao adianta
        if S == N:#Se sao iguais entao significa que qualquer N e S maiores vai ser maior tambem ao valor obtido, saimos
            break
        else: #Se nao sao iguais entao para S maior ainda vai ser maior ao otimo, entao aumentamos N.
            
            N+=1
            S = N-1
    
    S+=1 #AUmentamos S


    
res = nint(exp(v)) #Devolvemos o logaritmo a numero

print("El resultado es: {}".format(res))
print("The time spent is: {:.3f} seconds".format(perf_counter()-t))
