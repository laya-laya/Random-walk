# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:17:25 2018

@author: lili
"""

import numpy as np
import random
import matplotlib.pyplot as plt
l = 1
size=10
p=0.5
def randomwalk(N):
    x=np.zeros(N)
    start=0
    x[0]=start
    for t in range(1,N):
        rr=random.uniform(0,1)
        if rr<p:
            start=start+1
            
            
            
        elif rr>p:
            start=start-1
          
            
        x[t]=start
    return x

plt.plot(randomwalk(40))
plt.xlabel("tedade ghadam ha")
plt.ylabel("makan(x)")