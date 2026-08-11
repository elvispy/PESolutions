using Combinatorics

# An evaluation is a set of symbols, O and a, b, c, d where Oab means binary operation O is applied to a and b. 
# A string is read from right to left

digits = collect(combinations(1:9, 4));
operators = [+, *, /, -];
operations = collect(Iterators.product(operators, operators, operators));

function is_valid(S) # Filter valid operations
    if length(S) == 1
        return S[1] == 0 ? true : false
    end

    for idx = 0:(length(S) - 3)
        if S[(end-2-idx):(end-idx)] == [1, 0, 0]
            S2 = [S[1:(end-3-idx)]; 0; S[(end+1-idx):end]]
            return is_valid(S2)
        end
    end

    return false
end

# Expressions are sets of characters, 1 are binary operators, 0 are placehodlers for digits.
templates = Set(reverse.(filter(is_valid, collect(permutations([1, 1, 1, 0, 0, 0, 0])))));

function evaluator(expression, digit)
    local_digits = copy(digit)
    op = copy(collect(expression[1]))
    tem = copy(expression[2])

    stack = Float64[] # Forcing Float64 prevents type-instability slowdowns
    
    while length(tem) > 0
        val = popfirst!(tem);
        if val == 0 
            push!(stack, pop!(local_digits))
        else
            f = pop!(op)
            
            # Elegantly pop instead of slicing arrays!
            b = pop!(stack) 
            a = pop!(stack)
            
            # / implicitly handles zero by yielding Inf or NaN. 
            push!(stack, f(a, b)) 
        end
    end
    
    # Implicitly fix floating point inaccuracies (e.g. 3.99999996 -> 4.0)
    return round(stack[1], digits=5) 
end

expressions = Iterators.product(operations, templates)

# FIX: Use typeof instead of eltype. 
results = Dict{typeof(digits[1]), Int64}() 
maxval = 0; maxd = nothing;

for d in digits
    global maxval, maxd
    # Evaluates to a mix of valid integers, decimals, Inf, and NaN
    values = Set{Float64}()

    for d in permutations(d)
        union!(values, evaluator.(expressions, Ref(d)));
    end
    
    val = 1
    while true
        # Naturally ignores decimals, Inf, and NaN because val is an integer
        if val in values 
            val += 1
        else
            break
        end
    end
    
    results[d] = val - 1;
    
    if results[d] > maxval
        maxval = results[d];
        maxd = d;
    end
end

println("El resultado es: $(maxd) with $maxval consecutive integers.")