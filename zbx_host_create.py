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
    with open("/root/c", "r") as f:
        for line in f.readlines():
            hosts = line.split(" ")
            try:
                hostinfo = zapi.host.create({"host": hosts[1],
                                             "interfaces": [ {"type": 2, "main": 1, "useip": 1, "ip": hosts[2].strip("\n"), "dns": "", "port": 161} ],
                                             "name": hosts[0],
                                             "groups": [{"groupid": 32}],
                                             "templates": [{"templateid": 18638}],})
                                             #"macros": [{"{$SNMP_COMMUNITY}": "public_gdsw"}]})
                print  hostinfo
            except:
                print "host not exist: %s" %server
        f.close()
