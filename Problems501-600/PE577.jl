# PE577.jl

"""
Counting hexagons recursively.
H(n) = H(n-1) + A(n)/3 + 2/3 B(n) + C(n)
# NUmber of hexagons in triangle is the same as number of hexagons in a triangle of side n-1, plus all hexagons that touch exactly one side A(n), plus 
# hexagons that touch exactly two sides, plus hexagons that touch exatly three sides
A(n)/3 = A(n-1)/3 + B(n-1)/3 
# Number of hexagons that touc exactly one side, plus the ones that touch one of the sides too of a triangle smaller by one side
B(n)/3 = B(n-1)/3 + C(n-1)
"""

using LinearAlgebra
using Memoize

# C2(n::Int64) = (n >= 3) * ((n%3 == 0) + n);

jj = exp(1.0im * π/ 3);
relequal(a, b) = norm(a-b)/norm(b+1e-15) < 1e-3;
@memoize function C(n::Int64)::Int64
  if n%3 !=0; return 0; end
  
  k = div(n, 3);
  return k; 
  #grid       = [a + b*jj for a in 0.0:n for b in 0.0:(n-a)];
  #boundary_1 = 1.0:(n-1);
  #boundary_2 = jj .* (1.0:(n-1));
  #boundary_3 = boundary_2 .* jj .+ n; # Boundary 2 rotated 60 degrees counter clockwise and translated by n units to the right.

  # THis is the important line. The only requirement is that the points below are inthe grid. That happens when n/3 <= a < 2/3 n; 
  #triangles = [(a, 2*k + (a - k)* jj, (n-a) + a * jj, (2*k-a) + 2*k * jj, (n-a)*jj, (a-k) + (2*k-a)* jj) for a in boundary_1];
  #centers = [(a+b+c)/3 for (a, b, c) in triangles];
  
  # The other three vertices in the hexagon, we filter out the ones whose rotated versions also land on boundaries to avoid double counting
  #rotated_triangles = [(t .- c) .* jj .+ c for (t, c) in zip(triangles, centers)];

  # We filter out the ones which rotated also fall on the boundary to avoid dups
  # We only count triangles with all points in the grid
  #in_grid(p) = any(g -> relequal(p, g), grid)   
  #nb_hexagons = rotated_triangles                                |> 
  #              filter(t -> !any(relequal.(boundary_1, t[1])))   |> 
  #              filter(t -> all(in_grid, t))                     |> 
  #              length;
  #return nb_hexagons
end

@memoize function B(n::Int64)::Int64
  if n <= 3; return 0; end
  return B(n-1) + 3 * C(n-1);
end

@memoize function A(n::Int64)::Int64
  if n <= 3; return 0; end
  return A(n-1) + B(n-1);
end

@memoize function H(n::Int64)::Int64
  if n <=2; return 0; end
  return H(n-1) + div(A(n), 3) + 2* div( B(n), 3) + C(n);
end

@assert H(3) == 1;
@assert H(6) == 12;

println("The answer is $(sum(H.(1:12345)))")
