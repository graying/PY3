import matplotlib.pyplot as plt

fig = plt.figure()

# Don't understand what's the different between add_subplot() and add_axes()
ax1 = fig.add_subplot(2, 2, 1)
ax3 = plt.subplot(2, 2, 2)

ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.2])

ax1.plot([1, 2, 3, 4, 5], color='g', lw=3)
ax1.set_xlabel("ax1_x")
ax1.set_title("ax1")
ax1.set_ylabel("ax1_y")

ax2.hist([1, 2, 3, 2, 1], color='grey')
ax3.scatter([1, 2, 3, 4, 5], [5, 5, 5, 5, 5],
            color='r')

plt.show()
