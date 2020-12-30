from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import random
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
import csv 


cities = '合肥市、芜湖市、蚌埠市、淮南市、马鞍山市、淮北市、铜陵市、安庆市、黄山市、滁州市、阜阳市、宿州市、六安市、亳州市、池州市、宣城市'
Anhui_cities = cities.split('、')
tmp = []
with open(r'da.csv','r') as f:
    reader = csv.reader(f)
    for line in reader:
        tmp.append(line)


def geo_guangdong(title, day) -> Geo:
    c = (
        Geo()
        .add_schema(maptype="安徽")
        .add(
            title,
            [list(z) for z in zip(Anhui_cities,tmp[day])],
            type_=ChartType.HEATMAP,
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=18),  # is_piecewise=True),
            title_opts=opts.TitleOpts(title="安徽省11月份各地市温度变化情况"),
        )
    )
    return c


for i in range(10):
    str_date = "11月" + str(i+1) + "日"
    make_snapshot(snapshot, geo_guangdong(str_date,i).render(),
                  str(i+1)+".png", pixel_ratio=1)
    print(str_date)
