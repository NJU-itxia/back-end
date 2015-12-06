#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

from dao import OrderDao, ReplyDao, FileDao
from datetime import datetime
from flask import session

def getWaitList(location):
    wait = OrderDao.getWait(location)
    for each in wait:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return wait

def getWorkList(location):
    work = OrderDao.getWork(location)
    for each in work:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return work

def getFinishList(location, page):
    SIZE = 30
    finish = OrderDao.getFinish(location, page, SIZE)
    for each in finish:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return finish

def getSearchList(search, page):
    SIZE = 30
    search = OrderDao.getSearch(search, page, SIZE)
    for each in search:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return search

def getSearchNum(search):
    num = OrderDao.getSearchNum(search)
    return num

def getOrderNum(location):
    return OrderDao.getOrderCount(location)

def changeWait(oid):
    handler = session["id"]
    OrderDao.changeOrderStatus(oid, handler, 0)
    pass

def changeWork(oid):
    handler = session["id"]
    OrderDao.changeOrderStatus(oid, handler, 1)
    pass

def changeFinish(oid):
    handler = session["id"]
    OrderDao.changeOrderStatus(oid, handler, 2)
    pass

def getNewReplyOrder(location):
    orderList = OrderDao.getNewReplyOrder(location)
    for each in orderList:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return orderList

def getHelperOrder():
    orderList = OrderDao.getHelperOrder(session["id"])
    for each in orderList:
        each.reply = ReplyDao.getReply(each.id)
        each.filelist = FileDao.getFile(each.id)
    return orderList

def addOrder(bbs, local, model, os, desc, name):
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    return OrderDao.addOrder(time, session["id"], bbs, local, model, os, desc, name)

def delOrder(oid):
    if (session["id"] == getOrderPhone(oid)):
        OrderDao.delOrder(oid)
    pass
    
def modifyOrder(oid, bbsid, location, model, os, desc, name):
    return OrderDao.modifyOrder(oid, bbsid, location, model, os, desc, name)

def getOrderPhone(oid):
    orderList = OrderDao.getOrder(oid)
    phone = "notexist"
    for each in orderList:
        phone = each.phone
    return phone