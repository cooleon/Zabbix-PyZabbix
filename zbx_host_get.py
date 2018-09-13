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
        hostinfo = zapi.host.get({ "output": ["hostid"]})
        #hostinfo = zapi.host.get({ "output": ["hostid"], "selectGroups": ["groupid"],})
        #hostinfo = zapi.host.get({ "filter": {"hostid": 10244}, "output": ["hostid", "name"], "selectGroups": ["groupid", "name"], "selectGraphs": ["graphid", "name"]})
        #hostinfo = zapi.host.get({ "filter": {"hostid": [10244, 10084,10234]}, "output": ["hostid", "name", "status" ], "selectGroups": ["groupid", "name"], "selectGraphs": ["graphid", "name"]})
        #hostinfo = zapi.host.get({ "filter": {"hostid": [10146]}, "output": "extend", "selectGraphs": ["graphid", "name"], "selectInterfaces": ["interfaceid"]})
        #hostinfo = zapi.host.get({"output": ["hostid", "name"], "limit": 10})
        '''
        {u'hostid': u'10874', u'name': u'hjdl-dpi', u'groups': [{u'groupid': u'65', u'name': u'\u8d3a\u6c5fdpi'}]}
        '''
        print  hostinfo
        '''
        for h in hostinfo:
            gid = h['groups'][0]['groupid']
            gname = h['groups'][0]['name']
            hid = h['hostid']
            hname = h['name']
            print "group id: %s , group name: %s , host id: %s , host name: %s " %(gid, gname, hid, hname)
        '''
    except:
        print "host not exist: %s" %server
