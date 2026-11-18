import random
p = 7673
g = 1003
x = 4 
X = pow(g, x, p)

k = [[random.randint(1, p-1), pow(g, random.randint(1, p-1), p)] for _ in range(10)]

