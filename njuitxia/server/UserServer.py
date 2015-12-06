#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-5

@author: LC
'''

__all__ = ["login", "logout", "checkInfo", "addknight", "delknight", "allknight", "upadmin"]

from dao import UserDao
import web
import hashlib

session = web.ctx.session

def login(account, pw):
    userInfo = UserDao.getUser(account);
    if (len(userInfo) == 1):
        if (userInfo[0].password == pw):
            if (userInfo[0].admin == 1):
                result = "admin"
            else:
                result = "knight"
            session.id = userInfo[0].id
            session.status = result
            session.account = account
            session.location = userInfo[0].location
        else:
            result = u"密码错误"
    else:
        if (account.isdigit() and (len(account) < 20)):
            if (account == pw):
                result = "helper"
                session.status = result
                session.location = "donothave"
                session.id = account
                session.account = account
            else:
                result = u"两次电话不相同"
        else:
            result = u"请输入正确的电话号码"
    return result

def getLocation():
    return session.location

def logout():
    session.kill()
    pass

def checkInfo():
    if (session.id and session.status and session.location and session.account):
        return session.status
    else:
        session.kill()
        return "wrong"

def addknight(name, account, email, pw , location):
    UserDao.insert(name, account, email, pw, location)
    pass

def delknight(account):
    UserDao.delete(account)
    pass

def allknight():
    return UserDao.getAll()

def upadmin(account):
    UserDao.changeAdmin(account)
    pass
    
def test():
    UserDao.test()
    pass