# probRB.jl
# Dynamic programming for P(R,B) with memoization.

# P(R,B) with memoization.
# Assumes R,B are nonnegative integers.
# Base cases:
#   P(n,0)=1  for n>=1
#   P(0,n)=0  for n>=1
#   P(1,1)=1
# Recurrence:
#   P(R,B) = [R/(R+B)]*[ (R-1)/(R+B-1)*P(R-2,B) + (B)/(R+B-1)*P(R,B-1) ] +
#            [B/(R+B)]*[ (B-1)/(R+B-1)*P(R,B) + (R)/(R+B-1)*P(R,B-1) ]


# Cache for computed values
const cache = Dict{Tuple{Int,Int},Float64}()

function P(R::Int, B::Int)::Float64
    # invalid or negative inputs
    if R < 0 || B < 0
        return NaN
    end

    # base cases
    if R == 0 && B == 0
        return NaN  
    elseif B == 0
        return R >= 1 ? 0.0 : 1.0
    elseif R == 0
        return B >= 1 ? 1.0 : 0.0
    elseif R == 1 && B == 1
        return 1.0
    end

    key = (R,B)
    if haskey(cache, key)
        return cache[key]
    end

    denom  = R + B
    denom2 = denom - 1

    if R == 1
        rpart = 1.0/(1+B); # If you take R out, you then take a B and keep B -> Probability 1 of ending in black.
    else
        rpart = (R/denom) * ( (R-1)/denom2 * P(R-2, B) + (B)/denom2 * P(R, B-1) )
    end
    bpart = (B/denom) *  (R)/denom2 * P(R, B-1)
    val = (rpart + bpart)/(1- (B/denom) * ( (B-1)/denom2))

    # clamp to [0,1] for safety
    #val = min(max(val, 0.0), 1.0)

    cache[key] = val
    return val
end

# Tests
println("P(2,2) = ", P(2,2))
println("P(10,9) = ", P(10,9))
println("P(34,25) = ", P(34,25))


println("The answer is $(P(24690, 12345))")