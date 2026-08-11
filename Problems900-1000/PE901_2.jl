# PE901

# The idea is to calculate the expected value and simplify it so that it only depends on the first value
# Then, if the depts are s1, s2, s3...
# THe expected value
# EV = s1 * (1 - exp(-s1))
#    + s2 * (1 - exp(-(s2-s1))) * exp(-s1)
#    + s3 * (1 - exp(-(s3-s2))) * exp(-s1) + exp(-s2)

using Optim

function ES(x)
    EV = 1 + x + exp(-x)
    a = x
    b = exp(x)
    EV += exp(-b)
    
    for _ = 1:100
        next_b = exp(b - a)
        if next_b <= b
            return 1e20 
        end
        if next_b > 100.0 || isinf(next_b)
            break
        end
        EV += exp(-next_b)
        a = b
        b = next_b
    end
    return EV
end

setprecision(256)
res = Optim.optimize(ES, BigFloat("0.01"), BigFloat("2.0"), Brent(); abs_tol=BigFloat("1e-12"))
println(res.minimum)