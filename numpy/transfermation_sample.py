import matplotlib.pyplot as plt
import numpy as np

a = np.arange(1, 100)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# ax.transData.transform((10, 1)) transfer the data to display coordinate

print(ax.transData.transform((10, 1)))

print(ax.transData.transform((-10, 1)))

plt.show()
