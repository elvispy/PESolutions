using Primes
# Idea use recursion to divide into two cases: corrrect guess and incorrect guess. 
N = 10^8;

function expected(S, prob=1.0)
    if length(S) == 0
        return 0.0
    end
    evens = filter(iseven, S);
    odds  = filter(isodd,  S);

    exp_value = length(evens) > length(odds) ? length(evens)/length(S) : length(odds)/length(S);

    evens = evens .>> 1; evens = evens[evens .> 0];
    odds  = odds .>> 1;  odds  = odds[odds .> 0];

    return exp_value * prob + expected(evens, prob*length(evens)/length(S)) + expected(odds, prob*length(odds)/length(S))
end


# Assertion block
res = expected(Primes.primes(N))
println("El valor esperado para N = $N es: $res")