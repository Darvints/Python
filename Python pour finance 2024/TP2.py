# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:53:46 2024

@author: darvin
"""
#TP2

import math
import scipy.stats
#Exercice1

def ValPresente(VF,r,n):
    """Objectif : Calculer la valeur présente
    VF : Valeur future
    r : Taux d'intérêt
    n : nombre de période
    Formule : VP = VF/(1+r)**n"""
    VP = (VF)/(1+r)**n;
    return VP

ValPresente(100,0.1,1);
ValPresente(100,n=1,r=0.1)

#L'ordre des variable doit être respecté

#On viens de commenté entièrement notre progrmmme
def Interface_VP():
    VF = int(input("Quel est la valeur future?\n"))
    n = int(input("Sur combien de période?\n"))
    r = float(input("Quel est le taux d'intérêt?\n"))
    VP = ValPresente(VF,r,n)
    print("La valeur présente est : " , VP)
    return

#Exercice 2


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
        S = float(input("Quel était le prix à la date 0 de votre actif?\n"))
        S_t = float(input("Quel était le prix à la date t de votre actif?\n"))
        r = float(input("Quel était le taux d'intérêt?\n"))
        sigma = float(input("Que valait sigma?\n"))
        T = float(input("Que vaut T?\n"))
        K = float(input("Quel était le strike?\n"))
    except ValueError:
        print("Erreur de saisie. entrer des valeurs numériques valides.")
        return None
    
    P = Pricing(1, S, K, r, sigma, T)
    phi = CP(1, K, S_t)
    P_p = phi / (1 + r) - P
    return P_p

def erreurSaisie():
    while True:
        result = Net()
        if result is not None:
            return result
        else:
            print("Utilisez avec des valeurs numériques valides.")

def PP():
    result = erreurSaisie()
    return result
