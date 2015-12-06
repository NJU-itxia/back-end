#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015/5/25

@author: LC
'''

import qiniu.rsf
import qiniu.rs
from datetime import datetime

from config.setting import bucketName
from dao import FileDao

def get_qiniu_list():
    rs = qiniu.rsf.Client()
    marker = None
    err = None
    data = []
    while err is None:
        ret, err = rs.list_prefix(
            bucketName, prefix=None, limit=10, marker=marker)
        marker = ret.get('marker', None)
        for item in ret['items']:
            data.append(item['key'])
            pass
    if err is not qiniu.rsf.EOF:
        # 错误处理
        pass
    return data

def get_mysql_list():
    return FileDao.getAllFile()

def getFile(oid):
    return FileDao.getFile(oid)

def delFile(name):
    ret, err = qiniu.rs.Client().delete(bucketName, name)
    FileDao.del_file(name)
    pass

def addFile(name, oid, ext):
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    return FileDao.add_file(time, name, oid, ext)