# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:58:21 2018

@author: lili
"""

import numpy as np
import random
import matplotlib.pyplot as plt

count = 0
v=0
p=0.4
def random_walk(n):
   
    x =  0
    # y = 0
    for i in range(n):
        r=random.uniform(0,1)
        if r >= p:
            x = x+1
        if r < p:
            x = x-1
        
    return(x,i)
    

TRY = 100
for i in range(TRY):
    n=10
    walk = random_walk(n)
    count = count+walk[0]
    v = v +(walk[0])**2
    
    
    #print(walk)
mean = (count/TRY)
var = (v/TRY)-(mean)**2
var1 = 4*n*p*(1-p)
q=1-p
mean1=n*(q-p)
print(mean)
print(mean1)
print(var)
print(var1)
