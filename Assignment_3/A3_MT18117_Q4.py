#!/usr/bin/env python
# coding: utf-8

# In[61]:


# References
# - used plotImage method from my assignment-2
# - used fft2,ifft function from numpy


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import copy


# In[52]:


def plotImage(image):
    plt.imshow(image,cmap='gray',vmin=0,vmax=255)
    plt.show()
    
def plotImgFloat(image):
    image=np.asarray(image, dtype=int)
    plotImage(image)


# ### Image

# In[22]:


img = cv2.imread('Chandrayaan2 - Q3a-inputimage.png',0)
plotImage(img)
img.shape


# #### Cropping image

# In[38]:


crop_img = img[0:512, 0:512]
plotImage(crop_img)
crop_img.shape


# #### Padding image

# In[39]:


last_column = crop_img.shape[0]
last_row = crop_img.shape[1]
crop_img=np.insert(crop_img, last_column, 0, axis=1)# adding front column
crop_img=np.insert(crop_img, last_column, 0, axis=1) # adding last column
crop_img=np.insert(crop_img, last_row, 0, axis=0)# adding top row
crop_img=np.insert(crop_img, last_row, 0, axis=0)# adding last row

print(crop_img.shape)
plotImage(crop_img)


# ### Box Filter

# In[43]:


box_filter=(1/9)*np.ones((3,3))
print(box_filter)


# #### padding box filter

# In[44]:


last_column = box_filter.shape[0]
last_row = box_filter.shape[1]
for i in range(0,511):
    box_filter=np.insert(box_filter, last_column, 0, axis=1)# adding front column
for i in range(0,511):
    box_filter=np.insert(box_filter, last_row, 0, axis=0)# adding top row

print(box_filter.shape)
plotImage(box_filter)
print(box_filter)


# ### Calculating FFT

# In[53]:


fft_crop_img = np.fft.fft2(crop_img)
fft_box_filter = np.fft.fft2(box_filter)

plotImgFloat(fft_crop_img)
plotImgFloat(fft_box_filter)


# In[55]:


h_prod= fft_crop_img * fft_box_filter #hardman product = element-wise product ==np.multiply(dft_f,dft_w)
plotImgFloat(h_prod)
print(h_prod)


# In[56]:


mask_img = fft_crop_img - h_prod
plotImgFloat(mask_img)
print(mask_img)


# #### adding mask to fft2 of zero padded crop_img

# In[57]:


add = fft_crop_img + mask_img
plotImgFloat(add)


# In[58]:


ifft_crop_img = np.fft.ifft2(add)
real_part = np.real(ifft_crop_img)
plotImgFloat(real_part)


# In[ ]:




