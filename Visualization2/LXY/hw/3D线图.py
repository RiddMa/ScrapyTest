import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 设置画布
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置x、y、z轴数据
x = np.array([0, -1, 1, 0, 1, 1, 0, 1, -1, 0, -1, -1])
y = np.array([0, -1, -1, 0, -1, 1, 0, 1, 1, 0, 1, -1])
z1 = np.array([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
z2 = -z1


# 使用plot画3D线图
plt.plot(x, y, z1, 'r', marker='o')
plt.plot(x, y, z2, 'b', marker='o')
ax.set_zticks([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
ax.set_xticks([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
ax.set_yticks([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])

# 显示线图
plt.show()