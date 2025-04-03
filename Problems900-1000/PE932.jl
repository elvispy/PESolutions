# PE932


function T(N)
    squares = [ii => ii^2 for ii = 1:floor(Int64, sqrt(10^N))]
    res = 0;
    for n = squares
        ls(aux) = length(string(aux));
        d = ls(n[1]);
        split(nn, dd) = ls(nn) == ls(floor(Int64, nn/10^dd)) + ls(Int64(mod(nn, 10^dd))) ?  floor(nn/10^dd) + mod(nn, 10^dd) : -1;
        if n[1] in split.(n[2], [d-1, d, d+1])
            res += n[2]
            #println(n[2])
        end
    end
    return res - 100

end
@assert T(4) == 5131

# Assertion block
res = T(16)
println("El resultado es $res")