# Plantilla PE Julia
# Idea one: Use the formula for the biggest exponent that divides N! for each prime except 5 (because it generates trailing zeros)
# Update: this does not seem to work (too slow)
using Primes
N = 10^10
S = 1
pows = [0, 0]
for p in Primes.primes(N)
    global S, pows
    power = 0
    idx = 1
    while p^idx <= N
        power += floor(Int64, N/p^idx)
        idx+=1
    end
    if p == 2
        pows[1] = power;
    elseif p == 5
        pows[2] = power;
    else
        S *= powermod(p, power, 10^5);
        S = mod(S, 10^5);
    end
end

S *= powermod(2, pows[1] - pows[2], 10^5);

# Assertion block
res = mod(S, 10^5);
println("El resultado es $res")