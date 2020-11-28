# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:15:05 2020

@author: k20087271
"""
import arviz as az
import theano
import pymc3 as pm
import numpy as np

ABC_model = pm.Model()
if __name__ == '__main__':
    with ABC_model:
        angle = pm.Uniform("theta", 0, 2*3.141592)
        
        p = pm.Normal("sin", mu = theano.tensor.sin(angle), observed = np.random.normal(0,0.0001,1000))
        

        trace = pm.sample(tune = 1000, draws=5000, return_inferencedata=True)
    
    az.plot_trace(trace)
    #az.plot_pair(trace,divergences = True)