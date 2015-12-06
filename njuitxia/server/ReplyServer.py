#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-20

@author: LC
'''

import web
from dao import ReplyDao
from datetime import datetime

session = web.ctx.session

def knightRelpy(oid, content):
    id = session.id
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    ReplyDao.addReply(1, oid, id, time, content)
    pass

def helperReply(oid, content):
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    ReplyDao.addReply(0, oid, 0, time, content)
    pass

def checkIsPoster(rid):
    id = session.id
    return ReplyDao.check_index_itxia(rid, id)

def delReply(rid):
    return ReplyDao.delReply(rid)
