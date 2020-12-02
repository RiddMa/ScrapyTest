import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def count_elements(scores):  # 定义转换函数，统计每个数值对应多少个
    scorescount = {}  # 定义一个字典对象
    for i in scores:
        scorescount[int(i)] = scorescount.get(int(i), 0) + 1  # 累加每个分数值
        return scorescount


def count_elements1(scores):  # 定义转换函数，统计每个数值对应多少个
    scorescount = {}  # 定义一个字典对象
    for i in scores:
        scorescount[int(i * 100)] = scorescount.get(int(i * 100), 0) + 1  # 累加每个分数值的人数
    return scorescount


if __name__ == '__main__':
    fileNameStr = 'lianjia2.csv'
    df = pd.read_csv(fileNameStr, encoding='utf-8', usecols=[6, 7])
    df.dropna(axis=0, how="any", inplace=True)
    fig = plt.figure()
    ax1 = fig.add_subplot(231)
    # 子图1:原始图像
    x1 = df["unit_price"]
    y1 = df["total_price"]
    ax1.scatter(x1, y1, s=10)
    ax1.set_xlabel("unit_price")
    ax1.set_ylabel("total_price")
    ax1.set_title("Original")
    print(type(x1))
    # 子图2:(0,1)归一化，采用MinMaxScaler函数
    ax2 = fig.add_subplot(232)
    min = x1.min()
    max = x1.max()
    ave = x1.mean()
    std = x1.std()
    x2 = (x1 - min) / (max - min)
    scaler = MinMaxScaler()
    y_reshape = y1.values.reshape(-1, 1)
    y2 = scaler.fit_transform(y_reshape)
    ax2.scatter(x2, y2, s=10)
    ax2.set_title("MinMaxScaler")
    # 子图3:Z-score归一化，采用StandardScaler函数
    ax3 = fig.add_subplot(233)
    scaler_std = StandardScaler()
    x_reshape = x1.values.reshape(-1, 1)
    x3 = scaler_std.fit_transform(x_reshape)
    y_reshape = y1.values.reshape(-1, 1)
    y3 = scaler_std.fit_transform(y_reshape)
    ax3.scatter(x3, y3, s=10)
    ax3.set_title("StandardScaler")
    # 查看单个特征，在归一化之后的分布有何变化。
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)
    ax4.set_title("Original")
    ax5.set_title("MinMax")
    ax6.set_title("Standard")
    counted1 = count_elements(y1)
    counted2 = count_elements1(y2)
    counted3 = count_elements1(y3)
    ax4.bar(counted1.keys(), counted1.values(), 0.8, alpha=0.5, color='r')
    ax5.bar(counted2.keys(), counted2.values(), 0.8, alpha=0.5, color='r')
    ax6.bar(counted3.keys(), counted3.values(), 0.8, alpha=0.5, color='r')
    plt.show()
