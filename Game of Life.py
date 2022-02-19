# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:27:09 2022

@author: Léopo
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def créeplateau(n):
    return np.zeros(shape=(n,n),dtype=float)

def affiche(plateau):
    plt.imshow(plateau,'Greys',vmin=0,vmax=1)
    
def début(plateau):
    for i in range(plateau.shape[0]):
        for j in range(plateau.shape[1]):
            plateau[i][j]=random.getrandbits(1)
    return plateau
    
    
    
def itération(plateau):
    born=[]
    dead=[]
    l=plateau.shape[0]
    for i in range(l):
        for j in range(l):
            voisins=0
            if i==0:
                if j==0:
                    if plateau[i+1][j]==1:
                        voisins+=1
                    if plateau[i+1][j+1]==1:
                        voisins+=1
                    if plateau[i][j+1]==1:
                        voisins+=1
                elif j==l-1:
                    if plateau[i+1][j]==1:
                        voisins+=1
                    if plateau[i+1][j-1]==1:
                        voisins+=1
                    if plateau[i][j-1]==1:
                        voisins+=1              
                else:
                    if plateau[i][j-1]==1:
                        voisins+=1
                    if plateau[i][j+1]==1:
                        voisins+=1
                    if plateau[i+1][j-1]==1:
                        voisins+=1    
                    if plateau[i+1][j]==1:
                        voisins+=1
                    if plateau[i+1][j+1]==1:
                        voisins+=1
            elif i==l-1:
                if j==0:
                    if plateau[i-1][j]==1:
                        voisins+=1
                    if plateau[i-1][j+1]==1:
                        voisins+=1
                    if plateau[i][j+1]==1:
                        voisins+=1
                elif j==l-1:
                    if plateau[i-1][j-1]==1:
                        voisins+=1
                    if plateau[i-1][j]==1:
                        voisins+=1
                    if plateau[i][j-1]==1:
                        voisins+=1      
                else:
                    if plateau[i-1][j-1]==1:
                        voisins+=1
                    if plateau[i-1][j]==1:
                        voisins+=1
                    if plateau[i-1][j+1]==1:
                        voisins+=1    
                    if plateau[i][j-1]==1:
                        voisins+=1
                    if plateau[i][j+1]==1:
                        voisins+=1
            elif j==0 and i!=0 and i!=l-1:
                if plateau[i-1][j]==1:
                    voisins+=1
                if plateau[i-1][j+1]==1:
                    voisins+=1
                if plateau[i][j+1]==1:
                    voisins+=1
                if plateau[i+1][j]==1:
                    voisins+=1
                if plateau[i+1][j+1]==1:
                    voisins+=1
            elif j==l-1 and i!=0 and i!=l-1:
                if plateau[i-1][j-1]==1:
                    voisins+=1
                if plateau[i-1][j]==1:
                    voisins+=1
                if plateau[i][j-1]==1:
                    voisins+=1
                if plateau[i+1][j-1]==1:
                    voisins+=1
                if plateau[i+1][j]==1:
                    voisins+=1
            elif i<l-1 and i>0 and j<l-1 and j>0:
                    if plateau[i-1][j-1]==1:
                        voisins+=1
                    if plateau[i-1][j]==1:
                        voisins+=1
                    if plateau[i-1][j+1]==1:
                        voisins+=1
                    if plateau[i][j-1]==1:
                        voisins+=1
                    if plateau[i][j+1]==1:
                        voisins+=1
                    if plateau[i+1][j-1]==1:
                        voisins+=1
                    if plateau[i+1][j]==1:
                        voisins+=1
                    if plateau[i+1][j+1]==1:
                        voisins+=1
            if voisins==3 and plateau[i][j]==0:
                born.append((i,j))
            if voisins<2 or voisins>3 and plateau[i][j]==1:
                dead.append((i,j))
    return born,dead

def MAJplateau(plateau):
    born,dead=itération(plateau)
    for b in born:
        plateau[b[0]][b[1]]=1
    for d in dead:
        plateau[d[0]][d[1]]=0
    return plateau

def fonctionnement(tours,taille):
    plateau=créeplateau(taille)
    affiche(plateau)
    plateau=début(plateau)
    for t in range(tours):
        plateau=MAJplateau(plateau)
        if t == 0:
            line=plt.imshow(plateau,'Greys',vmin=0,vmax=1)
        else:
            line.set_data(plateau)
        plt.pause(0.01)
    plt.show()