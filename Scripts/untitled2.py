# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:22:25 2020

@author: k20087271
"""

import numpy as np
import matplotlib.pyplot as plt


mumu  = np.random.normal(0.27,0.03,400)
mue   = np.random.normal(0.35,0.03,400)
total = mumu + mue

ax = plt.subplot()

ax.hist(mumu,bins = 40,  density = True,  color = "red",     alpha =0.8)
ax.hist(mue,bins = 40,   density = True,  color = "orange",  alpha =0.8)
ax.hist(total,bins = 40, density = True,  color = "blue",    alpha =0.1)

ax.set_xlim(xmin = 0, xmax = 1)
plt.show()