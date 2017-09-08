import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg. imread('stinkbug.png')

plt.figure(1)
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
plt.colorbar()

plt.figure(2)
plt.imshow(lum_img, cmap='hot')
x = np.arange(0,200)
plt.plot(x)
plt.show()
