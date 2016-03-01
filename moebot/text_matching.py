# -*- coding:utf-8 -*-

import re
import jieba.analyse
from zhtools.zh_wiki import zh2Hans


IGNORE_KEYWORD_LIST = [u"编辑", u"维基百科", u"页面", u"小节", u"本页",\
                       u"別名", u"维基", u"列表", u"搜索", u"百科", u"萌娘"]


def extract_text(html):
    """
    抽取页面中的中文，然后分词
    """
    string = u""
    re_expression = re.compile(u"[\u4e00-\u9fa5]+")
    re_result = re.findall(re_expression, html.decode("utf-8"))
    if re_result:
        for i in re_result:
            string = string + i
    word_generator = jieba.analyse.extract_tags(hant_to_zh(string), 30)
    return [word for word in word_generator]


def hant_to_zh(text):
    """
    繁体转简体
    """
    result = u""
    for character in text:
        try:
            result = result + zh2Hans[character.encode("utf-8")].decode("utf-8")
        except:
            result = result + character
    return result
