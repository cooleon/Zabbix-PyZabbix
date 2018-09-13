#!/usr/bin/env python
#coding:utf8

'''
Created on 2016年 08月 25日 星期四 15:22:01 CST
'''

import ConfigParser
import requests
import urllib2,urllib,cookielib
from core import ZabbixAPI

cf =  ConfigParser.ConfigParser()
cf.read("config.ini")
server = cf.get("zabbix_server", "server")
username = cf.get("zabbix_server", "username")
password = cf.get("zabbix_server", "password")

def get_gra_info():
    try:
        hostinfo = zapi.host.get({ "filter": {"hostid": [10244, 10084,10234]}, "output": ["hostid", "name", ], "selectGraphs": ["graphid", "name"]})
        return hostinfo
    except:
        print "host not exist: %s" %server

def get_graph(graphs,stime,period,width=539,height=304):
    login_data = urllib.urlencode({
        "name": username,
        "password": password,
        "autologin": 1,
        "enter": "Sign in"})
    
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    opener.open(server + "/index.php",login_data).read()
   
    for graph in graphs:
        graph_args = urllib.urlencode({
            "graphid": graph["id"],
            "width": width,
            "height": height,
            "stime": stime,
            "period": period})
        
        if graph["type"] == 2:
            png_data = opener.open(server + "/chart6.php", graph_args).read()
        else :
            png_data = opener.open(server + "/chart2.php", graph_args).read()
        png_f = open("/opt/mozbx/" + str(graph["id"]) + ".png", "wb")
        png_f.write(png_data)
        png_f.flush()
        png_f.close()
        print "test file is  /opt/mozbx/" + str(graph["id"]) + ".png, please check."

if __name__ == "__main__":
    zapi = ZabbixAPI(server, username, password)
    list = get_gra_info()
    for i in list:
        graphs=i["graphs"]
        for g in graphs:
            get_graph([{"id":g["graphid"], "type": 1}],20161122160027,3600)
    print "ok"
