
"""
PE 816.jl
The idea is to subdivide the plane into small regions and perform nearest search on those small regions
This way, we only need to test for proximity in adjacent bins.

Since the maximum value possible for the coordinate of the points is approximately 5e+7, which has
26 digits in binary, the bin is going to be the first 10 digits in binary of the two coodinates,
being thus a tuple of two 10-digit binary numbers. 

See
https://en.m.wikipedia.org/wiki/Nearest_neighbor_search#Space_partitioning
For the idea of this algorithm

"""
# Function to convert a number to its first 5 binary digits
function first_5_binary_digits(x)
    return div(x, 2^15)
end

# Function to bin points based on their first 5 binary digits
function bin_points(points)
    bins = Dict{Tuple{Int, Int}, Vector{Tuple{Float64, Float64}}}()
    for point in points
        x_bin = first_5_binary_digits(point[1])
        y_bin = first_5_binary_digits(point[2])
        bin_key = (x_bin, y_bin)
        if !haskey(bins, bin_key)
            bins[bin_key] = []
        end
        push!(bins[bin_key], point)
    end
    return bins
end

# Function to calculate Euclidean distance between two points
function euclidean_distance(p1, p2)
    return sqrt((p1[1] - p2[1])^2 + (p1[2] - p2[2])^2)
end

# Function to find the minimum distance in a list of points
function min_distance_in_list(points)
    min_dist = Inf
    for i in 1:length(points)-1
        for j in i+1:length(points)
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist
                min_dist = dist
            end
        end
    end
    return min_dist
end

# Function to find the closest distance between points in adjacent bins
function min_distance_between_bins(bin1, bin2)
    min_dist = Inf
    for p1 in bin1
        for p2 in bin2
            dist = euclidean_distance(p1, p2)
            if dist < min_dist
                min_dist = dist
            end
        end
    end
    return min_dist
end

# Main function to find the closest Euclidean distance between any pair of points
function closest_distance(points)
    bins = bin_points(points)
    min_dist = Inf
    for ((x_bin, y_bin), bin_points) in bins
        # Check distance within the same bin
        min_dist = min(min_dist, min_distance_in_list(bin_points))
        # Check distances with adjacent bins
        for dx in -1:1
            for dy in -1:1
                if dx != 0 || dy != 0
                    adjacent_bin_key = (x_bin + dx, y_bin + dy)
                    if haskey(bins, adjacent_bin_key)
                        min_dist = min(min_dist, min_distance_between_bins(bin_points, bins[adjacent_bin_key]))
                    end
                end
            end
        end
    end
    return min_dist
end
N = 2000000
s0 = 290797.0;
M = 50515093.0
points = Vector{Tuple{Float64, Float64}}()
for i = 1:N
    global s0;
    s1 = convert(Float64, mod(s0^2, M));
    push!(points, (s0, s1));
    s0 = convert(Float64, mod(s1^2, M));
end
# Example usage
println("Closest distance: ", closest_distance(points))
