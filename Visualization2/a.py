import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
BasePath = r'G:\Courseware\Python\ScrapyTest\Visualization2'  # csv文件的保存路径
iris = pd.read_csv(BasePath + '\\iris.csv')
print(iris)
colors = ['r', 'y', 'b']  # 定义三种散点的颜色
Species = iris.Species.unique()  # 对类别去重
print(Species)

namelz = ['Sepal.length', 'Sepal.width', 'Petal.Length', 'Petal.Width']

figure, ax = plt.subplots(nrows=4, ncols=4, figsize=(40, 40))
for i in range(0, 16):
    r = i // 4
    c = i % 4
    ax[r][c].set_title(namelz[3 - r] + ' vs ' + namelz[c], fontsize='small')
    ax[r][c].set_xlabel(namelz[3 - r], fontsize='small')
    ax[r][c].set_ylabel(namelz[c], fontsize='small')
    for j in range(3):
        ax[r][c].scatter(iris.loc[iris.Species == Species[j], namelz[3 - r]],
                         iris.loc[iris.Species == Species[j], namelz[c]], s=35, c='', edgecolors=colors[j],
                         label=Species[j])

if __name__ == '__main__':
    plt.show()
