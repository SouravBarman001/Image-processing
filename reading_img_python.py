#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:34:10 2024

@author: souravbarman
"""

"""
Reading images into python
pip install scikit-image
pip install opencv-python
"""

"""
import numpy as np
img3 = img.astype(np.float) doesnot make range between 0 to 255
"""

from skimage import io, img_as_float,img_as_ubyte

img = io.imread("/Users/souravbarman/Documents/8th Semester/DIgital Image processing/Image processing code/images/Osteosarcoma_01.tif")
print(img.shape) # width,height , channel

img1 = img_as_float(img)

img2 = img_as_ubyte(img1)


import cv2
#BGR instead of RGB
image_cv2 = cv2.imread("/Users/souravbarman/Documents/8th Semester/DIgital Image processing/Image processing code/images/Osteosarcoma_01.tif",1)

img_opencv = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

print(img_opencv)

from matplotlib import pyplot as plt

plt.imshow(img_opencv)