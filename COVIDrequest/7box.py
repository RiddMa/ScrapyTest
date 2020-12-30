import os

import matplotlib.pyplot as plt
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


def main():
    dfs = loadfile()
    df = dfs['20201216-090001']
    df = df[df['#'].notna()]
    f = df.boxplot(column=['Total Cases'], meanline=True, showmeans=True, vert=True, return_type='dict')
    plt.text(1.1, df['Total Cases'].mean(), "%.2f" % df['Total Cases'].mean())
    for mean in f['means']:
        mean.set(color='r', linewidth=1)
    plt.title('Total Cases in box figure')
    plt.show()


if __name__ == '__main__':
    main()
