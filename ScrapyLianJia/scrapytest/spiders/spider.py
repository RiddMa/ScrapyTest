import scrapy
from ScrapyLianJia.scrapytest.items import BuptItem
from ScrapyLianJia.scrapytest.items import LjItem
page = 3


class BUPTSpider(scrapy.Spider):
    name = "BUPT"
    allowed_domains = ["bupt.edu.cn/"]
    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]

    def parse(self, response, **kwargs):
        item = BuptItem()
        for each in response.xpath('//a[@target="_blank"]'):
            print(each.extract())
            print('*' * 30)
            item["school"] = each.xpath("text()").extract()
            item["link"] = each.xpath("@href").extract()
            if item["school"] and item["link"]:
                yield item


class LianJiaSpider(scrapy.Spider):
    name = "LJ"
    allowed_domains = ["bj.fang.lianjia.com"]
    start_urls = []
    if page >= 1:  # 根据待爬取页面数量，添加起始链接
        for i in range(1, page + 1):
            start_urls.append(f"https://bj.fang.lianjia.com/loupan/nhs1pg{i}")

    def parse(self, response, **kwargs):
        item = LjItem()

        for each in response.xpath("/html/body/div[4]/ul[2]/*"):  # 将每一条房源数据进行整理
            item['Name'] = each.xpath("div/div[1]/a/text()").extract()
            item['ResidenceType'] = each.xpath('div/div[1]/span[@class="resblock-type"]/text()').extract()
            item['IsOnSale'] = each.xpath('div/div[1]/span[@class="sale-status"]/text()').extract()
            item['LocationDistrict'] = each.xpath('div/div[2]/span[1]/text()').extract()
            item['LocationBlock'] = each.xpath('div/div[2]/span[2]/text()').extract()
            item['LocationAddr'] = each.xpath('div/div[2]/a/text()').extract()
            item['LDK'] = []
            for room in each.xpath('div/a/*'):  # 对LDK内容进行格式整理
                item['LDK'] += room.xpath('text()').extract()
                if item['LDK'][-1] == '/':
                    del item['LDK'][-1]
            item['AreaSize'] = each.xpath('div/div[3]/span/text()').extract()
            item['PricePerSqM'] = [f"均价{each.xpath('div/div[6]/div[1]/span[1]/text()').extract()[0]}元/平方米"]
            item['PricePerSuite'] = each.xpath('div/div[6]/div[2]/text()').extract()

            yield item  # yield传递数据给下一个
