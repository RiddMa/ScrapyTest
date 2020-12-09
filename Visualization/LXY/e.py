import matplotlib.pyplot as plt
import csv
import numpy as np


def main():
    fig, ax = plt.subplots()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    dic = {}
    with open('beijing.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            year = int(row[0])
            month = int(row[1])
            rank = round(float(row[2]), 2)
            if year not in dic:
                dic[year] = [rank]
            else:
                dic[year].append(rank)
    month_lz = np.arange(1, 13)
    for year in range(2010, 2016):
        plt.plot(month_lz, dic[year], linewidth=2, linestyle="-", label=str(year))
    ax.set_title('北京空气质量数据')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    main()
