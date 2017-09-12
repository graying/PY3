import matplotlib.pyplot as plt

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
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')

plt.show()
