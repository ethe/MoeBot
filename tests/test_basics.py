# -*- coding:utf-8 -*-

import unittest
import re
from moebot.wikipedia_client import client


class WikipediaClientTest(unittest.TestCase):

    def runTest(self):
        response = client("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
        assert re.match(r"^[\s\S]*Gotzehsing[\s\S]*$", response.read())
