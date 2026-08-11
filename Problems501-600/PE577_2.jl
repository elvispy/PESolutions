
using Symbolics

@variables a n jj
s(expr) = simplify(expr, expand=true)

p1 = a
p5 = (n-a)*jj
p3 = s(a*jj + (n-a))
c  = s((p1 + p3 + p5)/3)
p2 = s(2*c - p5)
p4 = s(2*c - p1)
p6 = s(2*c - p3)

reduce_jj(expr) = s(substitute(expr, Dict(jj^2 => jj - 1)));


@assert isequal(reduce_jj(s((p1-c)* jj + c - p2)), 0)
@assert isequal(reduce_jj(s((p3-c)* jj + c - p4)), 0)
@assert isequal(reduce_jj(s((p5-c)* jj + c - p6)), 0)
