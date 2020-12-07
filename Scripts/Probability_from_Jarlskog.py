# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:22:02 2020

@author: k20087271
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

J_ABC = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_ABC")
J_ACB = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_ACB")
J_BCA = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_CBA")

L = 295
E = 0.6
m31 = 2.6*10**(-3)
m21 = 7.9*3**(-5)

delta31 = 1.27*L*m31/E 
delta21 = 1.27*L*m21/E 


factor = 1/(16*np.sin(delta21)*np.sin(delta31)**2)
x_eval = np.linspace(-.1, .002, num=1000)
a_eval = factor*x_eval

P_ABC = J_ABC*np.abs(factor)
P_ACB = J_ACB*np.abs(factor)
P_BCA = J_BCA*np.abs(factor)


sigmaABC = np.std(P_ABC)
muABC = np.average(P_ABC)

sigmaACB = np.std(P_ACB)
muACB = np.average(P_ACB)

sigmaBCA = np.std(P_BCA)
muBCA = np.average(P_BCA)

kde1 = stats.gaussian_kde(np.array(P_ABC))
kde2 = stats.gaussian_kde(np.array(P_ACB))
kde3 = stats.gaussian_kde(np.array(P_BCA))



total = []
normal_constant = 0
width = (np.amax(a_eval)-np.amin(a_eval))/len(x_eval)

for i in a_eval:
    i_total = (kde1(i)*kde2(i)*kde3(i))[0]

    if i_total < 10**(-10):
        i_total = 10**(-10)
    total.append(i_total)
    normal_constant += i_total*width

total = total/normal_constant

kdeTOTAL = stats.gaussian_kde(np.array(total))

#////////////////////////////////////////////////////////////////////////////#
#                               PLOTTING TIME                                #
#////////////////////////////////////////////////////////////////////////////#

ax = plt.subplot()

ax.plot(-a_eval, kde1(a_eval), color = 'orange', alpha = 0.4)
ax.plot(-a_eval, kde2(a_eval), color = 'turquoise', alpha = 0.5)
ax.plot(-a_eval, kde3(a_eval), color = 'mediumspringgreen', alpha = 0.5)
ax.plot(-a_eval, total, color = 'blue', linewidth = 2)

ax.axvline(x=0, color = "black", linewidth=0.8,linestyle='--',)

plt.xlabel("ΔP")

plt.plot()
plt.show()
plt.savefig('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/plots/prob estimation', dpi = 700)

ax2 = plt.subplot()

ax2.plot(-a_eval*30, kde1(a_eval), color = 'orange', alpha = 0.4)
ax2.plot(-a_eval*30, kde2(a_eval), color = 'turquoise', alpha = 0.5)
ax2.plot(-a_eval*30, kde3(a_eval), color = 'mediumspringgreen', alpha = 0.5)
ax2.plot(-a_eval*30, total, color = 'blue', linewidth = 2)

ax2.axvline(x=0, color = "black", linewidth=0.8,linestyle='--',)

plt.xlabel("% ΔP")

plt.plot()

plt.savefig('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/plots/prob estimation (percentage)', dpi = 700)

