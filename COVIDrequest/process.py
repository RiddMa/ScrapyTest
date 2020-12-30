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


def worldtrend(datadict: dict):
    datelz = []
    totlist = []
    for date in datadict:
        df = datadict[date]
        worldtot = df[df['Country, Other'] == 'World']['Total Cases'].values[0]

        totlist.append(worldtot)
        datelz.append(date[-4:])
    return datelz, totlist


def main():
    dfs = loadfile()
    fig, ax = plt.subplots()
    datelz, totlist = worldtrend(dfs)
    ax.set_title('World Trend')
    x = np.arange(16) + 1
    print(totlist)
    plt.plot(x, totlist, linewidth=2, linestyle="-", marker='o')
    plt.xticks(x, datelz, rotation=30, fontsize='small')
    for a, b in zip(x, totlist):
        plt.text(a, b + 5, '%d' % b, ha='center', va='bottom', fontsize=12)
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
