from pyecharts import options as opts
from pyecharts.charts import Map
import random
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
import csv


def data():
    with open(r"D:\python_repo\homework\11\sample\中国大学数量.csv",'r') as f:
            reader = csv.reader(f)
            head = next(reader)
            next(reader)
            lz = []
            for line in reader:
                value = float(line[1][:-1])
                lz.append([line[0],value])
                print([line[0],value])
            return lz


def map_visualmap() -> Map:
    c = (
        Map()
        .add("各省2017年考生数量", [z for z in data()], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(min_=0,max_=100))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c

make_snapshot(snapshot, map_visualmap().render(), "map1.png")

for i in range(5):
    map_visualmap().render("map"+str(i)+".html")

print("done")