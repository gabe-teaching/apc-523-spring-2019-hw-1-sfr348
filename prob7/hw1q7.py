from mpmath import *
from sympy import *
import numpy as np
import math
from scipy import optimize as opt

# Part a:
x = Symbol('x')
y = Symbol('y')
# wn = (x-1)
# for i in range(2,21):
#     wn = (x-i)*wn
wn = (x-1.0)
for i in range(2,21):
    j = float(i)
    wn = (x-j)*wn

#print(expand(wn))
#w = Poly(x**20 - 210*x**19 + 20615*x**18 - 1256850*x**17 + 53327946*x**16 - 1672280820*x**15 + 40171771630*x**14 - 756111184500*x**13 + 11310276995381*x**12 - 135585182899530*x**11 + 1307535010540395*x**10 - 10142299865511450*x**9 + 63030812099294896*x**8 - 311333643161390640*x**7 + 1206647803780373360*x**6 - 3599979517947607200*x**5 + 8037811822645051776*x**4 - 12870931245150988800*x**3 + 13803759753640704000*x**2 - 8752948036761600000*x + 2432902008176640000)

# Part b:
w = Poly(expand(wn)) #symbolic version
w_c = np.array(w.coeffs())
w_np = np.poly1d(w_c) #numpy version
#print(w_c[0])
# print(w(0))
# print(w(1))
# print(sum(w_c))
w_roots_newton = opt.newton(w, 21,maxiter=1000)
w_roots_newton2 = opt.newton(np.polynomial.Polynomial(w_c), 21,maxiter=1000)

print(w_c)
print('Newton-Raphson: ',w_roots_newton)
#print('\nNewton-Raphson2: ',w_roots_newton2)
print('\nPoly1d.roots: ',w_np.r[0])

# Part c:
w_rnewt = np.zeros([4,1])
w_rp = np.zeros([4,1])
w_cn = np.array(w.coeffs())
print('PART C: \n')
for i in range(1,5):
    w_cn[0] = 1.0 + 10**-(2*i)
    w_npn = np.poly1d(w_cn)
    w_rnewt[i-1]= opt.newton(w_npn, 21,maxiter=1000)
    w_rp[i-1] = w_npn.r[0]
    print(w_cn[0] ,',',w_rnewt[i-1],',',w_rp[i-1])


#Part d:
print('PART D: \n')

w_rnewt = np.zeros([4,1])
w_rp = np.zeros([4,1])
w_cn = np.array(w.coeffs())
w_cn[1] = w_cn[1] - 2**-(23)
w_npn = np.poly1d(w_cn)
w_rnewt_d= opt.newton(w_npn, 16,maxiter=1000)
w_rp_d = w_npn.r
print(w_cn[1] ,',',w_rp_d[4],',',w_rp_d[3])
#print('\n',w_rp_d)


#Part e ii:
print('PART E ii: \n')

def condOmega(omega_k,dp,w):
    cond_O = 0.0
    w_c = np.array(w.coeffs())
    #print(w_c)
    w_c = np.flip(w_c,0)
    #print(w_c)

    for i in range(0,21):
        cond_O = cond_O + abs(w_c[i]*(omega_k**(i-1))/dp(omega_k))
    return cond_O

dp = diff(w,x)
#omega_k = 14
roots = np.array(w_np.r)
roots = np.flip(roots,0)
#print(roots)
c14 = condOmega(roots[13],dp,w)
c16 = condOmega(roots[15],dp,w)
c17 = condOmega(roots[16],dp,w)
c20 = condOmega(roots[19],dp,w)
print('Condition Numbers for:\n')
print('| Root 14 | Root 16 | Root 17 | Root 20 |\n')
print(c14,c16,c17,c20)

# dw_c = np.zeros((19,1))
# for i in range(0,20,i):
#     dw_c[i] = w_c[i+1]*(19-i)
#print(w_c,'\n',dw_c)
