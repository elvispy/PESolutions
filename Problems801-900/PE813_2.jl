# This code implements a solution for computing P(n) = 11 ⊗ 11 ⊗ ... ⊗ 11 (n times),
# using a custom structure `PowerOfTwoNumber` to handle the sparsity of 1's in binary representations.

# Define a structure to represent numbers as sets of positions of 1's in their binary form.
struct PowerOfTwoNumber <: Number
    indices::Set{BigInt}  # Stores the positions of 1's as a set of integers
end

# Constructor for PowerOfTwoNumber, converting an integer to its binary representation.
function PowerOfTwoNumber(n::T) where T <: Integer
    n < 0 && throw(ArgumentError("Only non-negative integers are supported."))
    indices = findall(digits(n, base=2) .== 1) .- 1  # Find positions of 1's in binary representation
    return PowerOfTwoNumber(Set(indices))  # Store as a set of positions
end

# Import necessary Base methods for extending operators
import Base: +, *, show, <<, xor, ==, mod

# Define left-shift for PowerOfTwoNumber: shifts all indices by n positions
<<(a::PowerOfTwoNumber, n) = PowerOfTwoNumber(Set(a.indices .+ n))

# Define equality operator to compare a PowerOfTwoNumber with an integer
==(a::PowerOfTwoNumber, n::Integer) = a.indices == Set(findall(digits(n, base=2) .== 1) .- 1)
==(n::Integer, a::PowerOfTwoNumber) = a == n  # Symmetric case for comparison

# Define XOR operation between two PowerOfTwoNumbers
function xor(a::PowerOfTwoNumber, b::PowerOfTwoNumber)
    return PowerOfTwoNumber(symdiff(a.indices, b.indices))  # Symmetric difference of indices
end

# Define XOR-multiplication (⊗): applies XOR for each shifted term in the multiplication
function xorm(a::PowerOfTwoNumber, b::PowerOfTwoNumber)
    return reduce(xor, [a << idx for idx in b.indices])  # Combine shifted terms using XOR
end

# Define XOR-multiplication for multiple arguments
function xorm(args::Vararg{PowerOfTwoNumber})
    return reduce(xorm, args)  # Apply xorm recursively to all arguments
end

# Define modulo operation for PowerOfTwoNumber
function mod(a::PowerOfTwoNumber, m)
    mod(sum([powermod(2, idx, m) for idx in a.indices]), m)  # Compute modular value from indices
end

# Modulus value (prime) for result calculations
M = 10^9 + 7

# Override show method to print the number mod M
function Base.show(io::IO, n::PowerOfTwoNumber)
    print(io, mod(n, M))
end

# Precompute DB: a dictionary of P(2^k) for k = 0 to 64
DB = Dict{Int64, PowerOfTwoNumber}()
DB[0] = PowerOfTwoNumber(BigInt(11))  # Base case: P(1)
DB[1] = xorm(DB[0], DB[0])           # P(2) = 11 ⊗ 11
DB_list = [DB[0], DB[1]]
for ii = 2:65
    DB[ii] = xorm(DB[ii-1], DB[ii-1])  # Compute P(2^k) using doubling
    push!(DB_list, DB[ii])            # Store results for reuse
end

# Define function P(n): compute P(n) by decomposing n into powers of 2
function P(n::Integer)
    algarismos = findall(digits(n, base=2) .== 1) .- 1  # Find binary positions of 1's in n
    return mod(xorm([DB[alg] for alg in algarismos]...), M)  # Combine precomputed P(2^k)
end

# Compute the given n and verify correctness for small values
n = BigInt(8)^12 * BigInt(12)^8
for m = 1:(2^6)
    @assert P(m) == mod(xorm(PowerOfTwoNumber[11 for ii = 1:m]...), M) "Error with m=$m"
end

# Compute the result for P(n)
res = P(n)
println("El resultado es $res")
