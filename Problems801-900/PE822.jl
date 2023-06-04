# PE822 
"""
The idea is to approximate a number C in which all elements are greater or equal than C.
that is, find k such that n^2^k \geq C ==> k ln(2) + ln(ln(n)) >= ln(ln(C))
==> k >= (ln(ln(C)) - ln(ln(n)))/ln(2)
After that, we sum over all k's to obtain the number of turns that have passed for that C.
We update C in a binary search manner, using the fact that the sum of k's is monotonous w.r.t C.

Finally, a couple of tweaks: Sometimes the minimum k is not optimal. That is why we find 
a distribution of k's which is close enough and then we find the exact turn.

"""
function power(x, y, p)
    # Calculates x^y mod p
    res = 1
    # y = convert(Int64, y);
    while ( y > 0)
        if ((y & 1) != 0 )
            res = rem(res * x, p);
        end
        y = y >> 1
        x = rem(x * x, p)
    end
    return res % p
end

function update_ks(ks, M)
    # Makes sum(ks) == M, exact number of turns
    N = length(ks) + 1; L = sum(ks);
    xtra = @. log(log(2:N));
    weights = ks * log(2) .+ xtra;
    for _ = 1:(M-L)
        (b, c) = findmin(weights);
        ks[c] = ks[c] + 1;
        weights[c] = b + log(2);
    end
    return ks
end

function summ(N, M; P = 1234567891)
    M = convert(Int64, M);
    lnlnC = 1.0e+8; # log(log(4))
    loglogs = log.(log.(LinRange(2.0, N, N-1)));
    l2 = log(2.0);
    ks = @. ceil(Int64, (lnlnC - loglogs) / l2);
    sumksmin = 0;
    sumksmax = sum(ks);
    if sum(ks) > M
        throw("Initial guess too big!");
    end
    while sum(ks) < M
        lnlnC *= 2;
        ks = @. ceil(Int64, (lnlnC - loglogs) / l2);
        sumksmin = sumksmax;
        sumksmax = sum(ks);
    end
    lnlnC_max = lnlnC;
    lnlnC_min = lnlnC/2;
    # lnN = lnN/2;
    while !(0 <=  M - sum(ks) <= sqrt(N))
        sumks = sum(ks)
        if sumks < M
            lnlnC_min = lnlnC; sumksmin = sumks;
        else
            lnlnC_max = lnlnC; sumksmax = sumks;
        end
        lnlnC = lnlnC_min/2 + lnlnC_max/2; 
        ks = @. ceil(Int64, (lnlnC - loglogs) / l2);
        if abs(lnlnC_min - lnlnC_max)/lnlnC_max < 1e-15
            lnlnC_min *= 0.98;
            lnlnC_max *= 1.03;
        end
    end

    ks = update_ks(ks, M)
    # P is prime, so we use Euler's theorem on the exponent
    exps = power.(2, ks, P-1);

    
    return sum(power.(2:N, exps, P)) % P
end

# Assertion block
res = summ(10000, 1.0e+16)
println("El resultado es $res")