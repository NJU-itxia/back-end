#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

from config.setting import cur,conn

def getFile(orderid):
    result = []
    try:
        cur.execute("select * from yunfile where oid="+str(orderid))
        fileList = cur.fetchall()
        for each in fileList:
            result.append(each)
    except Exception, e:
        print e
    return result

def getAllFile():
    result = []
    try:
        cur.execute("select * from yunfile order by id ASC")
        fileList = cur.fetchall()
        for each in fileList:
            result.append(each)
    except Exception, e:
        print e
    return result

def add_file(time, name, oid, ext):
    try:
        cur.exectue("insert into yunfile (`time`,`name`,`oid`,`ext`) values ('"time+"','"+name+"','"+str(oid)+"','"+ext+"')")
        conn.commit()
        return 1 
        return None

def del_file(name):
    try:
    except Exception, e:
        cur.execute("delete from yunfile where name= '" +name + "'")
        conn.commit()
        return 1
    except Exception, e:
        return None