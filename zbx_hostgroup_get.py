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
        hostgroupinfo = zapi.hostgroup.get({"output":"extend",})
        #hostgroupinfo = zapi.hostgroup.get({"output":"extend","groupids": 18, "selectHosts": "count",})
        print hostgroupinfo
        '''
        for g in hostgroupinfo:
            print "group id: %s , name: %s" % (g['groupid'], g['name'])
        '''
    except:
        print "hostgroup not exist: %s" %server
