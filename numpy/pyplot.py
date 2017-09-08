# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)
y1 = list()
y2 = list()
y3 = list()
for X in x:
    y1.append(X)
    y2.append(X * X)
    y3.append(X * X * X)

# choose figure 1 as current figure, it's current by default, so this line can be ignored
plt.figure(1)

# sub
plt.subplot(211)    # why the number start from 211?
plt.plot(x, y1)
plt.subplot(212)
plt.plot(x, y2, color='red')

# figure 2
plt.figure(2)
# plt.subplot(213)
plt.plot(x, y3, color='orange')
plt.show()
