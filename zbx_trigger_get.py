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
        #item=zapi.trigger.get({"output": ["value"], "selectItems":["itmeid"], "search":{"name":"ora"}})
        #item=zapi.trigger.get({"output": "extend", "filter": {"value": 1}, "selectHosts":["hostid", "name"], })
        item=zapi.trigger.get({"output": "extend", "filter": {"value": 1}, "selectHosts":["hostid", "name"], })
        print item
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
