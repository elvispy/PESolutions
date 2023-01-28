# PE 808

using Primes;

function binary_search(list,item)
    low = 1
    high = length(list);
    while low <= high
        mid = (low + high) ÷ 2;
        guess = list[mid]
        if guess == item
            return mid
        end
        if guess > item
            high = mid - 1
        else
            low = mid + 1
        return 0 
        end
    end
end

function firstdigit(x::Integer)
    iszero(x) && return x
    x = abs(x)
    y = 10^floor(Int, log10(x))
    z = div(x, y)
    return z
end

reverse_integer(n::Integer) =  parse(Int64, reverse(string(n)))

PRIMES = Primes.primes(10, 10^9);

SUMS    = Vector{Int64}[[], [], [], [], [], []];
SQUARES = Vector{Int64}[[], [], [], [], [], []];
n = 0;
for el in PRIMES
    m = mod(el, 9);
    idx = m - floor(Int64, m/3);
    sq = el^2;
    push!(SQUARES[idx], sq);

    if mod(sq, 10) <= firstdigit(sq)
        R = reverse_integer(sq);
        if R != sq && isinteger(sqrt(R))
            if binary_search(SQUARES[idx], R) > 0
                global n;
                n = n + 2;
                println("$sq, $R");
            end
        end
    end 
end
# Assertion block
res = n
println("El resultado es $res")