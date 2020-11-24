import scrapy

from PreProcessLianJia.PreProcLianJia.items import PreProcessLianJiaItem

# from PreProcessLianJia.begin import writer

page = 19


# datalz = []


class PreProcessLianJiaSpider(scrapy.Spider):
    name = "PPLianJia"
    allowed_domains = ["bj.fang.lianjia.com"]
    start_urls = []
    if page >= 1:  # 根据待爬取页面数量，添加起始链接
        for i in range(1, page + 1):
            start_urls.append(f"https://bj.fang.lianjia.com/loupan/pg{i}")

    def parse(self, response, **kwargs):
        item = PreProcessLianJiaItem()

        # /html/body/div[4]/ul[2]/li[1]/div/div[1]/a
        for each in response.xpath("/html/body/div[4]/ul[2]/*"):  # 将每一条房源数据进行整理
            item['Name'] = each.xpath("div/div[1]/a/text()").extract()[0]
            # item['ResidenceType'] = each.xpath('div/div[1]/span[@class="resblock-type"]/text()').extract()
            # item['IsOnSale'] = each.xpath('div/div[1]/span[@class="sale-status"]/text()').extract()
            item['LocationDistrict'] = each.xpath('div/div[2]/span[1]/text()').extract()[0]
            item['LocationBlock'] = each.xpath('div/div[2]/span[2]/text()').extract()[0]
            item['LocationAddr'] = each.xpath('div/div[2]/a/text()').extract()[0]
            try:
                item['LDK'] = each.xpath('div/a/span[1]/text()').extract()[0]
            except Exception as e:
                item['LDK'] = ''
            """
            item['LDK'] = []
            for room in each.xpath('div/a/*'):  # 对LDK内容进行格式整理
                item['LDK'] += room.xpath('text()').extract()
                if item['LDK'][-1] == '/':
                    del item['LDK'][-1]
            """
            item['AreaSize'] = each.xpath('div/div[3]/span/text()').extract()[0]
            item['AreaSize'] = int(item['AreaSize'][3:-1].split('-')[0])
            if '均价' in each.xpath('div/div[6]/div[1]/span[2]/text()').extract()[0]:
                item['PricePerSqM'] = int(each.xpath('div/div[6]/div[1]/span[1]/text()').extract()[0])
                item['PricePerSuite'] = item['AreaSize'] * item['PricePerSqM'] / 10000
            else:
                item['PricePerSuite'] = float(each.xpath('div/div[6]/div[1]/span[1]/text()').extract()[0])
                item['PricePerSqM'] = int(item['PricePerSuite'] * 10000 / item['AreaSize'])
            yield item  # yield传递数据给下一个
