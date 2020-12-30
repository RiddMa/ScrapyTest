import matplotlib.pyplot as plt
import numpy as np
import os
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


def func():
    dfs = loadfile()
    datelz, totlz = worldtrend(dfs)
    print(datelz)
    print(totlz)
    datelz = np.arange(15) + 1
    totlz = totlz[:-1]

    e = [0] * 15

    model = np.polyfit(datelz, totlz, 1)
    plt.plot(datelz, totlz, marker='o', linestyle='-',
             linewidth=4, markersize=10, label='Original')
    add = 0
    for i in range(10, 15):
        oldval = totlz[i]
        totlz[i] = model[0] * (i) + model[1] + add
        e[i] = totlz[i] - oldval
    plt.plot(datelz, totlz, marker='x', linestyle='--',
             linewidth=1, markersize=10, color='r', label='Predict')

    for i in range(10, 15):
        plt.text(datelz[i], totlz[i] - 100, "%d" % e[i])

    plt.title('Trend to Predict')
    plt.grid()
    plt.legend()
    plt.show()


func()
