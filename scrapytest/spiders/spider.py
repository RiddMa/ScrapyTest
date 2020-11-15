import scrapy
from scrapytest.items import MyItem


class MySpider(scrapy.Spider):
    name = "BUPT"
    allowed_domains = ["bupt.edu.cn/"]
    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]

    def parse(self, response, **kwargs):
        item = MyItem()
        for each in response.xpath('//a[@target="_blank"]'):
            print(each.extract())
            print('*' * 30)
            item["school"] = each.xpath("text()").extract()
            item["link"] = each.xpath("@href").extract()
            if item["school"] and item["link"]:
                yield item
