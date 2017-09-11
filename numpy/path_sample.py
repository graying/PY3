import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path

verts = [(0, 0),
         (0, 1),
         (1, 1),
         (1, 0),
         (0, 0), ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY, ]

path = Path(verts, codes)

fig = plt.figure()
ax = fig.add_subplot(221)
patch = patches.PathPatch(path)
ax.add_patch(patch)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax1 = fig.add_subplot(222)
pos = list()
codes1 = list()
codes1.append(Path.MOVETO)
# pos = [(0,0),(1,1),(1,2),(2,3),(3,3),(1,1),(3,2),(2,1)]
# codes1=(Path.MOVETO,
#         Path.LINETO,
#         Path.LINETO,
#         Path.LINETO,
#         Path.LINETO,
#         Path.LINETO,
#         Path.LINETO,
#         Path.CLOSEPOLY
#         )
for i in range(10):
    x = np.random.randint(1, 100)
    y = np.random.randint(1, 100)
    pos.append((x, y))
    print('i=', i, 'x=', x, 'y=', y, codes1[i])

    if i == 9:
        codes1.append(Path.CLOSEPOLY)
        pos.append((0, 0))
        break
    codes1.append(Path.LINETO)
print(pos)
print(codes1)
path1 = Path(pos, codes1)
patch1 = patches.PathPatch(path1, facecolor='cyan', edgecolor='r', lw=1)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.add_patch(patch1)

ax3 = fig.add_subplot(223)

verts3 = [
    (0, 0),
    (0.2, 1),
    (1, 0.8),
    (0.8, 0)
]

codes3 = [Path.MOVETO,
          Path.CURVE4,
          Path.CURVE4,
          Path.CURVE4,
          ]
path3 = Path(verts3, codes3)
patch3 = patches.PathPatch(path3, facecolor='none', lw=2)
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.add_patch(patch3)
plt.show()
