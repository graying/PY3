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
plt.subplot(211)  # why the number start from 121? because of it's 1x2 subplots, or it can be 2x2 with total 4 subplot
plt.plot(x, y1, color='g')
plt.subplot(212)
plt.plot(x, y2, color='red')

# figure 2
plt.figure(2)
# plt.subplot(213)
plt.plot(x, y3, color='orange')

# xy is the position you want to annotated, xytext is the text position
plt.annotate('the highest', xy=(10, 1000), xytext=(5, 1000),
             arrowprops=dict(facecolor='black', shrink=0.5),
             )
plt.show()
