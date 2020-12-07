# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:04:21 2020

@author: k20087271
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

theta12 = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta12")
theta13 = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta13")
theta23 = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta23")
delta   = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/delta  ")

theta12ACB = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta12_ACB")
theta13ACB = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta13_ACB")
theta23ACB = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta23_ACB")
deltaACB   = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/delta_ACB  ")

theta12BCA = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta12_BCA")
theta13BCA = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta13_BCA")
theta23BCA = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/theta23_BCA")
deltaBCA   = np.loadtxt("C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/delta_BCA  ")


ax = plt.subplot()
#print(theta12.shape[0])
J = []
J2 = []
J3 = []

for i in range(200000):
        index = np.random.choice(theta12.shape[0], 4, replace=False) 
        v12 = theta12[index[0]]
        v13 = theta13[index[1]]
        v23 = theta23[index[2]]
        vDl =   delta[index[3]]
        
        s12 = np.sin(v12)
        c12 = np.cos(v12)

        s13 = np.sin(v13)
        c13 = np.cos(v13)

        s23 = np.sin(v23)
        c23 = np.cos(v23)

        sdl = np.sin(vDl)
        cdl = np.cos(vDl)        
        
        J_point_ABC = c12*c13**2*c23*s12*s13*s23*sdl
        
        v12 = theta12ACB[index[0]]
        v13 = theta13ACB[index[1]]
        v23 = theta23ACB[index[2]]
        vDl =   deltaACB[index[3]]
        
        s12 = np.sin(v12)
        c12 = np.cos(v12)

        s13 = np.sin(v13)
        c13 = np.cos(v13)

        s23 = np.sin(v23)
        c23 = np.cos(v23)

        sdl = np.sin(vDl)
        cdl = np.cos(vDl) 
        J_point_ACB = c12**2*c23*c13*s12*s13*s12*sdl
        
        v12 = theta12BCA[index[0]]
        v13 = theta13BCA[index[1]]
        v23 = theta23BCA[index[2]]
        vDl =   deltaBCA[index[3]]
        
        s12 = np.sin(v12)
        c12 = np.cos(v12)

        s13 = np.sin(v13)
        c13 = np.cos(v13)

        s23 = np.sin(v23)
        c23 = np.cos(v23)

        sdl = np.sin(vDl)
        cdl = np.cos(vDl) 
        
        J_point_BCA = c12**2*c23*c13*s23*s13*s12*sdl
        
        J.append(J_point_ABC)
        J2.append(J_point_ACB)
        J3.append(J_point_BCA)
        

sigmaABC = np.std(J)
muABC = np.average(J)

sigmaACB = np.std(J2)
muACB = np.average(J2)

sigmaBCA = np.std(J3)
muBCA = np.average(J3)

kde1 = stats.gaussian_kde(np.array(J))
kde2 = stats.gaussian_kde(np.array(J2))
kde3 = stats.gaussian_kde(np.array(J3))


x_eval = np.linspace(-.1, .1, num=1000)
ax.plot(x_eval, kde1(x_eval), color = 'orange', alpha = 0.4)
ax.plot(x_eval, kde2(x_eval), color = 'turquoise', alpha = 0.5)
ax.plot(x_eval, kde3(x_eval), color = 'mediumspringgreen', alpha = 0.5)


total = []
normal_constant = 0
width = 0.2/len(x_eval)
for i in x_eval:
    i_total = kde1(i)*kde2(i)*kde3(i)
    total.append(i_total)
    normal_constant += i_total*width

total = total/normal_constant
ax.plot(x_eval, total, color = 'blue', linewidth = 2)

#sigmaT = np.std(total)
#muT = np.average(total)
"""
ax.hist(J,bins=60, density = True,  color = "red",    alpha =0.3)
ax.hist(J2,bins=60, density = True,  color = "orange",    alpha =0.5)
ax.hist(J3,bins=60, density = True,  color = "blue",    alpha =0.3)
"""

ax.set_xlim(xmin = -0.08, xmax = 0.02)
"""
x = np.linspace(-0.1,0.05, 100)

plt.plot(x, stats.norm.pdf(x, muABC, sigmaABC), linewidth =0.5)
plt.plot(x, stats.norm.pdf(x, muACB, sigmaACB), linewidth =0.5)
plt.plot(x, stats.norm.pdf(x, muBCA, sigmaBCA), linewidth =0.5)
"""
"""
ax.axvline(x=muABC, color = "blue")
"""
#ax.axvline(x=muT+sigmaT, color = "red", linewidth=0.5)
#ax.axvline(x=muT-sigmaT, color = "red", linewidth=0.5)
#ax.axvline(x=muT+2*sigmaT, color = "red", linewidth=0.6)
#ax.axvline(x=muT-2*sigmaT, color = "red", linewidth=0.6)

#ax.axvline(x=muABC+sigmaABC, color = "deepskyblue", linewidth=0.5)
#ax.axvline(x=muABC-sigmaABC, color = "deepskyblue", linewidth=0.5)
#ax.axvline(x=muABC+2*sigmaABC, color = "aquamarine", linewidth=0.6)
#ax.axvline(x=muABC-2*sigmaABC, color = "aquamarine", linewidth=0.6)
plt.xlabel("J")
plt.ylabel("Pdf( J )")
ax.axvline(x=0, color = "black", linewidth=0.8,linestyle='--',)
plt.plot()


print("sigma (J ABC): " + str("{:.5f}".format(sigmaABC)))
print("sigma (J ACB): " + str("{:.5f}".format(sigmaACB)))
print("sigma (J BCA): " + str("{:.5f}".format(sigmaBCA)))

"""
total = J+J2+J3
ax.hist(total,bins=60, density = True,  color = "yellow",    alpha =0.75)            
plt.plot(x, stats.norm.pdf(x, np.average(total), np.std(total)), linewidth =1.5, color = 'blue') 
"""  

np.savetxt('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_ABC',J,  delimiter = ', ')
np.savetxt('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_ACB',J2, delimiter = ', ')
np.savetxt('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/data/J_BCA',J3, delimiter = ', ')

plt.savefig('C:/Users/k20087271/Documents/pyMC3_Reparametrisation/plots/Jarlskog estimation', dpi = 700)