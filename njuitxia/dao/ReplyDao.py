#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

import web
from config.setting import mydb

def getReply(orderid):
    result = []
    try:
        knightReply = mydb.query("SELECT `index`, `replybool`, `orderid`, `itxiaid`, `time`, `content`, `account` as `name` FROM `reply` JOIN `members` WHERE `itxiaid`=`id` AND `orderid`='$orderid' AND `replybool`='1' ORDER BY `reply`.`index` ASC", vars=locals())
        helperReply = mydb.query("SELECT `index`, `replybool`, `orderid`, `itxiaid`, `time`, `content` FROM `reply` WHERE `orderid`='$orderid' AND `replybool`='0' ORDER BY `reply`.`index` ASC", vars=locals())
        for each in knightReply:
            result.append(each)
        for each in helperReply:
            each.name = "用户"
            result.append(each)
    except Exception, e:
        print e
    result.sort(key = lambda each: each.index, reverse = False)
    return result

def addReply(replybool, orderid, itxiaid, time, content):
    try:
        if (content == ""):
            return 0
        mydb.query("INSERT INTO `reply` (`replybool`, `orderid`, `itxiaid`, `time`, `content`) VALUES ( '"+str(replybool)+"', '"+str(orderid)+"', '"+str(itxiaid)+"', '"+time+"', '"+content+"');")
        return 1
    except Exception, e:
        print e
        return 0

def check_index_itxia(rid, id):
    result = False
    try:
        replyList = mydb.query("SELECT `index` FROM `reply` WHERE `index`=$rid AND `itxiaid`=$id ", vars=locals())
        for each in replyList:
            result = True
            pass
        pass
        return result
    except Exception, e:
        print e
        return result

def delReply(rid):
    try:
        mydb.query("DELETE FROM `reply` WHERE `index`=$rid ", vars=locals())
        return 1
    except Exception, e:
        print e
        return None
