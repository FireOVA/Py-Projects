# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:57:43 2022

@author: kaieu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from numpy import linalg

def compression(k):
    U1 = U[:,:k]
    S1 = S[:k,:k]
    Vt1 = Vt[:k,:]
    return U1 @ S1 @ Vt1

img=misc.face()
imgc=img.copy()
imgg = imgc @ [0.2126,0.7152,0.0722]

U, s, Vt = linalg.svd(imgg)
S = np.zeros((768,1024))
for i in range(len(s)):
    S[i,i]=s[i]
    
#img6 = U[:,:100] @ S[:100,:100] @ Vt[:100,:]
#plt.imshow(img6,cmap="gray")
#plt.imshow(compression(120),cmap="gray")

fig, axes = plt.subplots(2,4)
axes[0,0].imshow(imgg,cmap="gray")
svalue = [5,20,50,80,110,150,200]
idx = 0
for i in range(2):
    for j in range(4):
        if i ==0 and j ==0: 
            continue
        axes[i,j].imshow(compression(svalue[idx]),cmap="gray")
        idx+=1