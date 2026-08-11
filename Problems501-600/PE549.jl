using Primes

# Idea use dyamic programming. The well-known formula for the exponent that divides n! is
# v_p(n) = \sum_{k \geq 1} \lfloor n/p^k \rfloor
# Given a prime decomposition of a number n = \Pi p_i^{\alpha_i}
# Then s(n) = k <=> p_i^{\alpha_i} | k! <=> v_{p_i}(k) \geq \alpha_i for all i.
# In particular, s(n) = max_i s(p_i^{\alpha_i}) 

# If we thinkg about a prime p^m, s(p^m) = k <=> v_p(k) ≥ m ^ v_p(k-1) < m 
#    <=> ∑_{j \geq 1} \lfloor k/p^j \rfloor ≥ m > ∑_{j \geq 1} \lfloor (k-1)/p^j \rfloor 
# Thus, by saving a dynamic table that calculates dp[i, j] = s(p_i^j)
N = 10^8;
p = Primes.primes(N);
sqrtIdx = findfirst(diff(p.^p .< N) .== -1) # Index of the largest prime p_i such that p_i^p_i < N;

struct listNumber
    exponents::Vector{Int}
    value::Int
end

function listNumberIterator(ln::listNumber; max_value=N)
    if 2* ln.value <= max_value
        ln.value *= 2
        ln.exponents[1] += 1
        return ln
    else

    end

end

function s(ii::Int, jj::Int; max_value=N)::Int
    # Calculates s(p_ii^jj)
    if ii > sqrtIdx
        return jj * p[ii]
    else
        maxIdx = ceil(Int, log10(jj)/log10(p[ii]))
        return (jj - sum([floor(Int, (jj-k)/p[ii]^k) for k in 1:maxIdx])) * p[ii] 
    end
end