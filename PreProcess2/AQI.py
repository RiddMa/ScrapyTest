import numpy as np
import pandas as pd


def toDf(fileName, lz):
    df = pd.read_csv(fileName, encoding='utf-8')
    df.dropna(axis=0, how='all', subset=lz, inplace=True)
    df['sum'] = df[lz].sum(axis=1)
    df['count'] = df[lz].count(axis=1)
    df['ave'] = round(df['sum'] / df['count'], 2)
    df = df[df['year'] == 2015]
    bin = [0, 50, 100, 150, 200, 300, 1000]
    df0 = df.groupby(["year", "month", "day"])
    result = pd.cut(df0['ave'].mean(), bin)
    print(fileName)
    print(pd.value_counts(result))


def main():
    lzBeijing = ['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']
    lzChengdu = ['PM_Caotangsi', 'PM_Shahepu', 'PM_US Post']
    lzGuangzhou = "PM_City Station,PM_5th Middle School,PM_US Post".split(',')
    lzShanghai = "PM_Jingan,PM_US Post,PM_Xuhui".split(',')
    lzShengyang = "PM_Taiyuanjie,PM_US Post,PM_Xiaoheyan".split(',')
    dic = {
        'BeijingPM20100101_20151231.csv': lzBeijing,
        'ChengduPM20100101_20151231.csv': lzChengdu,
        'GuangzhouPM20100101_20151231.csv': lzGuangzhou,
        'ShanghaiPM20100101_20151231.csv': lzShanghai,
        'ShenyangPM20100101_20151231.csv': lzShengyang
    }
    for file in dic:
        toDf(file, dic[file])


if __name__ == '__main__':
    main()
