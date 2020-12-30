import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def loadfile(path=r'G:/Courseware/Python/ScrapyTest/COVIDrequest/data15') -> dict:
    dataframes = {}
    filelz = os.listdir(path)
    for filename in filelz:
        df = pd.read_csv(path + '/' + filename, thousands=',')
        df = df.sort_values(by='Country, Other', ascending=False)
        df = df.reset_index()
        dataframes[filename.partition('.')[0]] = df
    return dataframes


def getdata(datadict: dict):
    head = '20201201-090001'
    tail = '20201216-090001'
    df = datadict[head]
    df = df[df['#'].notna()]
    df = df.sort_values(by='Country, Other', ascending=False)
    dfhead = df[['Country, Other', 'Total Cases']]

    df = datadict[tail]
    df = df[df['#'].notna()]
    df = df.sort_values(by='Country, Other', ascending=False)
    dftail = df[['Country, Other', 'Total Cases']]

    dftail['Increment'] = dftail['Total Cases'] - dfhead['Total Cases']

    df = dftail[['Country, Other', 'Increment']]
    df = df.sort_values(by='Increment', ascending=False)
    df = df.head(10)

    ret_dict = {}
    # 遍历top10的国家
    for Country in df['Country, Other'].values:
        addlz = []
        lz = []
        for key in datadict:
            df = datadict[key]
            df = df[df['Country, Other'] == Country]
            lz.append(df['Total Cases'].values[0])
            # addlz.append(df['New Cases'].values[0])
        for i in range(1, len(lz)):
            addlz.append(lz[i] - lz[i - 1])
        ret_dict[Country] = addlz

    print(ret_dict)
    return ret_dict


def main():
    dfs = loadfile()
    fig, ax = plt.subplots(nrows=5, ncols=2)
    dic = getdata(dfs)
    datelz = np.arange(15) + 1
    keylz = dic.keys()
    for i, key in zip(range(0, 10), keylz):
        r = i // 2
        c = i % 2
        ax[r][c].set_xlabel('Date', fontsize='medium')
        ax[r][c].grid()
        ax[r][c].plot(datelz, dic[key], linewidth=1, linestyle="-", label=key)
        ax[r][c].legend(loc='best')
    plt.show()


main()
