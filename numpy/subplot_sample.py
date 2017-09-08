import matplotlib.pyplot as plt

ax = plt.subplot(2, 2, 1)
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.title('ax-2.2.1')

ax2 = plt.subplot(2, 2, 2)
ax2.plot([21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
plt.title('ax-2.2.2')


ax3 = plt.subplot(2, 2, 3)
ax3.plot([31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
plt.title('ax-2.2.3')

ax4 = plt.subplot(2, 2, 4)
ax4.plot([31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
plt.title('ax-2.2.4')


plt.show()
