# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:14:26 2024

@author: darvin
"""

""" TP4"""
from TP2 import *

import math
import scipy
import numpy as np

#Exercice 1
import pylab as pl
X = [0,1,2,3]
Y = [1,2,4,10]
pl.plot(X,Y)
pl.title("Premier graphique")
pl.xlabel("Abcisse")
pl.ylabel("Ordonnée")

# Exercice 2

def Pricing(typeOpt,S,K,r,sigma,T):
    d1 = (math.log(S/K)+(r+(sigma**2)/2)*T)/(sigma * T**(1/2))
    d2 = d1 - sigma * T**(1/2)
    Prix = typeOpt * S * scipy.stats.norm.cdf(typeOpt * d1) - typeOpt * K * math.exp(-r*T) * scipy.stats.norm.cdf(typeOpt * d2)
    return Prix    

def CP(typeOpt,K,S):
    if typeOpt == 1:
        phi = max(S-K,0)
    if typeOpt == -1:
        phi = max(K-S,0)
    return phi

def Interface_CP(K,S):
    typeOpt = int(input("Si c'est un call, entrez 1.\n Si c'est un put, entrez 0.\n"))
    return CP(typeOpt,K,S)
    
def Net():
    try:
        typeopt = int(input("SI c'est un Call entrée 1 , si c'est un Put entrez -1!"))
        S = float(input("Quel était le prix à la date 0 de votre actif?\n"))
        r = float(input("Quel était le taux d'intérêt?\n"))
        sigma = float(input("Que valait sigma?\n"))
        T = float(input("Que vaut T?\n"))
        K = float(input("Quel était le strike?\n"))
        if r<0 or r>1 or (typeopt!=1 and typeopt!=-1) :
            K = int("Okey")
    except ValueError:
        print("Erreur de saisie. entrer des valeurs numériques valides.")
        return None
    
    P = Pricing(typeopt, S, K, r, sigma, T)
    n = 10000
    L = np.zeros(n+1)
    for i in range(n+1):
        L[i] = i/n * 100
        
    P_t = np.zeros(n+1)
    for i in range(n+1):
        phi = CP(typeopt, K, L[i])
        P_t[i] = phi / (1 + r) - P
    return P_t,typeopt, S , r , sigma , T , K

def erreurSaisie():
    while True:
        [result,typeopt,S,r,sigma,T,K] = Net()
        if result is not None:
            return result,typeopt, S, r , sigma, T, K
        else:
            print("Utilisez avec des valeurs numériques valides.")

def PP():
    [result,typeopt,S,r,sigma,T,K] = erreurSaisie()
    n = 10000
    L = np.zeros(n+1)
    y = np.zeros(n+1)
    for i in range(n+1):
        L[i] = i/n * 100
    if typeopt==1:
        pl.plot(L,result,L,y,'--')
        pl.title("Profit/Perte d'un call Européen \n S={}, K={}, sigma={}, r={}, T={}".format(S, K, sigma, r, T))
        pl.xlabel("S_t")
        pl.ylabel("Profit/Perte")
    if typeopt==-1:
        pl.plot(L,result,L,y,'--')
        pl.title("Profit/Perte d'un put Européen \n S={}, K={}, sigma={}, r={}, T={}".format(S, K, sigma, r, T))
        pl.ylabel("Profit/Perte")
    return 


#Exercice 3

import pandas as pd

fichier = "alstom.csv"
df = pd.read_csv(fichier,delimiter=';')
df
df['Call']
df['Call'][2]

def function(fichier,Sj,r,T):
    
