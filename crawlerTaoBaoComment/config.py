# coding=utf-8
from selenium import webdriver

# 保存链接的文件
URLS_FILE = 'file/urls.txt'

# 输出文件的Excel路径
OUT_FILE = 'file/result.xls'

# 计数文件
COUNT_TXT = 'file/count.txt'

# Chrome浏览器驱动
DRIVER = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")

# 采集超时时间
TIMEOUT = 30

# 下拉滚动条的最大次数
MAX_SCORLL_TIME = 10

# 总共采集到的链接数
TOTAL_URLS_COUNT = 0

# 当前采集到第几个链接
NOW_URL_COUNT = 0

# 登录淘宝的链接
LOGIN_URL = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.50862.754894437.1.MVF6jc&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'

# 采集淘宝链接的搜索页面
SEARCH_LINK = 'https://www.tmall.com/?spm=a220m.1000858.a2226n0.1.kM59nz'

# 采集链接临时变量
CONTENT = ''

# 采集淘宝链接的翻页数量
PAGE = 25

# 是否过滤相同的店铺
FILTER_SHOP = False

# 匿名用户标识，已失效
ANONYMOUS_STR = '***'
