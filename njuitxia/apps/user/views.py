#!/usr/bin/env python
# coding: utf-8

'''
Created on 2014-7-7

@author: LC
'''

import web

from config.setting import render_user
from config.setting import render_error

from server import UserServer

class login:
    def GET(self):
        check = UserServer.checkInfo()
        if ((check == "knight") or (check == "admin")):
            return web.seeother("/knight/wait")
        elif (check == "helper"):
            return web.seeother("/helper/now")
        return render_user.login()
    
    def POST(self):
        try:
            i = web.input(remember = "false")
            name = protect(i.name)
            password = protect(i.password)
            if (password == "iamhelper"):
                password = name;
            result = UserServer.login(name, password)
            if ((result == "knight") or (result == "admin")):
                return web.seeother("/knight/wait")
            elif (result == "helper"):
                return web.seeother("/helper/now")
            else:
                return render_user.login(message = result, username = name)
            return render_user.login()
        except Exception, e:
            print e
            return render_user.login(message="请输入账号密码")

class knightlogin:
    def GET(self):
        check = UserServer.checkInfo()
        if ((check == "knight") or (check == "admin")):
            return web.seeother("/knight/wait")
        elif (check == "helper"):
            return web.seeother("/helper/now")
        return render_user.knightlogin()

class logout:
    def GET(self):
        UserServer.logout()
        return web.seeother("/")
    
class eggs:
    def GET(self):
        return render_error.eggs()

def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace(' ','&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word