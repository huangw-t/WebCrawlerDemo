# coding=utf-8
import crawlerTaoBaoComment.config as config
import sys
from getRecommends import deal_recommends_infos
from getUrls import get_urls
from write_to_excel import get_count, write_count

reload(sys)
sys.setdefaultencoding("utf-8")


def scrap(url):
    deal_recommends_infos(url)


def from_input():
    print u"请输入宝贝链接"
    url = raw_input()
    driver = config.DRIVER
    driver.get(config.LOGIN_URL)
    print u"请完成登录之后，输入查询关键字，开始爬取信息"
    raw_input()
    scrap(url)
    print u"采集结束"


def from_file():
    driver = config.DRIVER
    driver.get(config.LOGIN_URL)
    print u"请完成登录之后，输入查询关键字，开始爬取信息"
    raw_input()
    urls = get_urls()
    config.TOTAL_URLS_COUNT = len(urls)
    print u'共有', config.TOTAL_URLS_COUNT, u'个链接'
    count = int(get_count())
    print u'上次爬取到第', int(count) + 1, u'个链接，继续爬取'
    print u'输入1继续爬取，输入2重新爬取：'
    num = raw_input()
    if num == '2':
        count = 0
        print u'开始重新爬取'
    if count < config.TOTAL_URLS_COUNT:
        for count in range(count, config.TOTAL_URLS_COUNT):
            write_count(count, config.COUNT_TXT)
            url = urls[count]
            print u'正在爬取第', count + 1, u'个网页, 共', config.TOTAL_URLS_COUNT, u'个网页'
            config.NOW_URL_COUNT = count
            scrap(url)
            count += 1
            print u'当前已采集', config.NOW_URL_COUNT + 1, u'个，共', config.TOTAL_URLS_COUNT, u'个网页'
        print u'采集结束，完成了', len(urls), u'个链接的采集'
    else:
        print u'链接上次已经全部爬取完毕'
