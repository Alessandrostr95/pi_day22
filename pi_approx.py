from random import random

def alg(n):
    k = 0
    for _ in range(n):
        x = random()*2 - 1
        y = random()*2 - 1
        if x**2 + y**2 <= 1:
            k+=1
    return 4*k/n

N = 100
print(alg(N))
