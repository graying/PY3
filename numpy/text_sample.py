import matplotlib.pyplot as plt
import numpy as np

np.random.seed(101010)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='r', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

# the r'$ is TeX to show the mu and Sigma sign
plt.text(60, 0.025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])

plt.grid(True)

# xy is the position you want to annotated, xytext is the text position
plt.annotate('the place', xy=(50, 0.01), xytext=(45, 0.02),
             arrowprops=dict(facecolor='black', shrink=0.5),
             )

plt.show()
