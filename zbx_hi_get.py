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
        item=zapi.history.get({"output":"extend", "history":0, "itemids":28891, "sortfield":"clock", "sortorder": "DESC", "time_from":1510560918, "time_till":1510647335})
        for it in item:
            print it
        '''
        for h in hostinfo:
            gid = h['groups'][0]['groupid']
            gname = h['groups'][0]['name']
            hid = h['hostid']
            hname = h['name']
            print "group id: %s , group name: %s , host id: %s , host name: %s " %(gid, gname, hid, hname)
            for g in h['graphs']:
                print "graph id: %s , graph name: %s " %(g['graphid'], g['name'])
        '''
    except:
        print "host not exist: %s" %server
