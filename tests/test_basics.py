# -*- coding:utf-8 -*-

import unittest
import re
import os
from moebot.wikipedia_client import client
from moebot.text_matching import extract_text


class WikipediaClientTest(unittest.TestCase):

    def runTest(self):
        response = client("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
        assert re.match(r"^[\s\S]*Gotzehsing[\s\S]*$", response)


class HTMLAnalyseTest(unittest.TestCase):

    def runTest(self):
        response = client("https://zh.wikipedia.org/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99")
        result = extract_text(response)
        assert result != [] and result is not None
        with open("tests/test.txt", "w") as f2:
            for i in result:
                f2.write(i.encode("utf-8"))
                f2.write(", ")

    def tearDown(self):
        os.remove("tests/test.txt")
