
using Primes

M = 10^9+7
function factorial_prime_exponents(N::Int)::Array{Int}
    primes_list = primes(N)  # All primes up to N
    exponents = []

    for p in primes_list
        exp = 0
        k = 1
        while true
            term = div(N, p^k)
            if term == 0
                break
            end
            exp += term
            k += 1
        end
        push!(exponents, exp)
    end

    return exponents
end

function number_divisors(L, M = M)
    # Takes a number as a list L and returns the number of divisors  
    # that are greater than 1 modulo M 
    if length(L) == 1
        return L[1]
    end
    res = 1;
    for l = L
        res = res * (l+1);
        if res > M
            res = mod(res, M);
        end
    end
    return res-1 # Not counting 1;
end

# Returns the biggest divisor less of equal than the nth square root of L, 
# a number expressed as a list of exponents of primes
nth_root(L, n) = [floor(Int, l/n) for l = L]


function total_roundness(N)
    # Calculates the total roundness of N!. 
    # Uses the well known formula to calculate the maximum exponent of 
    # n such that n^alpha divides N!

    prime_decomposition = factorial_prime_exponents(N);
    res = 0; idx = length(prime_decomposition);
    for power  = 1:prime_decomposition[1]
        while power > prime_decomposition[idx];
            idx -= 1;
        end
        Lth_root = nth_root(prime_decomposition, power);
        res += number_divisors(Lth_root);
        prime_decomposition = prime_decomposition[1:idx];
        if res > M
            res = mod(res, M);
        end
    end
    return res

end

# Assertion block
@assert total_roundness(10) == 312
N = 10_000_000;
res = total_roundness(N)
println("El resultado es $res")