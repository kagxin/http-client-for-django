#!/usr/bin/python

import cookielib
import json
import urllib
import urllib2
import logging

REMOTE_HOST = '192.168.1.244'
REMOTE_PORT = 80
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
 

class DjangoClient(object):
    def __init__(self, username, password):
        self._login(username, password)
        self.error_cnt = 0
        
    def _use_cookie(self):
        cj = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        return cj

    def _login(self, username, password, **kwargs):
        cj = self._use_cookie()
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
        
        return resobj

    def get(self, url):
        url = "http://%s:%d"%(REMOTE_HOST,REMOTE_PORT) + url
        res = urllib2.urlopen(url)
        if res.code != 200:
            self.error_cnt = self.error_cnt + 1

        return res

    def post(self, url, para):
        pass
    
client = DjangoClient('kx', '2017')

res = client.get("/mobile/")
print(res.read())
