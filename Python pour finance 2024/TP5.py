# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:50:11 2024

@author: darvin
"""

#TP5

import pylab as pl

S = 0
h = 1.1
b = 0.9

fig, ax = pl.subplots()

ax.text(0, S, 'S', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')

# haut1
ax.arrow(0, S, 1, S+h, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
ax.text(1, S+h, 'S+h', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')

#bas1
ax.arrow(0, S, 1, S-b, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
ax.text(1, S-b, 'S-b', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')

# Affichage
pl.show()

import matplotlib.pyplot as plt

def Branche(n, S, h, b,ax):    
    for i in range(n):
        P = S * (h**(n-1-i)) * b**(i)
        Q = h*(n-1-i) - b*i
        ax.arrow(n-1, Q, 1, h, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
        ax.text(n, Q+h, f'{P*h:.2f}', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')
    
        ax.arrow(n-1, Q, 1,-b , head_width=0.05, head_length=0.1, fc='blue', ec='blue')
        ax.text(n, Q-b, f'{P*b:.2f}', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')

    
def ArbreBinomial(N):
    S=35
    h=1.1
    b = 0.9
    fig, ax = plt.subplots()
    ax.text(0, 0, S, fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='blue')
    for i in range(N):
        Branche(i+1, S, h, b,ax)
        
    ax.set_axis_off()
    plt.title("Arbre binomial (peu esthétique)")
    plt.show()

ArbreBinomial(10)

