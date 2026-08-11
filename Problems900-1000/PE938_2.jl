# probRB_row_dp.jl
# Bottom-up 1D DP for P(R,B) with self-term isolation.

function P(Rstar::Int, Bstar::Int)::Float64
    @assert Rstar >= 0 && Bstar >= 0

    # Handle trivial rows/cols
    if Rstar == 0 && Bstar == 0
        return 0.0            # harmless default
    elseif Bstar == 0
        return Rstar >= 1 ? 1.0 : 0.0
    elseif Rstar == 0
        return 0.0
    end

    # prev[r+1] holds P(r, B-1)
    prev = Vector{Float64}(undef, Rstar+1)
    # Initialize B=0 row: P(0,0)=0, P(r,0)=1 for r>=1
    prev[1] = 0.0
    @inbounds for r in 1:Rstar
        prev[r+1] = 1.0
    end

    curr = similar(prev)

    @inbounds for B in 1:Bstar
        # Base for current row: P(0,B)=0 for B>=1
        curr[1] = 0.0
        for R in 1:Rstar
            if R == 1 && B == 1
                curr[R+1] = 1.0
                continue
            end
            s  = R + B
            s1 = s - 1
            # Coefficient of the self-term
            C = (B/float(s)) * ((B-1)/float(s1))
            # Terms that do NOT include P(R,B)
            p_r2_b   = (R >= 2) ? curr[R-1] : 0.0       # P(R-2,B) already in this row
            p_r_bm1  = prev[R+1]                        # P(R,B-1) from previous row

            rpart = (R/float(s)) * ( ((R-1)/float(s1)) * p_r2_b + (B/float(s1)) * p_r_bm1 )
            bpart = (B/float(s)) * ( (R/float(s1))     * p_r_bm1 )

            curr[R+1] = (rpart + bpart) / (1.0 - C)
            # Optional clamp:
            # curr[R+1] = min(max(curr[R+1], 0.0), 1.0)
        end
        prev, curr = curr, prev  # roll rows
    end

    return prev[Rstar+1]
end

# ---- quick checks ----
println("P(2,2) = ", 1-P(2,2))
println("P(10,9) = ", 1-P(10,9))
println("P(34,25) = ", 1-P(34,25))
println("P(24690,12345) = ", 1-P(24690,12345))
