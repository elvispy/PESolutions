# Plantilla PE Julia
N = 40;
M = BigInt(2^(N+1)-1);
MOD = 10^9+7;
leftshift(a, n) = (a & (2^(N-n+1)-1)) << n;  
XORMultiply(a::BigInt, b::BigInt)::BigInt = xor([a << idx for idx = findall(digits(b, base=2) .== 1) .- 1]...);

function XORM(args...)::BigInt
    #args = M .& args ; # Discarding unuseful bits
    return reduce(XORMultiply, args)# & M;
end

DB = Dict{Int64, BigInt}()
DB[0] = BigInt(11);
DB[1] = XORMultiply(11, 11);
DB_list = [DB[0], DB[1]]
for ii = 2:10
    DB[ii] = XORMultiply(DB[ii-1], DB[ii-1])
    push!(DB_list, DB[ii])
end


function P(n::Integer)::BigInt
    algarismos = findall(digits(n, base=2) .== 1) .- 1;
    return mod(XORM([DB[alg] for alg in algarismos]...), MOD);

end

n = 5; #BigInt(8)^12 * BigInt(12)^8
for m = 1:(2^6)
    @assert P(m) == mod(XORM(BigInt[11 for ii =1:m]...), MOD) "Error with m=$m"
end
res = P(n)
println("El resultado es $res")