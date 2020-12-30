import csv
import os

import pandas as pd
import requests
from lxml import etree


def spider():
    url = "https://www.worldometers.info/coronavirus/#nav-yesterday"
    with open('covid.html', 'w', encoding='utf-8') as f:
        x = requests.get(url)
        f.write(x.text)


def syntax(filename: str):
    df = pd.read_csv(filename, encoding='utf-8', dtype=str)
    df = df.replace("['']", "")  # 格式化
    print(df.describe())
    print(df.info)
    print(df.isnull().sum)
    df.to_csv(r'/data/' + filename[:-4] + '.csv', encoding='utf-8', index=None)


def transHTML(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return etree.HTML(''.join(lines))


def parser(html):
    # Yesterday data
    root = html.xpath('//div[@id="nav-yesterday"]')[0]

    header = []
    th = root.xpath('div/table/thead/tr/th')  # 处理表格头部
    for item in th:
        text = item.xpath('text()|*/text()')
        header.append(''.join(text))

    body = []
    tr = root.xpath('div/table/tbody[1]/tr')
    for item in tr:
        td = item.xpath('td')
        lz = []
        for i in td:
            data = i.xpath('*/text()|text()')
            if len(data) < 1:
                lz.append([''])
            else:
                data_row = []
                for i in data:
                    data_row.append(i.strip())
                lz.append(''.join(data_row))
        body.append(lz)
    return header, body


def main():
    addr = '/data/'
    lz = os.listdir(addr)
    for file in lz:
        if file[-4:] != 'html':
            continue
        html = transHTML(addr + '/' + file)
        header, body = parser(html)
        filename = file
        with open(filename[1:-4] + 'csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(body)
        syntax(filename)


if __name__ == '__main__':
    main()
