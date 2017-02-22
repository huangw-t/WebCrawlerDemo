# -*- coding:utf-8 -*-
import urllib
import urllib2
import httplib
import re
import thread
import time


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent}
        self.stories = []
        self.enable = False # 程序是否继续运行


    def getPage(self, pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/" +  str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError as e:
            if hasattr(e, "reason"):
                print u"连接糗事百科失败，错误原因：", e.reason
                return None


    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content".*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        # item[0]: 段子发布者, item[1]: 内容，item[2]: 图片，item[3]: 点赞数
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, "\n", item[1])
                pageStories.append([item[0].strip(), text.strip(), item[3].strip()])
        return pageStories


    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1


    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Quit":
                self.enable = False
                return
            # 打印，0：name,1:contents,2:votes
            print u"第%d页\t发布人:%s\t点赞数:%s\n%s" % (page, story[0], story[2] ,story[1])


    def start(self):
        print u"开始读取糗事百科，按回车查看最新段子，Quit退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)


if __name__ == '__main__':
    spider = QSBK()
    spider.start()