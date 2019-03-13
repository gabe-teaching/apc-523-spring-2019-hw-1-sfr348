from mpmath import *
import numpy as np
import matplotlib.pyplot as plt


# def rel_error(x,eps):
#     rel_err = (x*np.exp(-x)/(1.0-np.exp(-x)))*(np.exp(x)/x)*eps
#     return rel_err


x = np.linspace(0,1,1001,endpoint=True)
condf = np.empty_like(x)
condA = np.empty_like(x)

xex = np.multiply(x,np.exp(-x))
den = (1.0-np.exp(-x))
condf = np.divide(xex,den)
condA = np.divide(np.exp(x),x)

# err_b1 = rel_error(-np.log(0.5),2^-53)
# err_b2 = rel_error(-np.log(0.75),2^-53)
# err_b3 = rel_error(-np.log(7/8),2^-53)
# err_b4 = rel_error(-np.log(15/16),2^-53)
# print('b = 1 | b = 2 | b = 3 | b = 4\n')
# print(err_b1,err_b2,err_b3,err_b4)







plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
color = 'tab:red'
ax1.set_ylabel('Problem Condition Number',color=color)
plt.xlabel('X')
ax1.set_title('Condition Number')
ax1.plot(x,condf,color=color)
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.plot(x,condA,color=color)
ax2.set_ylabel('Algorithm Condition Number', color=color)  # we already handled the x-label with ax1
ax2.tick_params(axis='y', labelcolor=color)
plt.legend(['cond(F)','cond(A)'], loc='upper right')
plt.show()
# plt.plot(x,condA)
# plt.legend(['cond(F)','cond(A)'], loc='upper right')
# plt.show()
