#!/usr/bin/env python
#coding:utf8

'''
Created on 03.06.2015
'''

import ConfigParser
from core import ZabbixAPI

cf =  ConfigParser.ConfigParser()
cf.read("config.ini")
server = cf.get("zabbix_server", "server")
username = cf.get("zabbix_server", "username")
password = cf.get("zabbix_server", "password")

if __name__ == "__main__":
    zapi = ZabbixAPI(server, username, password)

    try:
        #hostinfo = zapi.trigger.get({ "output": "extend", "filter": {"value": 1}, "selectHosts":["hostid", "name", "key"], "selectItems":["key_"], })
        hostinfo = zapi.event.get({ "output": "extend"})
        print  hostinfo
    except:
        print "host not exist: %s" %server
