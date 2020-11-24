# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

totalPrice = []
unitPrice = []


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


class PreProcessLianJiaPipeline:
    def process_item(self, item, spider):
        d_item = dict(item)
        totalPrice.append(d_item['PricePerSuite'])
        unitPrice.append(d_item['PricePerSqM'])
        d_item['PricePerSuite'] = format(d_item['PricePerSuite'], '.4f')

        with open("LJ.csv", 'a+') as f:
            csv_write = csv.writer(f)
            data_value = [d_item['Name'], d_item['LocationDistrict'], d_item['LocationBlock'], d_item['LocationAddr'],
                          d_item['LDK'], d_item['AreaSize'], d_item['PricePerSqM'], d_item['PricePerSuite']]
            csv_write.writerow(data_value)

        return item

    def open_spider(self, spider):
        with open("LJ.csv", 'a+') as f:
            csv_write = csv.writer(f)

    def close_spider(self, spider):
        totalPrice.sort()
        unitPrice.sort()
        totalmin = totalPrice[0]
        totalmax = totalPrice[-1]
        totalmid = totalPrice[int((int((len(totalPrice)) / 2) + int((len(totalPrice) + 1) / 2)) / 2)]
        unitmin = unitPrice[0]
        unitmax = unitPrice[-1]
        unitmid = unitPrice[int((int((len(unitPrice)) / 2) + int((len(unitPrice) + 1) / 2)) / 2)]
        print(totalmin, totalmid, totalmax, unitmin, unitmid, unitmax)
        with open("Price.txt", 'a+') as ptxt:
            outstr = str(totalmin) + '\t' + str(totalmid) + '\t' + str(totalmax) + '\t' + str(unitmin) + '\t' + str(
                unitmid) + '\t' + str(unitmax) + '\n'
            ptxt.write(outstr)
        print(totalmin, totalmid, totalmax, unitmin, unitmid, unitmax)
