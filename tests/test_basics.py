# -*- coding:utf-8 -*-

import unittest
import os
from moebot.text_matching import extract_text
from moebot.api import login, token, edit, pick
from moebot.utils.constants import session_key, cookie_key


class HTMLAnalyseTest(unittest.TestCase):

    def runTest(self):
        try:
            f = open("tests/test.html")
            response = f.read()
        except:
            response = pick("https://zh.moegirl.org/index.php", "萌拟人化")
        try:
            response = response.decode("utf-8")
        except:
            pass
        print response
        result = extract_text(response)
        assert result != [] and result is not None
        with open("tests/test.txt", "w") as f2:
            for i in result:
                f2.write(i.encode("utf-8"))
                f2.write(", ")

    def tearDown(self):
        os.remove("tests/test.txt")


class CreateEntry(unittest.TestCase):

    def pick_test(self):
        assert pick("https://zh.moegirl.org/index.php", "萌拟人化") != ""

    def runTest(self):
        api_url = "https://zh.moegirl.org/api.php"
        login_response = login(api_url, "Zeno", "0.618033")
        print str(login_response)
        cookie = "{}={}; {}={};".format(session_key["zh.moegirl.org"], login_response["sessionid"],\
                                        cookie_key["zh.moegirl.org"], login_response["lgtoken"])
        print cookie
        csrftoken = token(api_url, cookie)
        print csrftoken
        f1 = open("tests/edittest.txt")
        response = edit(api_url, csrftoken, cookie, "spellworks", f1.read())
        print response
        with open("tests/testcase2.txt", "w") as f:
            f.write(response)
        print "Done"
        f1.close()
        self.pick_test()

    def tearDown(self):
        os.remove("tests/testcase2.txt")
