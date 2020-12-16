import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 设置画布
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置x、y、z的关系
x = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
y = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5])
z = np.array([1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 25, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9])
bottom = np.zeros_like(z)

# 绘制3D直方图
width = depth = 0.5
ax.bar3d(x, y, bottom, width, depth, z, shade=True)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([1, 2, 3, 4, 5])

# 显示图形
plt.show()