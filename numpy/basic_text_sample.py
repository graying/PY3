import matplotlib.pyplot as plt
import numpy as np

# text() - add text at an arbitrary location to the Axes; matplotlib.axes.Axes.text() in the API.
# xlabel() - add a label to the x-axis; matplotlib.axes.Axes.set_xlabel() in the API.
# ylabel() - add a label to the y-axis; matplotlib.axes.Axes.set_ylabel() in the API.
# title() - add a title to the Axes; matplotlib.axes.Axes.set_title() in the API.
# figtext() - add text at an arbitrary location to the Figure; matplotlib.figure.Figure.text() in the API.
# suptitle() - add a title to the Figure; matplotlib.figure.Figure.suptitle() in the API.
# annotate() - add an annotation, with
# optional arrow, to the Axes ; matplotlib.axes.Axes.annotate() in the API.
# All of these functions create and return a matplotlib.text.Text() instance, which can be configured with a variety of font and other properties. The example below shows all of these commands in action.

fig = plt.figure()
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
ax.set_xlim(1,100)
ax.set_ylim(1,100)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

text1 = ax.text(30, 80, 'boxed italics text in data coords',
                style='italic',
                bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10}
                )

ax.text(50, 50, 'text at 50,50')

ax.text(50, 50, "text on 50,50", fontsize=20)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax1.plot(t, s, lw=2)
ax1.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
ax1.set_ylim(-2, 2)

plt.show()
