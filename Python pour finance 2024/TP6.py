# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:33:15 2024

@author: darvin
"""

#TP6
import matplotlib.pyplot as plt
import math
import numpy as np

def Call(r,T,p,G,H):
    C = math.exp(-r*T)*(p*G+(1-p)*H)
    return C

def branche():
    
        