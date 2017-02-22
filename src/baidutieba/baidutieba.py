# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
from Tool import Tool


class Baidutieba:
    #参数seeLz:是否只看楼主, floorTag:是否写入楼层分隔符 
    def __init__(self, baseUrl, seeLz, floorTag):
        self.baseUrl = baseUrl
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent' : self.user_agent, 'Content-Type':'text/html; charset=UTF-8', 'Vary':'Accept-Encoding'}
        self.seeLz = '?see_lz=' + str(seeLz)
        self.tool = Tool()
        self.floor = 1
        self.defaultTitle = u"百度贴吧"
        self.floorTag = floorTag
    
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLz + "&pn=" + str(pageNum)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            #print response.read().decode('utf-8')
            return response.read().decode('utf-8')
        except urllib2.URLError as e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败，错误原因：", e.reason
                return None

    # 获取帖子标题
    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None


    # 提取帖子页数
    def getPageNums(self, page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None


    # 获取每一层楼的内容，传入页面内容
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)<.div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents


    def setFileTitle(self, title):
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")


    def writeData(self, contents):
        for item in contents:
            if str(self.floorTag) == "1":
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1


    def start(self):
        indexPage = self.getPage(1)
        pageNums = self.getPageNums(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNums == None:
            print u"URL失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNums) + "页"
            for i in range(1, int(pageNums) + 1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print "写入文件异常，原因：" + e.message
        finally:
            print u"写入文件完毕"


if __name__ == '__main__':
    number = raw_input(u"请输入帖子代号,必须是数字:")
    baseUrl = "http://tieba.baidu.com/p/" + str(number)    
    seeLz = raw_input(u"是否只获取楼主的发言，是：y，否：n\n")
    floorTag = raw_input(u"是否写入楼层信息，是：y，否：n\n")
    seeLz = 1 if str(seeLz) == "y" else 0
    floorTag = 1 if str(floorTag) == "y" else 0
    bdtb = Baidutieba(baseUrl, seeLz, floorTag)
    bdtb.start()
