#!/usr/bin/python



userinfo = ('kangxin', '1')
REMOTE_HOST = '192.168.1.244'
#REMOTE_HOST = '112.124.44.2**'
REMOTE_PORT = 80
USERNAME = '****'
PASSWORD = '****'

the_test_url = [
    ('/mobile/',),
    ('/mobile/filter/?_fs_=client_info:region:level:type:error_type',),
    ('/mobile/station/?_sp_region=1',),
    ('/mobile/station/87/detail/',),
    ('/mobile/error/?_sp_region=1',),
    ('/mobile/error/122/detail/',),
#    ('/mobile/error/122/dispatch/?status=1&operators=')
    ('/mobile/report/',),
    ('/mobile/report/6/detail/',),
    ('/mobile/photo/?_sp_region=1',),
    ('/mobile/video/?_sp_region=1',),
    ('/mobile/battery/?_sp_region=1',),
    ('/mobile/battery/82/detail/',),
    ('/mobile/battery/detail/32/h5/',),
    ('/mobile/user/'),
    (),  #"""pdatepic"""
    (),  #"""feedback"""
    (),  #"""station-about"""
    ('/mobile/submit-focus/?focus_station_id=45:46',),
    ('/mobile/myfocus/',),
    ('/mobile/get-carousel/',),
    (),  #"""switch-device-pattern"""
    (),  #"""living"""
    (),  #"""visitors-flowrate"""
    (),  #"""tail-query"""
    (),  #"""ignore nearby action """
    ('/mobile/info/',),
    ('/mobile/nearby/?lat=31.2099376&lng=121.424326&scope=3000',),
    ('/mobile/notification/',),
    ('/mobile/message/',),
    ('/mobile/operator/',),
]
