import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math

# 设置画布
fig = plt.figure(figsize=(40,40))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置x、y、z的值
x = np.random.randint(-100, 100, 5000)
y = np.random.randint(-100, 100, 5000)
z1 = x**2 + y**2 - 20000
z2 = -z1

# 绘制散点图
ax.scatter(x, y, z1, zdir='z', s=10, c='r', marker='o', depthshade=True,edgecolors='r')
ax.scatter(x, y, z2, zdir='z', s=10, c='b', marker='^', depthshade=True, edgecolors='b')

# 显示图画
plt.show()