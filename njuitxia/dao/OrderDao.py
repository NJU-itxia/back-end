#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

import string
from config.setting import cur,conn

WORK = 1
FINISH = 2

def getWait(location):
    result = []
    try:

        cur.execute("SELECT `id`, `updatedon`, `phone`, `bbsid`, `location`, `model`, `os`, `desc`, `reply`, `name` FROM `order` WHERE `status`='0' AND `location`="+location+" ORDER BY `order`.`updatedon` ASC")
        orderInfo = cur.fetchall()
        for each in orderInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def getWork(location):
    result = []
    try:

        cur.execute("SELECT `order`.`id` as `id`, `updatedon`, `phone`, `bbsid`, `order`.`location` as `location`, `model`, `os`, `desc`, `reply`, `order`.`name` as `name` , `members`.`account` as `handler` FROM `order` LEFT JOIN `members` ON `order`.`handler`=`members`.`id` WHERE ( `order`.`status`='1' OR `order`.`status`='3' ) AND `order`.`location`="+location+" ORDER BY `order`.`updatedon` ASC")
        orderInfo = cur.fetchall()
        for each in orderInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def getFinish(location, page, size):
    result = []
    page = page * size
    try:

        cur.execute("SELECT `order`.`id` as `id`, `updatedon`, `phone`, `bbsid`, `order`.`location` as `location`, `model`, `os`, `desc`, `reply`, `order`.`name` as `name` , `members`.`account` as `handler` FROM `order` LEFT JOIN `members` ON `order`.`handler`=`members`.`id` WHERE `order`.`status`='2' AND `order`.`location`=$location ORDER BY `order`.`updatedon` DESC LIMIT "+page+", "+ size)
        orderInfo = cur.fetchall()
        for each in orderInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def getSearch(search, page, size):
    result = []
    page = page * size
    checkType = ["`phone`", "`bbsid`", "`model`", "`os`", "`desc`", "`order`.`name`"]
    condition = ""
    for index in range(len(checkType)):
        checkType[index] = checkType[index] + " LIKE '%%" + search + "%%' "
        pass
    condition=" OR ".join(checkType);
    try:

        cur.execute("SELECT `order`.`id` as `id`, `updatedon`, `phone`, `bbsid`, `order`.`location` as `location`, `model`, `os`, `desc`, `reply`, `order`.`name` as `name` , `members`.`account` as `handler` FROM `order` LEFT JOIN `members` ON `order`.`handler`=`members`.`id` WHERE " + condition + " ORDER BY `order`.`updatedon` DESC LIMIT "+page+", "+size)
        orderInfo = cur.fetchall()
        for each in orderInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def getSearchNum(search):
    result = []
    checkType = ["`phone`", "`bbsid`", "`model`", "`os`", "`desc`", "`order`.`name`"]
    condition = ""
    for index in range(len(checkType)):
        checkType[index] = checkType[index] + " LIKE '%%" + search + "%%' "
        pass
    condition=" OR ".join(checkType);
    try:

        cur.execute("SELECT count(*) AS num FROM `order` WHERE " + condition)
        orderInfo = cur.fetchall()
        for each in orderInfo:
            result.append(each)
    except Exception, e:
        print e
    return result[0].num


def getOrderCount(location):
    num = []
    result = []
    cur = mysql.connect.cur()
    cur.execute("SELECT count(*) AS num FROM `order` WHERE `status`='0' AND `location`="+location)
    waitNum = cur.fetchall()
    for each in waitNum:
        result.append(each)
    num.append(result[0].num)
    result = []
    cur.execute("SELECT count(*) AS num FROM `order` WHERE (`status`='1' OR `status`='3') AND `location`="+location)
    workNum = cur.fetchall()
    for each in workNum:
        result.append(each)
    num.append(result[0].num)
    result = []
    cur.execute("SELECT count(*) AS num FROM `order` WHERE `status`='2' AND `location`="+location)
    finishNum = cur.fetchall()
    for each in finishNum:
        result.append(each)
    num.append(result[0].num)
    return num

def changeOrderStatus(oid, handler, status):
    try:
        cur.execute("UPDATE order SET `handlder`="+handlder+",`status`="+status+" where id='"+oid+"'")
        return 1
    except:
        return None

def getNewReplyOrder(location):
    result = []
    try:
    
        replyList = mydb.query(" \
            SELECT * \
            FROM ( \
                SELECT `orderid`,`replybool`,`time` as `replytime` \
                FROM ( \
                    SELECT * \
                    FROM `reply` \
                    order by `index` desc \
                ) as b \
                GROUP BY b.`orderid` \
                having b.`replybool`='0' \
            ) as a \
            JOIN `order` \
            ON `order`.`id`=a.`orderid` AND `order`.`location`='" + location + "' order by a.`replytime` desc limit 0, 10")
        for each in replyList:
            result.append(each)
    except Exception, e:
        print e
    return result

def getHelperOrder(account):
    result = []
    try:

        cur.execute("SELECT * FROM `order` WHERE `phone`="+account+" ORDER BY `id` DESC")
        replyList = cur.fetchall()
        for each in replyList:
            result.append(each)
    except Exception, e:
        print e
    return result

def addOrder(time, phone, bbsid, location, model, os, desc, name):
    try:

        cur.execute("INSERT INTO `order` (`updatedon`, `phone`, `bbsid`, `location`, `model`, `os`, `desc`, `name`, `status`) VALUES ( '"+time+"\', '"+phone+"', '"+bbsid+"', '"+location+"', '"+model+"', '"+os+"', '"+desc+"', '"+name+"', '0');")
        return 1
    except Exception, e:
        print e
        return None

def getOrder(oid):
    result = []
    try:

        cur.excecute("SELECT * FROM `order` WHERE `id`='" + oid + "'")
        orderList = cur.fetchall()
        for each in orderList:
            result.append(each)
            pass
    except Exception, e:
        print e
    return result

def delOrder(oid):
    try:

        cur.excecute("DELETE FROM `order` where id = " + oid
        return 1
    except Exception, e:
        print e
        return None
        
def modifyOrder(oid, bbsid, location, model, os, desc, name):
    try:
        mydb.query("UPDATE `order` \
            SET `bbsid`='"+bbsid+"', \
            `location`='"+location+"', \
            `model`='"+model+"', \
            `os`='"+os+"', \
            `desc`='"+desc+"', \
            `name`='"+name+"' \
            WHERE id='"+oid+"';")
        return 1
    except Exception, e:
        print e
        return None