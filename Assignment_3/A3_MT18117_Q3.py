#!/usr/bin/env python
# coding: utf-8

# In[139]:


# References
# - used plotImage method from my assignment-2
# - used fft2,ifft function from numpy


# In[127]:


import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import copy


# In[137]:


def plotImage(image):
    plt.imshow(image,cmap='gray',vmin=-10,vmax=255)
    plt.show()
    
def plotImgFloat(image):
    image=np.asarray(image, dtype=int)
    plotImage(image)


# In[129]:


f=[[1,3,4],[2,5,3],[6,8,9]]
f=np.asarray(f)

w=[[-1,-2,-3],[-4,0,-1],[-6,-5,-1]]
w = np.asarray(w)

plotImage(f)
plotImage(w)


# ### padding to f

# In[130]:


f=np.insert(f, f.shape[1], 0, axis=1)# columns padding
f=np.insert(f, f.shape[1], 0, axis=1)
f=np.insert(f, f.shape[0], 0, axis=0)#row padding
f=np.insert(f, f.shape[0], 0, axis=0)

print(f.shape)
plotImage(f)
print(f)


# ### w: padding and shifting

# In[131]:


w=np.insert(w, w.shape[1], 0, axis=1)#Collumn padding
w=np.insert(w, w.shape[1], 0, axis=1)
w=np.insert(w, w.shape[0], 0, axis=0)#row padding
w=np.insert(w, w.shape[0], 0, axis=0)

print(w.shape)
plotImage(w)
print(w)


# In[132]:


w=np.roll(w,-1,axis=1)
print(w)
w=np.roll(w,-1,axis=0)
print(w)
plotImage(w)


# ### calculating DFT

# In[138]:


dft_f=np.fft.fft2(f)
dft_w=np.fft.fft2(w)

plotImgFloat(dft_f)
plotImgFloat(dft_w)


# ### calculating Hardaman Product(element wise product)

# In[134]:


h_prod= dft_f * dft_w #hardman product = element-wise product ==np.multiply(dft_f,dft_w)
print(h_prod)


# In[135]:


dft_2d = np.fft.ifft2(h_prod).round()
real_part = np.real(dft_2d)
real_part


# In[136]:


plotImage(real_part)


# In[ ]:




