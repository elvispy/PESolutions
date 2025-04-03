# Plantilla PE Julia
""""
For this problem, I solved a number of special cases. We denote the pair (a, b), where it is
assumed that a ≥ b. We observe the following positions

1) (odd, 1) is LOSING
2) (even, 1) is WINING
3) (even, even) is WINING (can go to (odd, 1)) 
4) (even, odd) is WINING  (can go to (odd, 1)) 
5) from the following fact, two theorems can be proved:
    "the states available to (a, b) is a subset to the state available to (a, b+x), for all a, b, x with a ≥ b+x"
    - if (a, b) is WINING, (a, y) is wining for a ≥ y ≥ b (both have access to a losing position)
    - if (a, b) is LOSING, (a, y) is losing for b ≥ y (superset does not have access to a losing position) 
6) (4k+3, 2) is LOSING (goes to either (even, 1) or (4k+1, 2), and base case (3, 2) is losing)
7) (4k+1, even) is WINING (goes to (4k+3, 2))
8) (4k+1, odd) is WINING (can go to (4k+3, 2), but odd has to be > 1)
9) (4k+3, odd) is ? (can go to (even, even), )
"""








# Assertion block
res = 0
println("El resultado es $res")