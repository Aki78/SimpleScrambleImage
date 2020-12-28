import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from PIL import Image

img = mpimg.imread('12345.jpg').astype(np.uint8)
img2 = img

for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    for k in range(img.shape[2]):
      myRandInt = img[i][j][k]+randint(-100,100)
      if(myRandInt < 255 and myRandInt > 0):
        img2[i][j][k] =  myRandInt

im = Image.fromarray(img2)
im.save("out.jpg")
