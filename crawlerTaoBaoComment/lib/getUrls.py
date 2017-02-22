# coding=utf-8
import re
import crawlerTaoBaoComment.config as config


def get_urls():
    """获取文件中的链接"""
    try:
        file = open(config.URLS_FILE, 'r')
        content = file.read()
        pattern = re.compile(r'(.*?//.*?)\s', re.S)
        urls = re.findall(pattern, content)
        return urls
    except Exception as e:
        print u'获取链接失败', e.message