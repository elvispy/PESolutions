# PE816

"""
The idea is to subdivide the plane intro small grids 
"""
# using StatsBase;
using DataStructures

N = 14; # Number of points
M = 50515093; # mod
G = 2;
Points = [290797.0, mod(290797.0^2, M)];

struct points
    x::Int64
    y::Int64
end

PointsGrid = Matrix{Vector{points}(undef, N)}(undef, N, G, G);

for ii = 1:N

end


println("Calculated Points!");


G = 10; # Number of lines to project to
angs = LinRange(0, pi-pi/100, G);
angsX = cos.(angs);
angsY = sin.(angs);

min_distance = Inf;
Distance(p1, p2) = sqrt((p1[1] - p2[1])^2 + (p1[2] - p2[2])^2)
for ii = 1:G
    global min_distance
    f(p) = p[1] * angsX[ii] + p[2] * angsY[ii];

    sort!(Points, by = f); 

    A = Points;
    for jj = 1:N
        # Checking items less that the point
        if mod(jj, 100000) == 0; println("Im in $jj, $ii"); end
        ll = jj - 1;
        while ll >= 1 && abs(f(A[ll]) - f(A[jj])) < min_distance
            if Distance(A[ll], A[jj]) < min_distance
                min_distance = Distance(A[ll], A[jj]);
            end
            ll = ll - 1;
        end

        ll = jj + 1;
        while ll <= N && abs(f(A[ll]) - f(A[jj])) < min_distance
            if Distance(A[ll], A[jj]) < min_distance
                min_distance = Distance(A[ll], A[jj]);
            end
            ll = ll + 1;
        end

    end
end

function slow_checker(Points)
    L = length(Points);
    min_distance = Inf;
    for jj = 1:L
        for ii = (jj+1):L
            if Distance(Points[ii], Points[jj]) < min_distance
                min_distance = Distance(Points[ii], Points[jj]); 
            end
        end
    end
    return min_distance;
end


function calculate_min(Points)
    SIDES = 200;
    L = M / SIDES; # Divide the full grid on smaller SIDES x SIDES 
    X = [Vector{Float64}[] for _ = 1:SIDES];
    GRID = [X for _ = 1:SIDES];
    for ii = 1:N
        x, y = ceil.(Int64, Points[ii]/L);
        push!(GRID[x][y], Points[ii]);
    end
end


# println("The slow result is: ", slow_checker(Points));
println("The fast result is: ", min_distance); # Prints 20.880613017


