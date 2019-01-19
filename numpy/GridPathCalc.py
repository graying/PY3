from mpl_toolkits import mplot3d # this import is neccesary for projection='3d"
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("5x5_result.txt", delimiter=' ')

arr_x = list(df.x)
arr_y = list(df.y)
arr_result = list(df.result)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(arr_x, arr_y, arr_result)
ax.scatter3D(arr_x, arr_y, arr_result, c=arr_result)
plt.show()
