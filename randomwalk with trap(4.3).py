# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:57:11 2018

@author: lili
"""

import numpy as np
import random
import matplotlib.pyplot as plt
p = 0.5

for x in range(0,20):
    c=0
    for j in range(0,1000):
        start = x
        in_trap=False
        N = 0 #ghadam ha
        while(in_trap == False):
            r = random.uniform(0,1)
            if r <=p:
                start = start +1
                N = N+1
                if start < 0 or start >20:
                    in_trap = True
            elif r > p :
                start = start -1
                N = N+1
                if start < 0 or start >20:
                    in_trap = True
        c=c+N

    plt.scatter(x,c/1000)
    
plt.xlabel("initial_x")
plt.ylabel("life time")
plt.title("1 dimentional random walk with trap #RUN = 1000")
        


    
    