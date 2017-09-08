# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)
y_sin = np.sin(x)
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.axes().set_aspect('equal')
plt.title('y=sin(x)')
plt.plot(x, y_sin)
plt.show()
