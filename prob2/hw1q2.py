################################################################################
# Question 2 Homework 1 Susan Redmond
################################################################################
from mpmath import *
import numpy as np


def e_power_series(x,n,sigs):
    e_x = 1.0
    for i in range(1,n+1):
        e_x = e_x + x**i/(factorial(i))
        r = int((sigs-1.0) - floor(log10(e_x)))
        e_x = round(e_x,r)
    return e_x

def round_sigfigs(sigs,y):

    r = int((sigs-1.0) - floor(log10(y)))
    #print((sigs-1.0),floor(log10(y)),r)
    y = round(y,r)
    return y

def npround_sigfigs(sigs,y):

    r = int((sigs-1.0) - np.floor(np.log10(y)))
    #print((sigs-1.0),floor(log10(y)),r)
    y = np.round(y,r)
    return y


def a_power_series(x,n,sigs):

    e_x = 1.0
    num = 1.0
    den = 1.0
    e_xm = np.zeros((31,1))
    e_xm[0] = e_x
    for i in range(1,n+1):
        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)
        #print(i,num,den,num/den)
        e_x = e_x + frac
        e_x = round_sigfigs(sigs,e_x)
        # r = int((sigs-1.0) - floor(log10(e_x)))
        # e_x = round(e_x,r)
        e_xm[i] = e_x
    return e_x, e_xm

def aold_power_series(x,n,sigs):

    e_x = 1.0
    num = 1.0
    den = 1.0
    e_xm = np.zeros((31,1))
    e_xm[0] = e_x
    for i in range(1,n+1):
        num = num*x
        den = den*i
        #print(i,num,den)
        e_x = e_x + num/den
        r = int((sigs-1.0) - floor(log10(e_x)))
        e_x = round(e_x,r)
        e_xm[i] = e_x
    return e_x, e_xm

def b_power_series(x,sigs):
    e_x = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    i = 1
    while True:
        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)
        #print(i,num,den)
        e_x[i] = e_x[i-1] + frac
        # r = int((sigs-1.0) - np.floor(np.log10(e_x[i])))
        # e_x[i] = np.round(e_x[i],r)
        e_x[i] = npround_sigfigs(sigs,e_x[i])
        #print(i,list(map('{:.2f}%'.format,e_x[i])))

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1

    return e_x[0:i]

def c_power_series(x,sigs):
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den
    print(0,Sk[0])
    i = 1
    while True:

        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)
        Sk[i] = frac
        e_x[i] = Sk[i]
        for j in range(i-1,-1,-1):
            e_x[i] = npround_sigfigs(sigs,e_x[i]+Sk[j])
            # e_x[i] = np.sum(Sk[0:i+1],axis= -2)
        ##e_x[i] = e_x[i-1] + num/den
        #r = int((sigs-1.0) - np.floor(np.log10(e_x[i])))
        #e_x[i] = np.round(e_x[i],r)
        e_x[i] = npround_sigfigs(sigs,e_x[i])
        #print(i,Sk[i],e_x[i])
        print(i,list(map('{:.2f}%'.format,e_x[i])))
        #print(e_x[i],e_x[i-1])
        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1


    return e_x[0:i],Sk[0:i]


#e_x = e_power_series(5.5,30,5.0)

################################################################################
# Part a
e_x_a, e_xm = a_power_series(5.5,30,5)
print('Part A \n')
print(e_x_a)

################################################################################
# Part b
print('Part B \n')

e_x_b = b_power_series(5.5,5)
e_x = exp(5.5)

err_b = (e_x - e_x_b[-1])/e_x
print(e_xm)
print('Power Series Output: ',e_x_b[-1],'\nIterations Required: ',e_x_b.size,'\nRelative Error: ',err_b)

################################################################################
# Part c
print('Part C \n')

# Sk = np.ones((3,1))
#
# a = np.sum(Sk[0:3])
# print(Sk.sum(axis=-2))
e_x_c , Sk_c = c_power_series(5.5,5)

err_c = (e_x - e_x_c[-1])/e_x
#print(Sk_c)
print('Power Series Output: ',e_x_c[-1],'\nIterations Required: ',e_x_c.size,'\nRelative Error: ',err_c)
