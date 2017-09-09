import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
line_up = plt.plot([1,2,3], label='Line up', color="black")
line_dw = plt.plot([3,2,1], label='line dw')
# plt.legend() can bring the legend on
# plt.legend()

# customize the legends
red_patch = mpatches.Patch(color='red', label='The red data')
grn_patch = mpatches.Patch(color='green', label='The grn data')

plt.legend(handles=[red_patch, grn_patch])


plt.grid()
plt.show()