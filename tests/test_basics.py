# -*- coding:utf-8 -*-

import unittest
import re
import os
from moebot.wikipedia_client import client
from moebot.text_matching import extract_text
from moebot.api import login, token, edit
from moebot.utils.constants import session_key, cookie_key


class WikipediaClientTest(unittest.TestCase):

    def runTest(self):
        response = client("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
        assert re.match(r"^[\s\S]*Gotzehsing[\s\S]*$", response)


class HTMLAnalyseTest(unittest.TestCase):

    def runTest(self):
        try:
            f = open("tests/test.html")
            response = f.read()
        except:
            response = client("https://zh.wikipedia.org/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99")
        result = extract_text(response)
        assert result != [] and result is not None
        with open("tests/test.txt", "w") as f2:
            for i in result:
                f2.write(i.encode("utf-8"))
                f2.write(", ")

    def tearDown(self):
        os.remove("tests/test.txt")


class CreateEntry(unittest.TestCase):

    def runTest(self):
        api_url = "https://zh.moegirl.org/api.php"
        login_response = login(api_url, "Zeno", "0.618033")
        print str(login_response)
        cookie = "{}={}; {}={};".format(session_key["zh.moegirl.org"], "683472625f7ffb09188a7c3d7d2d82fe",\
                                        cookie_key["zh.moegirl.org"], "c3b1a21c42930a3766c752b022dc8565")
        print cookie
        csrftoken = token(api_url, cookie)
        print csrftoken
        f1 = open("edittest.txt")
        response = edit(api_url, csrftoken, cookie, "spellworks", f1.read())
        with open("testcase2.txt", "w") as f:
            f.write(response)
        print "Done"

    def tearDown(self):
        os.remove("tests/testcase2.txt")
