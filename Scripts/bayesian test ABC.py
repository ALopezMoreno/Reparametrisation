# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymc3 as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import theano
import seaborn as sns

pi = np.pi
ABC_model = pm.Model()  
L = 295
E = 0.6
m31 = 2.6*10**(-3)

delta31 = 1.27*L*m31/E #we set M21 = 0

if __name__ == '__main__':
    with ABC_model:
        
        #priors for unknown model parameters:
        theta12 = pm.Uniform("theta12",0,pi/2.) #mu = 0.57, sigma = 0.1)        #0,pi/2.)
        theta13 = pm.Uniform("theta13",0,pi/2.) #mu = 0.82, sigma = 0.1)        #0,pi/2.)
        theta23 = pm.Uniform("theta23",0,pi/2.) #mu = 0.14, sigma = 0.1)        #0,pi/2.)
        delta   = pm.Uniform("delta",0,2.*pi)
        
        #shortenings:
        c13 = theano.tensor.cos(theta13)
        s13 = theano.tensor.sin(theta13)
        
        c23 = theano.tensor.cos(theta23)
        s23 = theano.tensor.sin(theta23)
    
        c12 = theano.tensor.cos(theta12)
        s12 = theano.tensor.sin(theta12)
        #expression for our probability:

        #for muon to muon    
        P_mumu = 1 - 4*((c13**2)*(s23**2)*((s13**2)*(s23**2)*(c12**2) \
                                          +(s12**2)*(c23**2)         \
                                          +s23*s13*s12*c23*2*theano.tensor.cos(delta) \
                                          *(c12 - s12))*(theano.tensor.sin(delta31))**2)
        #real and imaginary parts of muon to electron
        P_mue_REAL = (c13**2)*(-(s13**2)*(s23**2)*(c12**2) -(c23*c12*s23*s13*s12  * theano.tensor.cos(delta)) \
                               -(s12**2)*(s13**2)*(s23**2) +((s12**2)*c23*s23*s13 * theano.tensor.cos(delta)))
            
        P_mue_IMAG = (c13**2)*(c23*c12*s23*s13*s12*theano.tensor.sin(delta)) \
                              -(s12**2)*(c23*s23*s13*theano.tensor.sin(delta))
        #muon to electron
        P_mue = -4*P_mue_REAL*(theano.tensor.sin(delta31)**2) + 2*P_mue_IMAG*theano.tensor.sin(2*delta31)    
        
        #we use PMNS(13) to further constrain
        U_13  = s13*theano.tensor.sqrt( (theano.tensor.cos(delta))**2 + (theano.tensor.sin(delta))**2)
        
        P_obs_mumu = pm.Normal("prob-MuMu",mu = P_mumu, observed = np.random.normal(0.27,0.01,400))
        P_obs_mue  = pm.Normal("prob-MuE" ,mu = P_mue,  observed = np.random.normal(0.35,0.01,400))
        PMNS_13    = pm.Normal("PMNS_13"  ,mu = U_13,   observed = np.random.normal(0.15,0.01,400))
        
        
        #step = pm.Slice()     $$$we use NUTS as recomended$$$
        trace = pm.sample(tune = 8000, draws= 8000)      # ,return_inferencedata=True)
    



    az.plot_trace(trace)
    az.plot_pair(trace,divergences = True)

    
    #ppc = np.asarray(pm.sample_ppc(trace, samples=1, model=ABC_model, size=1))

    
    az.plot_posterior(trace)



