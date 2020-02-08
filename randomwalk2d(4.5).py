# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:56:35 2018

@author: lili
"""

import numpy as np
import random
import matplotlib.pyplot as plt

#N=1000
x2 = 0
y2 = 0
x=np.zeros(N)
y=np.zeros(N)
def randomwalk2d(N):
    for i in range(1,N):
        rr=random.uniform(0,1)
        z=random.uniform(0,1)
        if rr<0.5 and z<0.5:
            x[i]=x[i-1]+1
            y[i]=y[i-1]
        
        elif rr<0.5 and z>0.5:
            x[i]=x[i-1]-1
            y[i]=y[i-1]
            
        elif rr>0.5 and z<0.5:
                
            x[i]=x[i-1]
            y[i]=y[i-1]+1
        
        else:
        
            x[i]=x[i-1]
            y[i]=y[i-1]-1
    return(x,y)
        
TRY = 1000
for i in range(TRY):
    n=100
    walk = randomwalk2d(n)
    xm = 0
    ym = 0
    for k in range(0,n):
        x2 = x2+(walk[0][k])**2
        y2 = y2 +(walk[1][k])**2
    xm += x2/n
    ym += y2/n
    
xx = xm/TRY
yy = ym/TRY
rmean2 = xx+yy
rmean = 2*N
print(rmean2)
print(rmean)
plt.plot(x,y)
plt.title("2 dimentional random walk , n = 1000")
