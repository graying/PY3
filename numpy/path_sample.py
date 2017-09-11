import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.path import Path
import numpy as np

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
ax = fig.add_subplot(211)
patch = patches.PathPatch(path)
ax.add_patch(patch)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax1 = fig.add_subplot(212)
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
    x = np.random.randint(1,100)
    y = np.random.randint(1,100)
    pos.append((x,y))
    print('i=', i, 'x=', x, 'y=', y, codes1[i])

    if i == 9:
        codes1.append(Path.CLOSEPOLY)
        pos.append((0,0))
        break
    codes1.append(Path.LINETO)
print (pos)
print (codes1)
path1 = Path(pos, codes1)
patch1 = patches.PathPatch(path1)
ax1.set_xlim(0,100)
ax1.set_ylim(0,100)
ax1.add_patch(patch1)


plt.show()
