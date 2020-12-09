import numpy as np
import matplotlib.pyplot as plt
import csv


def main():
    dic = {1: [], 2: [], 3: []}
    with open("datac.csv", 'r', encoding='utf-8') as csvf:
        reader = csv.reader(csvf)
        for row in reader:
            key = int(row[0])
            id = int(row[1])
            rank = int(row[2])
            dic[key].append((id, rank))
        for key in dic:
            dic[key].sort(key=lambda xx: xx[0])
        print(dic)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    ax.set_title("排名")

    rank1 = [xx[1] for xx in dic[1]]
    rank2 = [xx[1] for xx in dic[2]]
    rank3 = [xx[1] for xx in dic[3]]

    # ax.set_xlim(1, 10)
    x = np.arange(1, 11)
    ax.set_xticks(np.arange(1, 11))

    plt.bar(x - 0.3, rank1, 0.3, color='r')
    plt.bar(x, rank2, 0.3, color='b')
    plt.bar(x + 0.3, rank3, 0.3, color='g')

    for a, b in zip(x, rank1):  # 在直方图上显示数字
        plt.text(a - 0.3, b, '%d' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(x, rank2):  # 在直方图上显示数字
        plt.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(x, rank3):  # 在直方图上显示数字
        plt.text(a + 0.3, b, '%d' % b, ha='center', va='bottom', fontsize=10)

    plt.legend(["第1学期", "第2学期", "第3学期"], loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()
