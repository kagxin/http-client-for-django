#!/usr/bin/python

import cookielib
import json
import urllib
import urllib2
from my_logger import get_logger
from my_config import userinfo, the_test_url, REMOTE_HOST, REMOTE_PORT, PASSWORD, USERNAME


logger = get_logger()

class DjangoClient(object):
    def __init__(self, username, password):
        self._login(username, password)
        self.error_case = []
        
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
        logger.info("url:{}".format(url))
        try:
            res = urllib2.urlopen(url)
        except urllib2.HTTPError:
            self.error_case.append(url)
            return {"message":"server internel error."}
        if res.code != 200:
            self.error_case.append(url)
            return res.read()
        try:
            dct = json.loads(res.read())
        except ValueError:
            return res.read()

        return json.dumps(dct, indent=1)

    def post(self, url, data):
        post_url = "http://%s:%d"%(REMOTE_HOST,REMOTE_PORT) + url
        res =  self.get(url)
        dct = json.loads(res)
        csrfmiddlewaretoken = dct.get('csrfmiddlewaretoken')
        data.update({"csrfmiddlewaretoken":csrfmiddlewaretoken})
        try:
            res = urllib2.urlopen(post_url, urllib.urlencode(data))
        except urllib2.HTTPError:
            self.error_case.append(url)
            return "500"
        if res.code != 200:
            self.error_case.append(url)
            return res.read()
        try:
            dct = json.loads(res.read())
        except ValueError:
            return res.read()

        return json.dumps(dct, indent=1)

    def test_case(self, *arg):
        if len(arg) == 0:
            arg = 'foo'
        if isinstance(arg[0],int):
            if len(the_test_url[arg[0]])==1:
                res = client.get(the_test_url[arg[0]][0])
                logger.info("{},{}".format(the_test_url[arg[0]][0], res))
            elif len(the_test_url[arg[0]])==2:
                res = client.post(*the_test_url[arg[0]])
                logger.info("{},{}".format(url[arg[0]][0], res))
            return
                
                
        for url in the_test_url:
            print(len(url))
            if len(url)==2:
                res = client.post(*url)
                logger.info("{},{}".format(url, res))
            elif len(url)==1:
                res = client.get(url[0])
                logger.info("{},{}".format(url, res))
            else:
                pass
    def test_case_feedback(self, *arg):
        url = '/mobile/feedback/'
        data = {"feedback_content":"kx feedback_content", "feedback_username":"kx", "feedback_contact":"18211712212"}

        res = self.post(url, data)
        print(res)

    def test_update_usr_data(self):
        url = '/mobile/update-user-info/'
        data = {"username":"kangxin", "phone":"18212345564", "email":"kangxin@163.com", "gender":"gender", "position":"asf", "company":"asdf", "dept":"asdf"}
        res = self.post(url, data)

        print(res)
    
    
client = DjangoClient(USERNAME, PASSWORD)

client.test_case(-4)

for url in client.error_case:
    logger.info("url:{}".format(url))

#client.test_case_feedback()
#client.test_update_usr_data()



