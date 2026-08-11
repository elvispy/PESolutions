using Combinatorics
using Base.Iterators: product

# ==========================================
# 1. THE TEMPLATES (Structural Shapes)
# ==========================================
abstract type Skeleton end
struct SLeaf <: Skeleton end
struct SBranch <: Skeleton
    left::Skeleton
    right::Skeleton
end

function generate_templates(n::Int)
    n == 1 && return [SLeaf()]
    
    trees = Skeleton[]
    for i in 1:(n-1)
        for l in generate_templates(i)
            for r in generate_templates(n - i)
                push!(trees, SBranch(l, r))
            end
        end
    end
    return trees
end

# ==========================================
# 2. THE INSTANCES (Filled Trees)
# ==========================================
abstract type ExprNode end
struct Leaf <: ExprNode
    val::Float64
end
struct Branch <: ExprNode
    op::Symbol
    left::ExprNode
    right::ExprNode
end

# A helper to print the tree in a readable math format
Base.show(io::IO, n::Leaf) = print(io, n.val)
Base.show(io::IO, n::Branch) = print(io, "(", n.left, " ", n.op, " ", n.right, ")")

# ==========================================
# 3. THE INSTANTIATOR (Bridge)
# ==========================================
function instantiate(template::SBranch, ops::Vector{Symbol}, nums::Vector{Float64})
    left_node = instantiate(template.left, ops, nums)
    right_node = instantiate(template.right, ops, nums)
    
    # Pop the first operator in the queue
    current_op = popfirst!(ops) 
    return Branch(current_op, left_node, right_node)
end

function instantiate(template::SLeaf, ops::Vector{Symbol}, nums::Vector{Float64})
    # Pop the first number in the queue
    return Leaf(popfirst!(nums))
end

# ==========================================
# 4. THE EVALUATOR (Execution)
# ==========================================
evaluate(n::Leaf) = n.val

function evaluate(n::Branch)
    a = evaluate(n.left)
    b = evaluate(n.right)
    
    n.op === :+ && return a + b
    n.op === :- && return a - b
    n.op === :* && return a * b
    n.op === :/ && return b == 0 ? NaN : a / b  # Protect against DivByZero
    
    error("Unknown operator: $(n.op)")
end

# ==========================================
# 5. THE SOLVER (Putting it all together)
# ==========================================
function generate_all_expressions(nums::Vector{Float64}, allowed_ops::Vector{Symbol})
    N = length(nums)
    templates = generate_templates(N)
    
    # Generate all permutations of the numbers (Order matters, no replacement)
    num_perms = collect(permutations(nums))
    
    # Generate all combinations of operators (Order matters, WITH replacement)
    # A tree with N leaves requires exactly N-1 operations
    op_combos = collect(product(fill(allowed_ops, N-1)...))
    
    results = []
    
    # Loop through every shape, number order, and operator combination
    for template in templates
        for num_perm in num_perms
            for op_combo in op_combos
                # We collect() and copy() because instantiate() consumes the arrays
                tree = instantiate(template, collect(op_combo), copy(num_perm))
                val = evaluate(tree)
                
                push!(results, (expr=tree, value=val))
            end
        end
    end
    
    return results
end

# ==========================================
# RUN THE SCRIPT
# ==========================================
my_numbers = [3.0, 4.0, 5.0, 6.0]
my_operators = [:+, :*, :-, :/]

# Generate every possible mathematical expression
all_exprs = generate_all_expressions(my_numbers, my_operators)

println("Generated $(length(all_exprs)) unique expressions.")
println("---")
println("Here are a few combinations that evaluate to exactly 24.0:\n")

# Filter and print results that equal 24
count = 0
for res in all_exprs
    if res.value == 24.0
        println(res.expr, " = 24.0")
        global count += 1
        count >= 5 && break # Just show the first 5 for brevity
    end
end