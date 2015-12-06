#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

from config.setting import mysql

def getFile(orderid):
    result = []
    try:
        cursor = mysql.connect.cursor()
        cursor.execute('yunfile', vars=locals(), where="oid=$orderid")
        for each in fileList:
            result.append(each)
    except Exception, e:
        print e
    return result

def getAllFile():
    result = []
    try:
        fileList = mydb.select('yunfile', order="id ASC")
        for each in fileList:
            result.append(each)
    except Exception, e:
        print e
    return result

def add_file(time, name, oid, ext):
    try:
        mydb.insert('yunfile', time=time, name=name, oid=oid, ext=ext)
        return 1
    except Exception, e:
        return None

def del_file(name):
    try:
        mydb.delete('yunfile', where = "name='" + name + "'")
        return 1
    except Exception, e:
        return None