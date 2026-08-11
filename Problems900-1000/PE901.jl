using LBFGSB, ForwardDiff
# Plantilla PE Julia

# La idea es que si escoges d, la probabilidad de que esté en los primeros d metros es
# d * (1-e^(-d)). After that, the probability of being deeper than d+m is e^(-m) memoryless property
#So, it should make sense that the optimal strategy is to do d, 2d, 3d, etc. 

# We should calculate the maximum point of x*(1-exp(-x))

# Given a sequence (strategy) (d_1, d_2, ...), the expected waiting time is
function ES(D::AbstractVector) # No truen typ e annotation A dual return would be cast to Float64
    probs = cumsum(D)
    p(x, y) = (exp(-y) - exp(-x))
    sunk_cost = cumsum(probs)
    result = sunk_cost[1] * p(probs[1], 0) # For Dual compatbitility
    for idx = 2:(length(D))
        result += sunk_cost[idx] * p(probs[idx], probs[idx-1]);
    end
    return result
end


function telescopic(D::AbstractVector)
    EV = cumsum(D)
    probs = exp.(-EV); shifted_probs = vcat(one(eltype(EV)), probs[1:(end-1)]);
    return sum(EV .* shifted_probs)
end

# Partial sums definitions

function optimize(f::Function)
    function g!(G, x)
        ForwardDiff.gradient!(G, f, x)    # stores directly into G, no allocation
    end

    N = 100
    x0 = fill(Inf, N)
    l = zeros(N) .+ 1e-9;
    u = 100*ones(N);

    res = lbfgsb(f, g!, x0;               # f, ∇f!, initial point
                lb      = l,             # lower bounds
                ub      = u,             # upper bounds
                factr   = 1e-12,
                pgtol   = 1e-12,
                maxfun  = 10000,
                maxiter = 10000)
    return res
end
# Assertion block
println("El resultado es $(optimize(telescopic))")