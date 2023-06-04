# PE816

"""
The idea is to project the points onto a 1-D line and check only the closests 
"""
# using StatsBase;
using DataStructures

N = 14; # Number of points
M = 50515093; # mod
Points = [[0.0, 0.0] for i = 1:N];
Points[1] = [290797.0, mod(290797.0^2, M)];

struct points
    x::Int64
    y::Int64
end

Points2 = Vector{points}(undef, N);

for ii = 2:N
    Points[ii][1] = mod(Points[ii-1][2]^2, M);
    Points[ii][2] = mod(Points[ii][1]^2, M);
    Points2[ii] = points(Points[ii][1], Points[ii][2]);
end

function convex_hull(p::Vector{points})::Vector{points}
    N = length(p);
    hull = Stack{points}();
    order(p1::points, p2::points) = (p1.x + p1.y) <= (p2.x + p2.y);

    p_sorted = sort(p, by=order);

    push!(hull, p_sorted[0]);

    jj1 = 1;
    while (jj1 < N)
        if !(p[0] == p[jj1]); break; end
        if (jj1 == N); return hull; end
        jj1 = jj1 + 1;
    end

    jj2 = jj1 + 1;
    while (jj2 < N)
        if counter_clock_wise(p[0], p[jj1], p[jj2]) != 0; break; end
        jj2 = jj2 + 1;
    end
    push!(hull, p[jj2-1]);

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


