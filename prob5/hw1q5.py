import numpy as np
import math

def npround_sigfigs(sigs,y):

    r = int((sigs-1.0) - np.floor(np.log10(y)))
    #print((sigs-1.0),floor(log10(y)),r)
    y = np.round(y,r)
    return y
def round_to_n(x,r):
    '''Rounds x to r significant digits.'''
    return float('%.*g' % (r,x))

e_it  = np.zeros( (20,1) )
N = np.zeros( (20,1) )

n = 1.0
e_it[0] = (1.0+(1.0/n))**n
N[0] = n


#new_file=open("/Users/susanredmond/Desktop/PhD/Term\ 2/APC\ 523\ Numerical\ Algorithms/HW1/hw1q5.txt",mode="a+",encoding="utf-8")
print('| i | N | e[i] | e[i-1]')
i = 1
while True:
    n = 10.0**i
    e_it[i] = np.round((1.0+(1.0/n))**n,13) #this is fine since 1<e_it <10
    #e_it[i] = round_to_n(e_it[i],12)
    N[i] = n
    #new_file.writelines([i,N[i],e_it[i],e_it[i-1]])
    print(i+1,N[i],list(map('{:.11f}%'.format,e_it[i])),list(map('{:.11f}%'.format,e_it[i-1])))
    if e_it[i-1] == e_it[i]:
        break
    i = i+1

# N gets large enough such that 1 + 1/n -> 1 since 1/n gets outside the range of
# of the mantissa. 10^-16 = 2^-53



#print(i,N[i],list(map('{:.12f}%'.format,e_it[i])),list(map('{:.12f}%'.format,e_it[i-1])))
