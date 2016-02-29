# -*- coding:utf-8 -*-

import re
import jieba.analyse


def extract_text(html):
    string = u""
    re_expression = re.compile(u"[\u4e00-\u9fa5]+")
    re_result = re.findall(re_expression, html.decode("utf-8"))
    if re_result:
        for i in re_result:
            string = string + i
    word_generator = jieba.analyse.extract_tags(string, 30)
    return [word for word in word_generator]
