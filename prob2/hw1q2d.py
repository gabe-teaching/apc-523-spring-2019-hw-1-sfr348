from mpmath import *
import numpy as np



def round_sigfigs(sigs,y):

    r = int((sigs-1.0) - floor(log10(abs(y))))
    y = round(y,r)
    return y

def npround_sigfigs(sigs,y):

    r = int((sigs-1.0) - np.floor(np.log10(abs(y))))
    y = np.round(y,r)
    return y

def round_to_n(r,x):
    '''Rounds x to r significant digits.'''
    return float('%.*g' % (r,x))



def di_power_series(x,sigs):
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
        Sk[i] = frac#*((-1)**i)
        e_x[i] = e_x[i-1] + Sk[i]
        e_x[i] = npround_sigfigs(sigs,e_x[i])

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1

    return e_x[0:i],Sk[0:i]


def dii_power_series(x,sigs):
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den

    i = 1
    while True:

        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)#*((-1)**i)
        Sk[i] = frac
        e_x[i] = Sk[i]
        for j in range(i-1,-1,-1):
            e_x[i] = npround_sigfigs(sigs,e_x[i]+Sk[j])

        e_x[i] = npround_sigfigs(sigs,e_x[i])

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1


    return e_x[0:i],Sk[0:i]

def diii_power_series(x,sigs):
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den
    f_pos = Sk[0]
    f_neg = 0.0#Sk[1]

    i = 1
    while True:

        num = num*x
        num = round_to_n(sigs,num)
        den = den*i
        den = round_to_n(sigs,den)
        frac = round_to_n(sigs,num/den)#*((-1)**i)
        Sk[i] = frac

        r_pos = np.flip(range(0,i+1,2),0)
        r_neg = np.flip(range(1,i+1,2),0)


        if (i % 2) == 0:
            f_pos = round_to_n(sigs, f_pos + Sk[i])
        else:
            f_neg = round_to_n(sigs, f_neg + Sk[i])

        e_x[i] = f_neg+f_pos
        e_x[i] = round_to_n(sigs,e_x[i])
        print(i,Sk[i],f_neg,f_pos)

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1

    return e_x[0:i],Sk[0:i]
def div_power_series(x,sigs):
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den
    #print(0,Sk[0])
    i = 1
    while True:

        num = num*x


        num = round_to_n(sigs,num)
        den = den*i
        den = round_to_n(sigs,den)
        frac = round_to_n(sigs,num/den)#*((-1)**i)
        Sk[i] = frac

        f_pos = 0.0#Sk[0]
        f_neg = 0.0#Sk[1]
        r_pos = np.flip(range(0,i+1,2),0)
        r_neg = np.flip(range(1,i+1,2),0)
        for j in r_pos:
            f_pos = round_to_n(sigs, f_pos + Sk[j])
        for j in r_neg:
            f_neg = round_to_n(sigs, f_neg + Sk[j])

        e_x[i] = f_neg+f_pos
        e_x[i] = round_to_n(sigs,e_x[i])

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1

    return e_x[0:i],Sk[0:i]

### PART E ###
def e_power_series(x,sigs):
    if x<0:
        x = -x
        sgn = -1
    else:
        sgn = 1
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den

    i = 1
    while True:

        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)#*((-1)**i)
        Sk[i] = frac
        e_x[i] = Sk[i]
        for j in range(i-1,-1,-1):
            e_x[i] = npround_sigfigs(sigs,e_x[i]+Sk[j])

        e_x[i] = npround_sigfigs(sigs,e_x[i])

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1
    if sgn<0:
        e_x[i] = 1.0/e_x[i]
        print(e_x[i])
    return e_x[0:i+1],Sk[0:i+1]

def e2_power_series(x,sigs):
    if x<0:
        x = -x
        sgn = -1.0
    else:
        sgn = 1
    e_x = np.zeros((200,1))
    Sk = np.zeros((200,1))
    e_x[0] = 1.0
    num = 1.0
    den = 1.0
    Sk[0] = num/den
    i = 1
    while True:
        num = num*x
        num = round_sigfigs(sigs,num)
        den = den*i
        den = round_sigfigs(sigs,den)
        frac = round_sigfigs(sigs,num/den)
        Sk[i] = frac#*((-1)**i)
        e_x[i] = e_x[i-1] + Sk[i]
        e_x[i] = npround_sigfigs(sigs,e_x[i])

        if e_x[i-1] == e_x[i]:
            break
        else:
            i = i+1
    if sgn<0:
        e_x[i] = 1.0/e_x[i]
        print(e_x[i])
    return e_x[0:i+1],Sk[0:i+1]

e_x = exp(-5.5)
e_xi,Ski = di_power_series(-5.5,5)
err_i = (e_x - e_xi[-1])/e_x
e_xii,Skii = dii_power_series(-5.5,5)
err_ii = (e_x - e_xii[-1])/e_x
e_xiii,Skiii = diii_power_series(-5.5,5)
err_iii = (e_x - e_xiii[-1])/e_x
e_xiv,Skiv = div_power_series(-5.5,5)
err_iv = (e_x - e_xiv[-1])/e_x

print('PART D\n')
print('Using exp() function:',e_x)
print('Section Iterations  Final Value   Error\n')
print('Part d i  ',e_xi.size,e_xi[-1],err_i)
print('Part d ii ',e_xii.size,e_xii[-1],err_ii)
print('Part d iii',e_xiii.size,e_xiii[-1],err_iii)
print('Part d iv ',e_xiv.size,e_xiv[-1],err_iv)

#### PART E ####
e_xe,Ske = e_power_series(-5.5,5)
err_e = (e_x - e_xe[-1])/e_x
e_xe2,Ske2 = e2_power_series(-5.5,5)
err_e2 = (e_x - e_xe2[-1])/e_x
print('\nPART E\n')
print('Adding Left to Right',e_xe2.size,e_xe[-1],err_e2)
print('Adding Right to Left',e_xe.size,e_xe[-1],err_e)


#print(Ski)
