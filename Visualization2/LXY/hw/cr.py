import requests
from lxml import etree
import re
import csv


# raw = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7
# Cache-Control: max-age=0
# Cookie: UM_distinctid=17660d7df1a459-058aa59737d7fd-c791039-146d15-17660d7df1b6cd; CNZZDATA1275796416=1127384109-1607941733-%7C1607941733; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1607942529; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1607942861
# Host: lishi.tianqi.com
# If-Modified-Since: Sat, 12 Dec 2020 09:56:30 GMT
# Proxy-Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"""

# def func(rawheaders: str):
#     headers = dict([[h.partition(':')[0], h.partition(':')[2][1:]]
#                     for h in rawheaders.split('\n')])
#     return headers

# s = 'hefei,wuhu,benbu,huainan,maanshan,huaibei,tongling,anqing,huangshan,tuzhou,fuyang,suzhou,liuan,bozhou,chizhou,xuancheng'
# lz = s.split(',')

# url = 'http://lishi.tianqi.com/{loc}/202011.html'

# pp = []

# for i in lz:
#     uu = url.format(loc=i)
#     print(uu)
#     x = requests.get(uu,headers=func(raw))
#     # print(x.text)
#     h = etree.HTML(x.text)
#     ss = h.xpath('/html/head/script/text()')[0]
#     print(ss)
#     ll = ss.split('\r\n')
#     for j in range(len(ll)):
#         ll[j] = ll[j].strip()
#     high = eval(ll[1].split()[3][:-1])
#     low = eval(ll[2].split()[3][:-1])
#     gg = []
#     for j in range(10):
#         if high[j] == '-' or low[j] == '-':
#             gg.append(10)
#             continue
#         gg.append((int(high[j])+int(low[j]))/2)
#     print('f')
#     pp.append(gg)
pp = [[16.0, 15.0, 13.0, 14.0, 15.0, 15.5, 14.5, 14.0, 13.5, 12.5], [16.5, 16.0, 13.0, 14.5, 16.5, 17.0, 16.5, 14.5, 14.0, 14.0], [10.5, 10, 10, 8.5, 9.5, 11.0, 10.5, 8.0, 9.0, 10.0], [15.5, 14.5, 13.0, 14.0, 14.5, 17.0, 17.0, 15.0, 14.0, 14.5], [15.5, 16.5, 13.0, 14.5, 17.0, 17.5, 17.0, 15.0, 15.0, 14.5], [15.0, 12.0, 11.5, 13.5, 13.0, 15.5, 14.0, 12.0, 12.0, 13.0], [16.0, 16.0, 14.0, 15.0, 18.0, 17.0, 17.0, 14.5, 14.5, 14.0], [16.0, 16.0, 14.5, 15.0, 17.0, 17.5, 17.0, 15.0, 14.5, 14.0], [16.0, 15.5, 13.5, 15.0, 18.5, 19.0, 17.5, 15.5, 13.5, 13.5], [10.5, 10, 10, 8.5, 9.5, 11.0, 10.5, 8.0, 9.0, 10.0], [18.5, 15.0, 13.5, 15.0, 18.0, 20.5, 18.0, 15.5, 14.5, 14.0], [17.5, 17.5, 16.5, 16.5, 14.0, 14.0, 14.5, 14.5, 17.5, 17.5], [10.5, 10, 10, 8.5, 9.5, 11.0, 10.5, 8.0, 9.0, 10.0], [2.5, 4.0, 4.5, 4.0, 1.5, 1.0, 2.5, 3.5, 2.5, 2.0], [16.5, 16.5, 13.5, 15.5, 17.5, 17.0, 16.0, 14.5, 14.0, 14.0], [16.5, 16.0, 12.5, 15.0, 17.0, 16.0, 16.0, 13.5, 13.5, 13.5]]
with open(r'D:\python_repo\homework\11\hw\da.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    lines = []
    for i in range(10):
        line = []
        for j in range(16):
            x = pp[j][i]
            line.append(x)
        lines.append(line)
    wr.writerows(lines)
    print(pp)
