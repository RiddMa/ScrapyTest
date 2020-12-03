import requests
from lxml import etree
import csv
import time
import json

bgg_url = 'https://www.boardgamegeek.com'
base_url = "https://www.boardgamegeek.com/browse/boardgame/page/"

rawheaders = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7
referer: https://www.boardgamegeek.com/
sec-fetch-dest: document
sec-fetch-site: same-origin
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"""

headers = dict([[h.partition(':')[0], h.partition(':')[2][1:]] for h in rawheaders.split('\n')])


def spider(wr):
    page2get = 1225
    for i in range(114, 201):
        main_url = base_url + str(i)
        main_page = requests.get(main_url, headers=headers)
        main_page = etree.HTML(main_page.text)
        main_lz = main_page.xpath('//*[@id="row_"]')
        j = 0
        while j < len(main_lz):
            item = main_lz[j]
            try:
                sub_url = item.xpath('td[3]/div[2]/a/@href')[0]
                bg_id = sub_url.split('/')[-2]

                x = item.xpath('td[2]/a/img/@src')[0]
                url = "G:/Courseware/Python/ScrapyTest/BGG/image_xx/{}.{}".format(str(bg_id), x[-3:])
                with open(url, 'wb') as photo:
                    info = requests.get(x, headers=headers)
                    photo.write(info.content)
            except:
                print("An exception occurred")
                time.sleep(2.4)
                j -= 1
                print("再来一次")
            j += 1
            print(bg_id)
        print(i, "------------------------done")


if __name__ == '__main__':
    spider(None)



