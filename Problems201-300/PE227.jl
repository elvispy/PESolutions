# Plantilla PE Julia
# Use a transition matrix approach to calculate the probability

using LinearAlgebra

N = 10; # Number of players
steps = floor(Int32, N/2)+1;

#T_matrix[i, j] is the prob that people at distance j finish at distance i after rolling dice (steps \equiv 0)
T_matrix = zeros(steps, steps);

for ii = 1:steps
    vals = [ii-2, ii-1, ii, ii+1, ii+2];
    
    #vals[vals .< 0] = - vals[vals .< 0];
    probs = [1/36, 8/36, 18/36, 8/36, 1/36];
    if any(vals .== -1)
        vals[vals .== -1] .= 1;
        probs[vals .== 1] .= sum(probs[vals .== 1]);
    end
    if any(vals .>= steps)
        vals[vals .>= steps] = N .- vals[vals .>= steps];
        probs[vals .== steps-2] .= sum(probs[vals .== steps-2]);
        probs[vals .== steps-3] .= sum(probs[vals .== steps-3]);
    end
    vals[vals .== 0] .= steps;
    
    if ii == steps
        vals .= steps-1; vals[3] = steps;
        probs = 0 .* probs; probs[3] = 1;
    end
    T_matrix[vals, ii] = probs;
end



expectedValues = zeros(Float64, (steps-1,));
for jj = 1:(steps-1)
    global expectedValues
    b = zeros(Float64, (steps, ));
    b[jj] = 1;
    M = 1;
    rest = 1;
    expValue = 0;
    #value = T_matrix[steps, steps-1]; # Value that keeps track of the probability
    # that game has ended
    #curMatrix = T_matrix;
    while (M * rest > 1e-5) && M < 1e+6
        if M%1000000 == 0; println(M); end
        #global value, expValue, M
        b = T_matrix * b; 
        rest -= b[end]; expValue += M * b[end]; b[end] = 0;
        for ii=1:(jj-1)
            rest -= b[ii];
            expValue = M * expectedValues[ii];
            b[ii] = 0;
        end
        M+=1;
    end
    expectedValues[jj] = expValue;
end

# Assertion block
res = expectedValues[end]
println("El resultado es $res")