import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


def loadfile(path=r'G:/Courseware/Python/ScrapyTest/COVIDrequest/data15') -> dict:
    dataframes = {}
    filelz = os.listdir(path)
    for filename in filelz:
        df = pd.read_csv(path + '/' + filename, thousands=',')
        df = df.sort_values(by='Country, Other', ascending=False)
        df = df.reset_index()
        dataframes[filename.partition('.')[0]] = df
    return dataframes


def data():
    dfs = loadfile()
    df = dfs['20201216-090001']
    df = df[df['#'].notna()]

    x, y = df['Country, Other'].values, df['Total Cases'].values
    lz = []

    for i, j in zip(x, y):
        if i == 'USA':
            i = 'United States'
        lz.append([i, j.item()])

    lz.sort(key=lambda x: -x[1])
    return lz


def map_visualmap() -> Map:
    c = (
        Map()
            .add("Coronavirus Heatmap", [z for z in data()], "world")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Cases"),
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=2000000))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


make_snapshot(snapshot, map_visualmap().render(), "map1.png")
map_visualmap().render("map" + ".html")
