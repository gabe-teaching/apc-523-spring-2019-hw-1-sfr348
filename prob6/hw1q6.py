import numpy as np
import math
import matplotlib.pyplot as plt

plt.close('all')
PLOT=1


def sqrtsq_func(x_nom,num):
    x = x_nom
    for i in range(num):
        #x = map(lambda y: np.sqrt(y), x)
        x = np.sqrt(x)

    #check = x/(2**-53)
    xr = np.round(x,16)
    #plt.plot(x_nom,xr)
    #plt.show()

    check = x % (2**-53) == 0
    # print(check)
    inds_perf = np.array((check>=1).nonzero())

    for i in range(num):
        #x = map(lambda y: y*y, x)
        x = x*x

    dx = np.diff(x)
    inds = np.array((dx>0.0012).nonzero())
    inds = inds+1
    inds = np.append([0,1,2],inds)
    #print(x_nom[inds])
    return inds,inds_perf, x

# (0.12776 + 0.560911*exp(0.499044x))/1000


#x_nom = np.linspace(0,1,1001,endpoint=True)
x_nom = np.linspace(1,10,1001,endpoint=True)

inds49,inds49p,x49 = sqrtsq_func(x_nom,49)
inds50,inds50p,x50 = sqrtsq_func(x_nom,50)
inds51,inds51p,x51 = sqrtsq_func(x_nom,51)
inds52,inds52p,x52 = sqrtsq_func(x_nom,52)
inds53,inds53p,x53 = sqrtsq_func(x_nom,53)
inds54,inds54p,x54 = sqrtsq_func(x_nom,54)

print(inds52,inds52p,x52)
#(0.944663/1000)exp(0.498203x)
#np.expfit(x_nom[inds])
#[x+1.0 for x in inds]
#x_good = set(np.round(x,9)).intersection(x_nom)
#print(inds)
#


if PLOT == 1:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    fig = plt.figure()#(figsize = [10, 5])
    ax1 = fig.add_subplot(3, 2, 1)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax1.set_title('X Square Rooted 49 Times then Squared 49 Times')
    #plt.subplots_adjust(top=0.3)
    plt.plot(x_nom,x49)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds49],x49[inds49],'k*')
    plt.legend([r"$y=[x^{\frac{1}{2^{49}}}]^{2^{49}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)
    ax2 = fig.add_subplot(3, 2, 2)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax2.set_title('X Square Rooted 50 Times then Squared 50 Times')
    plt.plot(x_nom,x50)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds50],x50[inds50],'k*')
    plt.legend([ r"$y=[x^{\frac{1}{2^{50}}}]^{2^{50}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)
    ax3 = fig.add_subplot(3, 2, 3)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax3.set_title('X Square Rooted 51 Times then Squared 51 Times')
    #plt.subplots_adjust(top=0.8)
    plt.plot(x_nom,x51)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds51],x51[inds51],'k*')
    plt.legend([ r"$y=[x^{\frac{1}{2^{51}}}]^{2^{51}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)
    ax4 = fig.add_subplot(3, 2, 4)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax4.set_title('X Square Rooted 52 Times then Squared 52 Times')
    #plt.subplots_adjust(top=0.03)
    plt.plot(x_nom,x52)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds52],x52[inds52],'k*')
    plt.legend([r"$y=[x^{\frac{1}{2^{52}}}]^{2^{52}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)
    ax5 = fig.add_subplot(3, 2, 5)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax5.set_title('X Square Rooted 53 Times then Squared 53 Times')
    plt.plot(x_nom,x53)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds53],x53[inds53],'k*')
    plt.legend([r"$y=[x^{\frac{1}{2^{53}}}]^{2^{53}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)
    ax6 = fig.add_subplot(3, 2, 6)
    plt.ylabel('Y')
    plt.xlabel('X')
    ax6.set_title('X Square Rooted 54 Times then Squared 54 Times')
    plt.plot(x_nom,x54)
    plt.plot(x_nom,x_nom)
    plt.plot(x_nom[inds54],x54[inds54],'k*')
    plt.legend([ r"$y=[x^{\frac{1}{2^{54}}}]^{2^{54}}$",'y = x',], loc='upper left')
    plt.subplots_adjust(hspace = 0.5)



    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')
    # fig = plt.figure(figsize = [10, 5])
    # ax1 = fig.add_subplot(1, 1, 1)
    # plt.ylabel('dY')
    # plt.xlabel('X')
    # ax1.set_title('diff(Y)')
    # plt.plot(x_nom[0:-1],dx)
    #
    #
    # fig2 = plt.figure(figsize = [10, 5])
    # ax2 = fig2.add_subplot(1, 1, 1)
    # plt.ylabel('N')
    # plt.xlabel('Y')
    # ax2.set_title('Histogram X Square Rooted 52 Times then Squared 52 Times')
    # plt.hist(x,100)
    plt.show()



#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#fig = plt.figure(figsize = [10, 5])
#ax1 = fig.add_subplot(1, 1, 1)
# plt.xlim(0,1.0)
# plt.ylabel('Y')
# plt.xlabel('X')
#ax1.set_title(r"$[x^{\frac{1}{2^{52}}]^{2^{52}}$")
#self.ax1.set_yscale('log')
#plt.plot(x_nom,x)
#fig = plt.figure()
