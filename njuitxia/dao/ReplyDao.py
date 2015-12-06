#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''


from config.setting import cur,conn

def getReply(orderid):
    result = []
    try:
        cur.execute("SELECT `index`, `replybool`, `orderid`, `itxiaid`, `time`, `content`, `account` as `name` FROM `reply` JOIN `members` WHERE `itxiaid`=`id` AND `orderid`='"+str(orderid)+"' AND `replybool`='1' ORDER BY `reply`.`index` ASC")
        knightReply = cur.fetchall()
        cur.execute("SELECT `index`, `replybool`, `orderid`, `itxiaid`, `time`, `content` FROM `reply` WHERE `orderid`='"+str(orderid)+"' AND `replybool`='0' ORDER BY `reply`.`index` ASC")
        helperReply = cur.fetchall()
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
        cur.execute("INSERT INTO `reply` (`replybool`, `orderid`, `itxiaid`, `time`, `content`) VALUES ( '"+str(replybool)+"', '"+str(orderid)+"', '"+str(itxiaid)+"', '"+time+"', '"+content+"');")
        conn.commit()
        return 1
    except Exception, e:
        print e
        return 0

def check_index_itxia(rid, id):
    result = False
    try:
        cur.execute("SELECT `index` FROM `reply` WHERE `index`=$rid AND `itxiaid`="+str(id))
        replyList = cur.fetchall()
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
        cur.execute("DELETE FROM `reply` WHERE `index`= " + str(rid))
        conn.commit()
        return 1
    except Exception, e:
        print e
        return None
