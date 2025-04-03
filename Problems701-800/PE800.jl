using Primes

function count_hybrid_integers(base::Int, exponent::Int)
    upper_bound_log = exponent * log(base)
    max_prime = floor(Int, upper_bound_log*2)
    prime_list = collect(Primes.primes(max_prime))
    count = 0
    left = 1
    right = length(prime_list)

    while left < right
        while left < right
            p = prime_list[left]
            q = prime_list[right]
            if q * log(p) + p * log(q) <= upper_bound_log
                break
            end
            right -= 1
        end
        count += right - left
        left += 1
    end

    return count
end

# Example usage:
N = 800800
result = count_hybrid_integers(N, N)
println("C($N^$N) = $result")
