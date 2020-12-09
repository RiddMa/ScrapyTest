import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():
    plt.style.use('bmh')  # 设置图像风格
    fig, ax = plt.subplots()
    ax.set_title("square numbers")
    ax.set_xlim(-10, 10)
    x = np.array(range(-10, 11))  # 创建一个numpy数组x
    y = x ** 2 + 1  # 创建一个numpy数组y，内容为x中数据的平方值
    plt.bar(x, y, color='r')  # bar的颜色改为红色
    for a, b in zip(x, y):  # 在直方图上显示数字
        plt.text(a, b/2, '%d' % b, ha='center', va='bottom', fontsize=10)
    plt.show()


if __name__ == '__main__':
    main()
