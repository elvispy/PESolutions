# Function to compute the sequence s_n mod `mod_val`
function compute_sequence(n, mod_val)
    # Initialize an array to store the sequence
    s = Vector{BigInt}(undef, n)
    # Base case
    s[1] = BigInt(102022661)
    # Recurrence relation: s_n = s_(n-1)^2 % mod_val
    for i in 2:n
        s[i] = powermod(s[i-1], 2, mod_val)
    end
    return s
end

# Function to compute arrays a_n and b_n from the sequence s
function compute_a_b(s, n)
    # a_n corresponds to the odd-indexed terms: s[1], s[3], ..., s[2n-1]
    a = s[1:2:2n-1]
    # b_n corresponds to the even-indexed terms: s[2], s[4], ..., s[2n]
    b = s[2:2:2n]
    return a, b
end

# Function to compute the minimal path sum using dynamic programming
function minimal_path_sum(a, b, N)
    # Construct the matrix M where M[i, j] = a[i] + b[j]
    M = BigInt[a[i] + b[j] for i in 1:N, j in 1:N]
    # Copy M to dp to calculate the minimal path sums
    dp = deepcopy(M)

    # Iterate through each cell in the matrix
    for i in 1:N
        for j in 1:N
            # If not in the first row, update dp[i, j] based on the cell above
            if i > 1
                dp[i, j] = min(dp[i, j], dp[i-1, j] + M[i, j])
            end
            # If not in the first column, update dp[i, j] based on the cell to the left
            if j > 1
                dp[i, j] = min(dp[i, j], dp[i, j-1] + M[i, j])
            end
        end
    end

    # The minimal path sum from top-left to bottom-right is stored in dp[N, N]
    return dp[N, N]
end

# Function to compute A(N), the minimal path sum for an N x N matrix
function A(N)
    mod_val = 998388889  # Given modulus for the sequence
    seq_len = 2 * N      # Total number of terms needed in the sequence
    # Compute the sequence s_n
    s = compute_sequence(seq_len, mod_val)
    # Compute arrays a_n and b_n
    a, b = compute_a_b(s, N)
    # Compute the minimal path sum for the matrix M
    return minimal_path_sum(a, b, N)
end

# Test cases to verify the implementation
println(A(1))  # Should print 966774091
println(A(2))  # Should print 2388327490
println(A(10)) # Should print 13389278727

# Uncomment the following line to compute A(10^7) (may take significant time/memory)
# println(A(10^7))
