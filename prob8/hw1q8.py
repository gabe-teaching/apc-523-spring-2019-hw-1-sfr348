import numpy as np
from mpmath import *

def revrec(k,N,yN):
    yk = (e - yN)/N
    for n in range(N-1,k,-1):
        yk = (e - yk)/n
    return yk

k = 20
N = 32
yN = 0

yk = revrec(k,N,yN)

yk_wolfram = 0.1238038307625699486913962
#yk_wolfram = 209.0*4282366656425369.0*np.exp(1) - 209.0*11640679464960000.0
#print(yk_wolfram)
yk_err = abs((yk_wolfram - yk)/yk_wolfram)

print('y20 recursion | y20 wolfram | relative error')
print(yk,yk_wolfram,yk_err)
