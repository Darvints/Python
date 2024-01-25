# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:43:46 2024

@author: darvin
"""

"""TP3"""

import math
import scipy


def C_sigma(S,K,r,T,Sigma):
    d1 =(math.log(S/K)+(r+(Sigma**2)/2)*T)/(Sigma*T**(1/2))
    d2 = d1 - Sigma*T**(1/2)
    C = S* scipy.stats.norm.cdf(d1) -K*math.exp(-r*T)*scipy.stats.norm.cdf(d2)
    return C

def Vol_impli(S,K,r,T,C):
    Sigma_b = 0.001
    Sigma_h = 1
    C_b = C_sigma(S,K,r,T,Sigma_b)
    C_h = C_sigma(S,K,r,T,Sigma_h)
    Err = 0.0001
    middle = 0
    n=0
    while abs(C_b - C) > Err and abs(C_h - C) > Err :
        n=n+1
        middle = (Sigma_h + Sigma_b)/2
        test = C_sigma(S,K,r,T,middle)
        if ((test-C)*(C_b-C))<0:
            Sigma_h = middle
            C_h = test
        elif ((test-C)*(C_h-C))<0:
            Sigma_b = middle
            C_b = test
    return middle

def Interface():
    try:
        S = float(input("Quel était le prix à la date 0 de votre actif?\n"))
        r = float(input("Quel était le taux d'intérêt?\n"))
        T = float(input("Que vaut T?\n"))
        K = float(input("Quel était le strike?\n"))
        C = float(input("Quel était le prix?\n"))
        if r<0 or r>1 or C<0:
            C = int("Okey")
    except ValueError:
        print("Erreur de saisie. entrer des valeurs numériques valides.")
        return None
    sigma = Vol_impli(S,K,r,T,C)
    return sigma
        
def erreurSaisie():
    while True:
        result = Interface()
        if result is not None:
            return result
        else:
            print("Utilisez avec des valeurs numériques valides.")

def PP():
    result = erreurSaisie()
    return result
