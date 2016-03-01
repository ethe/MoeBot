# -*- coding:utf-8 -*-

import re
import jieba.analyse


IGNORE_KEYWORD_LIST = [u"编辑", u"维基百科", u"页面", u"小节", u"本页", u"別名", u"维基", u"列表", u"搜索"]


def extract_text(html):
    string = u""
    re_expression = re.compile(u"[\u4e00-\u9fa5]+")
    re_result = re.findall(re_expression, html.decode("utf-8"))
    if re_result:
        for i in re_result:
            string = string + i
    word_generator = jieba.analyse.extract_tags(string, 30)
    return [word for word in word_generator]


def matching(keyword_map, another_keyword_map):
    pass
