# PE371

# The idea is to use recursion: we classify plates as 
"""
1) Plates that have not been seen and wouldnt make me win if I were to see them
2) Plates that have not been seen and would   make me win if I were to see them
3) Plates that I have already seen and wouldnt make me win If I were to see them again
4) Plates that I have already seen and would make me win If I were to see them again (plate 500)

Let b be zero or one, corresponding to having seen plate #4. 
Let x be the number of plates in #3
Let y be the number of plates in #1

Then b + 2x + y + 1 = N

We have that
    E[X] = P(#1)(1 + E[X']) + P(#2) + P(#4) + P(#3)(1 + E[X])
         = 1 + P(#1) * E[X'] + P(#3) * E[X]
∴ E[X] = (1 + P(#1) * E[X'])/(1 - P(#3))
"""
M = 1000;
# insert_and_dedup!(v::Vector, x) = (splice!(v, searchsorted(v,x), [x]); v);
b_zero = NaN * zeros((div(M, 2), ));
b_one  = NaN * zeros((div(M, 2), )); b_one[end] = 2;
function ExpValue(b, x, y ;N = M, approximate = false)
    # Recursion Base
    if y == 0
        return 2 # Calculated this by hand
    elseif y == 1
        return 2 + 4/N; # I calculated this by hand
    end
    # Dynamic Programming
    if b == 1
        if b_one[x+1] !== NaN
            return b_one[x+1]
        end
    else
        if b_zero[x+1] !== NaN
            return b_zero[x+1]
        end
    end
    
    # Recursive Step
    if b == 1
        val = (1 + y/N * ExpValue(b, x+1, y-2))/(1 - (x+1)/N);
        b_one[x+1] = val;
        return val;
    else
        val = (1 + ExpValue(1, x, y-1)/N + (y-1)*ExpValue(0, x+1, y-2)/N) / (1 - (x+1)/N);
        b_zero[x+1] = val;
        return val
    end
    
end

# println(ExpValue(1, 498, 2))

# Assertion block
res = ExpValue(0, 0, M-1) 
println("El resultado es $res")