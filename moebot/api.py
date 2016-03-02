# -*- coding: utf-8 -*-

import time
import json
import urllib
import urllib2


def login(site, username, password, token=None, set_cookie=None, times=1):
    """
    MediaWiki api login
    :param site: witch wiki site api url wants to login, like: "https://zh.moegirl.org/api.php"
    :username: your username
    :password: your password
    :times: login attempt times,
    """
    try:
        with open("/tmp/moebos.txt") as f:
            return json.loads(f.read())
    except Exception, e:
        raise e
    headers = {}
    data = {
        "action": "login",
        "lgname": username,
        "lgpassword": password,
        "format": "json"
    }
    if token and set_cookie:
        data["lgtoken"] = token
        headers["Cookie"] = set_cookie
    data = urllib.urlencode(data)
    request = urllib2.Request(site, data, headers)
    response = urllib2.urlopen(request)
    response_content = json.loads(response.read())["login"]
    if response_content["result"] == "Success":
        with open("/tmp/moebox.txt", "w") as f:
            f.write(json.dumps(response_content))
        return response_content
    token = response_content["token"]
    set_cookie = response.headers.get("set-cookie")
    if times == 0:
        raise IOError("Request timeout")
    return login(site, username, password, token, set_cookie, times-1)


def pick(site, title):
    """
    get MediaWiki raw template
    :param site: wiki entry url, like: "https://zh.moegirl.org/index.php"
    :param title: the template's title wants to search
    """
    data = {
        "action": "raw",
        "title": title
    }
    data = urllib.urlencode(data)
    request = urllib2.Request(site, data)
    response = urllib2.urlopen(request)
    return response.read().decode("utf-8")


def token(site, cookie):
    """
    get MediaWiki api edit token
    """
    headers = {"cookie": cookie}
    data = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }
    data = urllib.urlencode(data)
    request = urllib2.Request(site, data, headers)  # get token
    response = json.loads(urllib2.urlopen(request).read())
    return response["query"]["tokens"]["csrftoken"]


def edit(site, csrftoken, cookie, title, text, summary=None):
    headers = {"cookie": cookie}
    data = {
        "action": "edit",
        "title": title,
        "basetimestamp": int(time.time()),
        "text": text,
        "summary": summary,
        "bot": "true",
        "format": "json",
        "token": csrftoken
    }
    data = urllib.urlencode(data)
    request = urllib2.Request(site, data, headers)
    response = urllib2.urlopen(request).read()
    return response.decode("unicode-escape").encode("utf-8")
