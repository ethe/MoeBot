# -*- coding:utf-8 -*-

import unittest
import re
from moebot.wikipedia_client import client
from moebot.keywords_algorithm import extract_text


class WikipediaClientTest(unittest.TestCase):

    def runTest(self):
        response = client("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
        assert re.match(r"^[\s\S]*Gotzehsing[\s\S]*$", response.read())


class HTMLAnalyseTest(unittest.TestCase):

    def runTest(self):
        with open("tests/test.html") as f:
            result = extract_text(f.read())
            assert result != []
