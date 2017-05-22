
# -*- coding: utf8 -*-
import cookielib
import json
import urllib
import urllib2
import logging

REMOTE_HOST = 'localhost'
REMOTE_PORT = 80

def _use_cookie():
    cj = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    return cj

def remote_login(username, password, **kwargs):
    cj = _use_cookie()
    remote_host = kwargs.get('host', REMOTE_HOST)
    remote_port = kwargs.get('port', REMOTE_PORT)
    remote_uri = kwargs.get('uri', 'mobile/login/')
    url = "http://%s:%d/%s" % (remote_host, remote_port, remote_uri)

    urllib2.urlopen(url)
    csrftoken = ''
    for cookie in cj:
        if cookie.name == 'csrftoken':
            csrftoken = cookie.value

    data = {}
    data['username'] = username
    data['password'] = password
    data['csrfmiddlewaretoken'] = csrftoken

    res = urllib2.urlopen(url, urllib.urlencode(data))
    remote_session = ''
    for cookie in cj:
        if cookie.name == 'sessionid':
            remote_session = cookie.value
    jsonhtml = res.read()
    resobj = json.loads(jsonhtml)
    if int(resobj['status']) == 0:
        cj.clear()
        return None

    resobj['remote_session'] = remote_session
    # cj.clear() #不清除session
    return resobj

# res = remote_login(username='kx', password='2012', uri='mobile/login/')
# print(res)
#
# rsp = urllib2.urlopen("http://localhost/mobile/register/")
# tmp = rsp.read()
# tmp = json.loads(tmp)
# print(tmp)
# tmp.pop("status")
# data = {"username":"testss", "password":"2012", "email":"123@123.com"}
# data.update(tmp)
# res = urllib2.urlopen("http://localhost/mobile/register/", urllib.urlencode(data))
# print(res.read())

def test_update_user_info():
    username = 'kx'
    phone = '18211710965'
    email = 'k123@123.com'
    gender = "嘉定区"
    address = "菊园"
    position = '老师'
    company = '赢谊'
    f = read('D:/test.jpg')
    jpg = f.read()
    head_protrait = jpg
    bg_image = jpg
