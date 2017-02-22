# coding=utf-8
import xlrd
import xlwt
import crawlerTaoBaoComment.config as config
from xlutils.copy import copy
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def create_excel_file(file=config.OUT_FILE):
    print u"发现写入目标文件不存在，正在创建文件", file
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    book.add_sheet('sheet1', cell_overwrite_ok=True)
    book.save(file)
    print u"已成功创建文件", file


def repeat_excel(word, file=config.OUT_FILE):
    print u"正在检测", word, u"是否存在文件夹中"
    try:
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheet_by_index(0)
        words = sheet.col_values(0)
        if word in words:
            print u"用户名在excel中已经存在", word, u"跳过该用户"
            return True
        else:
            print u"用户名在excel中不存在"
            return False
    except IOError, e:
        if 'No such file' in e.strerror:
            print u"匹配重复时未找到该文件", file
            create_excel_file(file)
            return False
        return False


def write_to_excel(contents, file=config.OUT_FILE):
    print u"正在写入到文本中", contents[0]
    try:
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheets()[0]
        rows = sheet.nrows
        wb = copy(workbook)
        sheet = wb.get_sheet(0)
        count = 0
        name = contents[0]
        if not repeat_excel(name, file):
            for content in contents:
                sheet.write(rows, count, content)
                count += 1
                wb.save(file)
                print u"已成功写入文件", file, u"第", rows + 1, u"行"
        else:
            print u"内存已存在， 跳过写入文件", file
    except IOError:
        create_excel_file(file)
        write_to_excel(contents, file)


def write_info(infos, file=config.OUT_FILE):
    if len(infos) >= 3:
        name = infos[0]
        print u"准备将", name, u'写入文件'
        comment = infos[1]
        url = infos[2]
        contents = (name, comment, url)
        write_to_excel(contents, file)
    else:
        print u"写入文件时发生错误，跳过写入"


def write_count(count, file):
    try:
        with open(file, 'w') as f:
            f.write(str(count))
            f.close()
    except TypeError:
        print u"页码写入失败"


def get_count():
    try:
        with open(config.COUNT_TXT, 'r') as f:
            page = f.read()
            if not page:
                return 0
            else:
                return page
    except Exception:
        print u"不存在计数文件，可从开头开始抓取"
        return 0
