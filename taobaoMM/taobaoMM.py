# -*- coding:utf-8 -*-
import urlib2
import re


class TaobaoMM:
    def __init__(self):
        self.siteUrl = "http://mm.taobao.com/json/request_top_list.htm"


    def getPage(self, pageIndex):
        url = self.siteUrl + "?page=" + str()