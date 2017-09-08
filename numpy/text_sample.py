import matplotlib.pyplot as plt
import numpy as np

<<<<<<< HEAD
np.random.seed(20170907)
=======
np.random.seed(101010)
>>>>>>> 482b67d38e0bb0c59057938a29f8523ed8410b02

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='r', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
<<<<<<< HEAD
plt.text(60, 0.025, r'$\mu=100,\ \sigma=15$') # the r'$ is TeX to show the mu and Sigma sign
plt.axis([40, 160, 0, 0.03])
=======
plt.text(60,0.025, r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
>>>>>>> 482b67d38e0bb0c59057938a29f8523ed8410b02
plt.grid(True)
plt.show()
