# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:13:20 2024

@author: darvin
"""

#TP1

#Exercice1

def valeur_present(VF,n,r):
    VP = (VF)/(1+r)**n;
    return VP

def Interface_VP():
    VF = int(input("Quel est la valeur future?\n"))
    n = int(input("Sur combien de période?\n"))
    r = float(input("Quel est le taux d'intérêt?\n"))
    VP = valeur_present(VF,n,r)
    print("La valeur présente est : " , VP)
    return

#Exercice2
CI = 100000
T = 3
R = CI/T
P1 = 10000
P2 = 40000
P3 = 60000
r = 0.05
Remb = P1*(1-r)**2 + P2*(1-r)**1 + P3**(1+r)**0

#exercice 3 
n = 0
print("Les 20 premiers terme de la table de 5 : \n")
while (n<20):
    print("5 x ", n ," = ", n*5 )
    n = n+1

#Exercice 4

def remboursement(r,N,An):
    n = 1
    RAP = N
    print('{} {} {} {}'.format("Année","Annuité","MOntant des intérêt","Reste à Payer"))
    print('{} {} {} {}'.format(0,0,0,RAP))
    while(N>0):
        RAP = N - An + N * r
        if(RAP<0):
            RAP = 0
        print('{} {} {} {}'.format(n,An,r*N,RAP))
        N = N - An + r*N
        n = n+1
    return
        
#Pour aller plus loin

