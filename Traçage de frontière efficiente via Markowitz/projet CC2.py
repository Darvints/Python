# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:55:39 2024

@author: Darvin
"""
import pylab as py
import yfinance as yf
import itertools
import numpy as np

def rdt(A):
    rdt = []
    n = len(A)
    for i in range(n-1):
        rdt.append(A[i+1]/A[i] - 1)
    return rdt

def rendement(A):
    dt = 1/256
    n=len(A)
    S = py.mean(A)
    S = S/dt
    V = py.std(A)
    V = V * n**(1/2) /(dt*(n-1) )**(1/2)
    S = round(S,3)
    V = round(V,3)
    return S,V

def RV(A):
    A = rdt(A)
    return rendement(A)
A = py.array([109.8 , 108.3, 107.6, 108, 107.2, 108.1, 109.3, 110.6, 108.8, 107.2, 107.6])

B = py.array(yf.Ticker('ML.PA').history('1y').Close)
rendement(B)

def import_action(nom):
    B = py.array(yf.Ticker(nom).history('1y').Close)
    return B

B = py.array([100,100,100,100,100,100,100,100,100,100,100])
def RV2(A,B):
    A = rdt(A)
    B = rdt(B)
    dt = 1/256
    R = [rendement(A)[0],rendement(B)[0]]
    vc = py.matrix.round(py.cov(A,B)/dt,3)
    return R,vc

def RV5(A,B,C,D,E):
    A = rdt(A)
    B= rdt(B)
    C = rdt(C)
    D = rdt(D)
    E = rdt(E)
    dt = 1/256
    R = [rendement(A)[0],rendement(B)[0],rendement(C)[0],rendement(D)[0],rendement(E)[0]]
    data = py.column_stack((A, B, C, D, E))
    
    # Calculer la matrice de covariance et l'arrondir
    vc = py.matrix.round(py.cov(data, rowvar=False) / dt, 3)
    
    return R, vc

def Principal(L):
    A = import_action(L[0])
    B = import_action(L[1])
    C = import_action(L[2])
    D = import_action(L[3])
    E = import_action(L[4])
    return RV5(A,B,C,D,E)
        
L = ['ML.PA','GLE.PA','DG.PA','SAN.PA','OR.PA']

R = Principal(L)[0]
cov = Principal(L)[1]
Omega = py.linspace(-1,1,41)

X_list = []
Y_list = []

for i in itertools.product(Omega, repeat=5):
    if sum(i) == 1:
        i_array = py.array(i)
        Y_list.append(py.dot(i_array, R))
        X_list.append(py.dot(py.dot(i_array,cov), i_array))

# Convertir les listes en vecteurs NumPy après avoir terminé toutes les itérations
X = py.array(X_list)
Y = py.array(Y_list)


n = len(X)
Z = py.zeros(n)
k = 0
W = py.matrix.round(Y,2)
for i in itertools.product(Omega, repeat=5):
    if sum(i) == 1:
        i_array = py.array(i)
        j = round(py.dot(i_array, R),2)
        Lo = 1
        for u in range(n):
            if W[u] == j and X[u] < Lo:
                Lo = X[u]
        Z[k] = Lo
        k = k+1


##Partie 3

U = py.ones(5)
U_t = py.transpose(U)
cov = Principal(L)[1]
cov_inv = py.linalg.inv(cov)
mu = Principal(L)[0]
mu_t = py.transpose(mu)
a = py.dot(py.dot(U_t,cov_inv),U)
b = py.dot(py.dot(U_t,cov_inv),mu)
c = py.dot(py.dot(mu_t,cov_inv),mu)
h = (1/(a*c-b**2))*py.dot(cov_inv,py.multiply(a,mu) - py.multiply(b , U))

g = (1/(a*c-b**2))*py.dot(cov_inv,py.multiply(c,U) - py.multiply(b , mu))

R = py.linspace(min(Y),max(Y),1001)


w = []


for r in R:
    w.append(g + h * r)

w = np.array(w)

R = Principal(L)[0]
X_min= py.zeros(1001)
Y_2 = py.zeros(1001)
for i in range(1001):
    Y_2[i] = py.dot(w[i], R)
    X_min[i] = py.dot(py.dot(w[i],cov), w[i])

py.plot(X, Y, 'b.')  # Points bleus pour la frontière efficiente
py.plot(X_min, Y_2, 'r.', label='Frontière efficiente')  # Points rouges pour une autre série de points
py.xlabel('Risque (Variance)')
py.ylabel('Rendement')
py.title('Comparaison de deux séries de points')
py.legend()  # Afficher la légende
py.grid(True)
py.show()

