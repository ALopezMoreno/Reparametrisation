# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:31:36 2020

@author: k20087271
"""

import pymc3 as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import theano
import seaborn as sns
import theano.tensor as t

RANDOM_SEED = 58

pi = np.pi
ACB_model = pm.Model()  
L = 295
E = 0.6
m31 = 2.6*10**(-3)

delta31 = 1.27*L*m31/E #we set M21 = 0



if __name__ == '__main__':
    with ACB_model:
        
        #priors for unknown model parameters:
        theta12 = pm.Uniform("theta12",0,pi/2.) #mu = 0.57, sigma = 0.1)        #0,pi/2.)
        theta13 = pm.Uniform("theta13",0,pi/2.) #mu = 0.82, sigma = 0.1)        #0,pi/2.)
        theta23 = pm.Uniform("theta23",0,pi/2.) #mu = 0.14, sigma = 0.1)        #0,pi/2.)
        delta   = pm.Uniform("delta", pi - 0.1,2.*pi)
        
        #shortenings:
        c13 = t.cos(theta13)
        s13 = t.sin(theta13)
        
        c23 = t.cos(theta23)
        s23 = t.sin(theta23)
    
        c12 = t.cos(theta12)
        s12 = t.sin(theta12)
        
        cDEL = t.cos(delta)
        sDEL = t.sin(delta)
        
        
        
        #We build the PMNX matrix in this parametrisation:
            
            
        U11 = c12*c13
        U12 = t.sqrt( (s12*c23*c13 - s23*s13*cDEL)**2 + (s23*s13*sDEL)**2 )
        U13 = t.sqrt( (s23*c13*s12 + c23*s13*cDEL)**2 + (c23*s13*sDEL)**2 )
        
        U21 = s12
        U22 = c12*c23
        U23 = c12*s13
        
        U31 = t.sqrt( (c12*s13*cDEL)**2 + (c12*s13*sDEL)**2 )
        U32 = t.sqrt( (s23*c13 + c23*s13*s12*cDEL)**2 + (c23*s13*s12*sDEL)**2 )
        U33 = t.sqrt( (c13*c23 - s12*s13*s23*cDEL)**2 + (s12*s13*s23*sDEL)**2 )
        
        
        P_mue_REAL =  - s12**2*s23**2*c12**2*c13**2 - c12**2*cDEL*c23*c13*s23*s13*s12 \
                      + s12**2*s23**2*c12**2*c13**2*c23**2 - s13**2*s23**2*c12**2*c23**2
                     
      
        P_mue_IMAG = c12**2*c23*c13*s13*s23*s12*sDEL
        #muon to electron
        P_mue = -4*P_mue_REAL*(t.sin(delta31)**2) + 2*P_mue_IMAG*t.sin(2*delta31)        
        
        #We give the observed values for the PMNX matrix:
        
        PMNS11 = pm.Normal("U(11)", mu = U11, observed = np.random.normal(0.8215, 0.026/3., 300))
        PMNS12 = pm.Normal("U(12)", mu = U12, observed = np.random.normal(0.5490, 0.033/3., 300))
        PMNS13 = pm.Normal("U(13)", mu = U13, observed = np.random.normal(0.1485, 0.008/3., 300))
        
        PMNS21 = pm.Normal("U(21)", mu = U21, observed = np.random.normal(0.3680, 0.126/3., 300))
        PMNS22 = pm.Normal("U(22)", mu = U22, observed = np.random.normal(0.5725, 0.106/3., 300))
        PMNS23 = pm.Normal("U(23)", mu = U23, observed = np.random.normal(0.7065, 0.068/3., 300))
        
        PMNS31 = pm.Normal("U(31)", mu = U31, observed = np.random.normal(0.4025, 0.119/3., 300))
        PMNS32 = pm.Normal("U(32)", mu = U32, observed = np.random.normal(0.5925, 0.103/3., 300))
        PMNS33 = pm.Normal("U(33)", mu = U33, observed = np.random.normal(0.6845, 0.070/3., 300))

        #And for muon to electron channel
        P_obs_mue  = pm.Normal("prob-MuE" ,mu = P_mue, observed = np.random.normal(0.3,0.07,300))            
        #We run the bayesian sampling:
            
        trace = pm.sample(tune = 15000, draws= 10000)
        ppc = pm.sample_posterior_predictive(trace, var_names=["theta12", "theta13", "theta23", "delta"], random_seed=RANDOM_SEED)
    
    #Plots
    pm.traceplot(trace)
    az.plot_pair(trace,divergences = True)
   
    pm.plot_posterior(trace)


    data_theta12 = np.asarray(ppc["theta12"])
    data_theta13 = np.asarray(ppc["theta13"])
    data_theta23 = np.asarray(ppc["theta23"])
    data_delta   = np.asarray(ppc["delta"]  )

    np.savetxt("C:/Users/k20087271/Documents/Reparametrisation data/theta12_BCA", data_theta12, delimiter = ', ')
    np.savetxt("C:/Users/k20087271/Documents/Reparametrisation data/theta13_BCA", data_theta13, delimiter = ', ')
    np.savetxt("C:/Users/k20087271/Documents/Reparametrisation data/theta23_BCA", data_theta23, delimiter = ', ')
    np.savetxt("C:/Users/k20087271/Documents/Reparametrisation data/delta_BCA  ", data_delta  , delimiter = ', ')
