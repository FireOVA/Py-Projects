# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:53:37 2022

@author: kaieu
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from sklearn.datasets import fetch_olivetti_faces
img_data=fetch_olivetti_faces()

imgs = img_data.data
U,s,Vt=linalg.svd(imgs)
len(s)
S = np.zeros((400,4096))
for i in range(len(s)):
    S[i,i]=s[i]
    
n = [1,5,10,15,20,25,30,35,40,50,60,80,120,180]
idx=0
fig,axes=plt.subplots(3,5)

axes[0,0].imshow(imgs[50].reshape(64,64),cmap='gray')
for i in range(3):
    for j in range(5):
        if i==0 and j==0:
            continue
        face=U[:,:n[idx]]@S[:n[idx],:n[idx]]@Vt[:n[idx],:]
        face=face[50].reshape(64,64)
        axes[i,j].imshow(face,cmap='gray')
        idx+=1