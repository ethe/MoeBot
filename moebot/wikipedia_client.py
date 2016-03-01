# -*- coding:utf-8 -*-

import os
import urllib2

if "cookie" in os.environ:
    cookie = os.environ["cookie"]
else:
    cookie = "CP=H2; WMF-Last-Access=29-Feb-2016; GeoIP=JP:::35.69:139.69:v4; \
              zhwikimwuser-sessionId=b839417fc6d293c7; centralauth_LoggedOut=1456737418; \
              zhwikiSession=j0p4trkdrbo5er5jheq82oifuonuem9a; zhwikiUserID=2232331; \
              zhwikiUserName=Gotzehsing; forceHTTPS=true; centralauth_User=Gotzehsing; \
              centralauth_Token=3ea5d648484832545b40473e818a5ac8; \
              centralauth_Session=321d61e432ee242c3b31b4209aecf15c; TBLkisOn=0"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4",
    "cache-control": "max-age=0",
    "cookie": cookie,
    "if-modified-since": "Mon, 29 Feb 2016 09:17:27 GMT",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/48.0.2564.109 Safari/537.36"
    }


def client(url):
    request = urllib2.Request(url)
    for key in headers:
        request.add_header(key, headers[key])
    response = urllib2.urlopen(request)
    return response.read()
