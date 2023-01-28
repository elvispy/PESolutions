# PE 216

using Primes;
"""
The idea is that 2n^2-1 ≡ 1 mod p ⟺ (2^-1 p) = 1 (Legendre Symbol) ⟺ (2 p) = 1

That's true when p ≡ ±1 (mod 8). So we only need to test primality on a subset of primes

On the other hand, when p ≡ -1 (mod 8), n ≡ ±2^(2k+1) are the only solutions to the original equation

For p ≡ 1, we must find which n's are good, organically. 
"""

M = 50000000; # Max number for need
P = floor(Int64, sqrt(2*M^2 - 1)); # Maximum prime allowed


"""
function test_primality(p::Int64, extra_primes = [])
    primes = [2, 3, 5];
    for pp in [primes; extra_primes]
        if powermod(pp, p-1, p) != 1; return false end;
    end
    for n = 2:floor(Int64, sqrt(p))
        if mod(p, n) == 0; return false end; 
    end
    return true;    
end
"""

primes_1 = zeros(Bool, floor(Integer, P/8)); # PseudoPrimes of the form 8k+1
primes_7 = zeros(Bool, floor(Integer, P/8)); # Primes of the form 8k-1


for ii = 1:floor(Integer, P/8)
    global n;
    if Primes.isprime(8*ii+1)
        primes_1[ii] = true;
    end
    if Primes.isprime(8*ii-1)
        primes_7[ii] = true;
    end
end


function legendre(n, p)
    if p != 2 && isprime(p)
        x = powermod(BigInt(n), div(p - 1, 2), p)
        return x == 0 ? 0 : x == 1 ? 1 : -1
    end
    return -1
end

function cipolla(n, p)
    if legendre(n, p) != 1
        return NaN
    end
    a, w2 = BigInt(0), BigInt(0)
    while true
        w2 = (a^2 + p - n) % p
        if legendre(w2, p) < 0
            break
        end
        a += 1
    end
    r, s, i = (1, 0), (a, 1), p + 1
    while (i >>= 1) > 0
        if isodd(i)
            r = ((r[1] * s[1] + r[2] * s[2] * w2) % p, (r[1] * s[2] + s[1] * r[2]) % p)
        end
        s = ((s[1] * s[1] + s[2] * s[2] * w2) % p, (2 * s[1] * s[2]) % p)
    end
    return r[2] != 0 ? NaN : r[1]
end

modules_1 = [cipolla(invmod(2, 8*ii+1), 8*ii+1) for ii in eachindex(primes_1) if primes_1[ii] == true];
primes_1  = [(8*ii+1) for ii = eachindex(primes_1) if primes_1[ii] == true];
modules_7 = [powermod(2, 2*ii-1, 8*ii-1) for ii in eachindex(primes_7) if primes_7[ii] == true];
primes_7  = [(8*ii-1) for ii = eachindex(primes_7) if primes_7[ii] == true];

potential_primes = ones(Int64, M, ); potential_primes[1] = 0;

for ii in eachindex(modules_1)
    jj = 0;
    p = primes_1[ii];
    n1 = modules_1[ii];
    n2 = p - n1;
    m = min(n1, n2);
    while jj*p + m <= M
        if jj * p + n1 <= M && 2*(jj*p+n1)^2 - 1 > p; potential_primes[jj*p + n1] = 0; end
        if jj * p + n2 <= M && 2*(jj*p+n2)^2 - 1 > p; potential_primes[jj*p + n2] = 0; end
        jj = jj + 1;
    end
end

for ii in eachindex(modules_7)
    jj = 0;
    p = primes_7[ii];
    n1 = modules_7[ii];
    n2 = p - n1;
    m = min(n1, n2);
    while jj*p + m <= M
        if jj * p + n1 <= M && 2*(jj*p+n1)^2 - 1 > p; potential_primes[jj*p + n1] = 0; end
        if jj * p + n2 <= M && 2*(jj*p+n2)^2 - 1 > p; potential_primes[jj*p + n2] = 0; end
        jj = jj + 1;
    end
end

res = sum(potential_primes);
potential_primes = [2*ii*ii-1 for ii in eachindex(potential_primes) if potential_primes[ii] == 1];
for el in potential_primes
    if ~Primes.isprime(el)
        println(el)
        break;
    end
end
# Assertion block
println("El resultado es $res")