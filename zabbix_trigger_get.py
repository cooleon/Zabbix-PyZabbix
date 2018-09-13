#!/usr/bin/env python
#coding:utf8

'''
Created on 03.06.2015
'''

import optparse
import sys
import traceback
from getpass import getpass
from core import ZabbixAPI

def get_options():
    usage = "usage: %prog [options]"
    OptionParser = optparse.OptionParser
    parser = OptionParser(usage)

    parser.add_option("-s","--server",action="store",type="string",\
        dest="server",help="(REQUIRED)Zabbix Server URL.")
    parser.add_option("-u", "--username", action="store", type="string",\
        dest="username",help="(REQUIRED)Username (Will prompt if not given).")
    parser.add_option("-p", "--password", action="store", type="string",\
        dest="password",help="(REQUIRED)Password (Will prompt if not given).")

    options,args = parser.parse_args()

    if not options.server:
        options.server = raw_input('server http:')

    if not options.username:
        options.username = raw_input('Username:')

    if not options.password:
        options.password = getpass()

    return options, args

def errmsg(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(-1)

if __name__ == "__main__":
    options, args = get_options()

    zapi = ZabbixAPI(options.server,options.username, options.password)

    triggers=zapi.trigger.get({"output": ["triggerid", "description", "priority", "value", "lastchange"], "filter": {"value": 1}, "sortfield": "priority", "sortorder": "DESC"})
    #print triggers
    for trigger in triggers:
        #print "triggerid: " + trigger["triggerid"]
        founctions = zapi.trigger.get({"triggerids": int(trigger["triggerid"]), "output": "functions", "selectFunctions": "extend"})
        founction_list = founctions[0]["functions"]
        itemid = founction_list[0]["itemid"]
        #print "itemid: " + itemid
        hostinfo = zapi.item.get({"output": ["hostid", "key_"], "itemids": itemid,})
        hostid =hostinfo[0]["hostid"]
        #print "hostid: " + hostid
        hostdes = zapi.host.get({"output": "extend", "hostids": hostid})
        hostname =hostdes[0]["host"]
        print "time: " +  trigger["lastchange"]
        print hostname
        description =  trigger["description"].replace("{HOST.NAME}", hostname)
        print "description: " + description

