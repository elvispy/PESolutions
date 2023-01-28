#PE51
from time import perf_counter
from itertools import combinations
t = perf_counter()

with open("pprimes.txt", "r") as f:
    data = f.read()
data = [ int(j) for j in data.split("\n")[:-1]]
# We know that for a 8-member family of primes has to have a number of 
# digits that are wildcards which is a multiple of three, 
# so it has to be 3, 6, 9, 12 etc

def check_family(nb_of_digits):
    # Check if there's a 8-member family of primes with exactly nb_of_digits digits.
    # We divide in the number of possible wildcards, which has to be multiple of three
    value_to_return = False
    for nb_of_wildcards in [3*k for k in range(1, (nb_of_digits+2)//3)]:

        allowed_positions = combinations(range(nb_of_digits-1), nb_of_wildcards)
        for positions in allowed_positions:
            for base in range(10**(nb_of_digits-nb_of_wildcards-1)+1, 10**(nb_of_digits-nb_of_wildcards), 2):
                #assert(len(str(base)) + len(positions) == nb_of_digits)
                if test_family(base, positions):
                    print(base, positions) 
                    value_to_return =  True
            #print(f"Finished positions {positions} with {nb_of_digits} digits")
    return value_to_return

def test_family(base, positions):
    # Tests if a given set of digits with wildcards (like "**123") can be part of a 
    #8 prime value family. 
    idx1 = 0
    idx2 = 0
    s = ""
    base = str(base)
    for j in range(len(base) + len(positions)):
        if idx2 < len(positions) and j == positions[idx2]:
            s = s + "*"
            idx2+=1
        else:
            s = s + base[idx1]
            idx1+=1

    if not any([pseudo_prime(s.replace("*", str(x))) for x in range(1, 4)]): return False
    not_primes = 1 if 0 in positions else 0
    digits = []
    for x in range(not_primes, 10):
        if binary_search(data, int(s.replace("*", str(x)))) == -1:
            not_primes += 1
        else:
            digits.append(x)
        if not_primes >= 3:
            return False

    print("-----------------")
    print("One possible family: ")
    for x in digits:
        print(s.replace("*", str(x)))
    print("-----------------")

    #if sum([pseudo_prime(s.replace("*", str(x))) for x in range(d, 10)]) >= 8: return True

    return True

def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1

def pseudo_prime(p):
    p = int(p)
    #print(f"Tested {p}")
    if sum([int(s) for s in str(p)])%3 == 0: return False
    return all([pow(a, p-1, p) == 1 for a in [2, 3, 5, 7, 11, 13]])
    

nb_of_digits = 4
while check_family(nb_of_digits) == False:
    print(f"Finished with {nb_of_digits} digits")
    nb_of_digits += 1

#print("El resultado es: {}".format(data[ini-1]))
print("The time spent is: {}".format(perf_counter()-t))
