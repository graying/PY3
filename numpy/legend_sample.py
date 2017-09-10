import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.xlim(-3, 3)
plt.ylim(0, 3)

line_up = plt.plot([1, 2, 3], label='Line up', color="black")
line_dw = plt.plot([3, 2, 1], label='line dw')
line_blue = plt.plot([2, 2, 2], '*', color='blue')
# plt.legend() can bring the legend on
# plt.legend()

# customize the legends
red_patch = mpatches.Patch(color='red', label='The red data')
grn_patch = mpatches.Patch(color='green', label='The grn data')
blue_line = mlines.Line2D([], [], color='blue', marker='*',
                          markersize=15, label='Blue Starts')

plt.legend(handles=[red_patch, grn_patch, blue_line])

plt.grid()
plt.show()
