# -*- coding: utf-8 -*-
import re


"""处理页面标签"""
class Tool:
    #去除img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')

    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')

    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    # 把表格<td>替换为\t
    replaceTd = re.compile('<td>')

    # 把段落开头替换为\n加两空格
    replaceP = re.compile('<p.*?>')

    #将换行符或者双换行符替换为\n
    replaceBr = re.compile('<br><br>|<br>')

    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTd, "\t", x)
        x = re.sub(self.replaceP, "\n  ", x)
        x = re.sub(self.replaceBr, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()


