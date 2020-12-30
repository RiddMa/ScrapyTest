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


def totalcase(datadict: dict):
    key = '20201216-090001'
    df = datadict[key]
    df = df[df['#'].notna()]
    df = df.sort_values(by='Total Cases', ascending=False)
    return df['Country, Other'].values, df['Total Cases'].values


def main():
    plt.figure(figsize=(6, 9))
    dfs = loadfile()
    loclz, datalz = totalcase(dfs)
    data = np.array(datalz)
    sum = data.sum()
    percent = data / sum

    pos = 15
    other = 0

    for x in datalz[pos:]:
        other += x

    explode = [0.01]*17
    x = datalz[:pos + 1]
    x = np.append(x, other)
    label = loclz[:pos + 1]
    label = np.append(label, 'others')
    patches = plt.pie(x, labels=label, explode=explode, autopct='%1.5f%%',
                      pctdistance=1, startangle=150)

    plt.title('Total Cases/Population', fontsize=30)
    plt.axis('equal')
    plt.legend(label, loc='best')
    plt.show()


if __name__ == '__main__':
    main()
