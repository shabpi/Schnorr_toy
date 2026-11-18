import hashlib
import secrets
import random

p = 7673
g = 1003
x = 4 
X = pow(g, x, p)
poss_commits = [[6623, 4422], [3989, 141], [4846, 6198], [1075, 3859], [3849, 7054], [5330, 7579], [4289, 6721], [166, 5553], [1219, 1314], [3062, 5256]]
# Source - https://stackoverflow.com/q/16007204
# Posted by Juan José Castro, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-17, License - CC BY-SA 4.0

def factorize(n):
    sieve = [True] * (n + 1)

    for x in range(2, int(len(sieve) ** 0.5) + 1):
        if sieve[x]: 
            for i in range(x + x, len(sieve), x):
                sieve[i] = False

    lowerPrimes = [i for i in range(2, len(sieve)) if sieve[i] and (n % i == 0)]
    return lowerPrimes

def zkp():
    V = int(input("give V :"))
    c = random.randint(1, p - 1)
    print("C : {}".format(c))
    b = int(input("give b :"))
    if pow(g, b, p) == ((pow(X, c, p) * V )% p):
        print("Verified")
    else:
        print("Not Verified")
    pass


def random_gen(p):
    factos = factorize(p - 1)
    for k in range(p-1):
        g = random.randint(2, p - 1)
        if all(pow(g, (p - 1) // f, p) != 1 for f in factos):
            return g


zkp()




