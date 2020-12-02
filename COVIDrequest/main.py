import requests
from lxml import etree


def crawler():
    url = "https://www.worldometers.info/coronavirus/#nav-yesterday"
    source = requests.get(url).text
    # html = etree.HTML(source)
    with open("covid.html", "w", encoding='utf-8') as f:
        lz = source.split('\n')
        f.writelines(lz)
    return etree.HTML(source)


def parser(html):
    # Yesterday data
    # lz = html.xpath(
    #     '//*[@id="main_table_countries_yesterday"]/tbody[1]/*[@class="odd"]' | '//*[@id="main_table_countries_yesterday"]/tbody[1]/*[@class="even"]')
    lz = html.xpath('//*[@id="main_table_countries_yesterday"]/tbody[1]/*')

    for item in lz:
        country = item.xpath('/td[2]/a/text()')
        print(country)


def main():
    html = crawler()
    parser(html)


if __name__ == '__main__':
    main()
