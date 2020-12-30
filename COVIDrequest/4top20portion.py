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


def casePPL(datadict: dict):
    key = '20201216-090001'
    df = datadict[key]
    df = df.sort_values(by='1 Case every X ppl', ascending=True)
    df = df.head(10)

    return df['Country, Other'].values, df['1 Case every X ppl'].values


def main():
    dfs = loadfile()
    fig, ax = plt.subplots()
    loclz, datalz = casePPL(dfs)
    datalz = np.array(datalz)
    datalz = 100 / datalz
    ax.set_title('Top 10 Case/Population')
    x = np.arange(10) + 1
    plt.bar(x, datalz)
    plt.xticks(x, loclz, rotation=40, fontsize='medium')
    ax.set_xlabel('Country/Region')
    ax.set_ylabel('Cases')
    for a, b in zip(x, datalz):
        plt.text(a, b, '%.2f' % b + '%', ha='center', va='bottom', fontsize=10)
    plt.show()


if __name__ == '__main__':
    main()
