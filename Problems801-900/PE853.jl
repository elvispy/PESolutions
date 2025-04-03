using Primes
using Combinatorics

N = 120;
# Calculate fibonacci numbers
F = zeros(BigInt, (N+10,)); F[2] = 1;
for ii = 3:length(F)
    F[ii] = F[ii-1] + F[ii-2];
end

# Decompose number into prime factors
function decompose(n::BigInt)::Vector{BigInt}
    M = 10^6
    p = primes(M)
    s = BigInt[];
    for prime in p
        while mod(n, prime) == 0
            push!(s, prime);
            n = n ÷ prime;
        end
    end
    p = Primes.nextprime(M);
    while n > 1
        if Primes.isprime(n)
            push!(s, n);
            n = 1;
        end
        while mod(n, p) == 0
            push!(s, p);
            n = n ÷ p;
        end
        p = Primes.nextprime(p);
        if p > 10^9
            break;
        end
    end
    return s
end

function sum_divisors(prime_factors::Vector{Int})
    # Count exponents for each prime
    factor_counts = Dict{Int,Int}()
    for p in prime_factors
        factor_counts[p] = get(factor_counts, p, 0) + 1
    end
    
    # Calculate product of (1 + p + p² + ... + p^a) for each prime p with exponent a
    total = 1
    for (p, a) in factor_counts
        total *= (p^(a + 1) - 1) ÷ (p - 1)
    end
    
    return total
end

function brute_force_period(n)
    a, b = 1, 1;
    p = 1; global N;
    while (a, b) != (0, 1) && p < 2*N
        p+=1;
        a, b = b, mod(a+b, n);
        #println("$a, $b");
    end
    return p
end


function pisano_period(p)
    # Calculates the numbers that have pisano period equal to n.
    # It has to satisfy F_1 = F_{N+1} (mod n) and F_1 = F_{N+2} (mod n)

    cut = 10^9;
    primes   = decompose(F[p+1] - F[1]);
    primesp1 = decompose(F[p+2] - F[2]);

    # Check that n satisfy both modular arithmetic equations
    intersect_with_repeats(a, b) = isempty(a) || isempty(b) ? eltype(a)[] : reduce(vcat, [fill(x, min(count(==(x), a), count(==(x), b))) for x in unique(a) if x in b]; init=eltype(a)[]);

    # List all numbers that have those primes in their prime decomposition
    intersected = intersect_with_repeats(primes, primesp1); #println("Intersected: $intersected")
    subset_products(p) = unique(foldl((a,x)->vcat(a,a.*x), p; init=[1]))
    candidates = subset_products(intersected); #println("Candidates: $candidates")

    # Check a posteriori that the pisano period is exactly p
    return filter((n) -> n < cut && brute_force_period(n) == p, candidates)
end

pisano_period_sum(n) = sum(pisano_period(n))


@assert(pisano_period_sum(18) == 19+38+76)

# Assertion block
res = pisano_period_sum(120)
println("El resultado es $res")