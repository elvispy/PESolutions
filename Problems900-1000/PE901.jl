# Plantilla PE Julia

# La idea es que si escoges d, la probabilidad de que esté en los primeros d metros es
# d * (1-e^(-d)). After that, the probability of being deeper than d+m is e^(-m) memoryless property
#So, it should make sense that the optimal strategy is to do d, 2d, 3d, etc. 

# We should calculate the maximum point of x*(1-exp(-x))








# Assertion block
res = 0
println("El resultado es $res")