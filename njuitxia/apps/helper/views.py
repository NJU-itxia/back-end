#!/usr/bin/env python
# coding: utf-8

'''
Created on 2014-7-29

@author: LC
'''

from datetime import datetime

from tools.decorator import check_helper
from server import OrderServer, ReplyServer, FileServer

from flask import request,session

@check_helper
def now():
    if request.me
    def GET(self):
        orderlist = OrderServer.getHelperOrder()
        if ((not orderlist) or (len(orderlist) == 0) or (orderlist[0].status == 2)):
            return render_helper.now_post(session.id)
        else:
            data = OrderServer.getOrderNum(orderlist[0].location)
            for each in orderlist[0].reply:
                if (each.replybool==0):
                    each.name = "我";
            number = data[0] + data[1]
            filelist = orderlist[0].filelist
            return render_helper.now_exist(orderlist[0], number, filelist)

class history:
    @check_helper
    def GET(self):
        orderlist = OrderServer.getHelperOrder()
        return render_helper.history(orderlist)
    
class addorder:
    @check_helper
    def POST(self):
        i = web.input()
        name = protect(i.name)
        bbs = protect(i.bbs)
        local = protect(i.local)
        model = protect(i.model)
        os = protect(i.os)
        desc = protect(i.desc)
        OrderServer.addOrder(bbs, local, model, os, desc, name)
        return web.seeother("/helper/now")

class modify:
    @check_helper
    def GET(self):
        orderlist = OrderServer.getHelperOrder()
        if ((not orderlist) or (len(orderlist) == 0) or (orderlist[0].status == 2)):
            return web.seeother("/helper/now")
        else:
            for each in orderlist[0].reply:
                if (each.replybool==0):
                    each.name = "我";
            return render_helper.modify(orderlist[0])

    @check_helper
    def POST(self):
        i = web.input()
        name = protect(i.name)
        oid = protect(i.oid)
        bbs = protect(i.bbs)
        local = protect(i.local)
        model = protect(i.model)
        os = protect(i.os)
        desc = protect(i.desc)
        OrderServer.modifyOrder(oid, bbs, local, model, os, desc, name)
        return web.seeother("/helper/now")

class delorder:
    @check_helper
    def GET(self, oid):
        oid = protect(oid)
        OrderServer.delOrder(oid)
        return web.seeother("/helper/now")
    
class reply:
    @check_helper
    def POST(self):
        i = web.input()
        order = protect(i.order)
        content = protect(i.content)
        ReplyServer.helperReply(order, content)
        referer = web.ctx.env.get("HTTP_REFERER")
        return web.seeother(referer)

class upload:
    @check_helper
    def POST(self):
        i = web.input(oid=None, name=None, ext=None)
        oid = protect(i.oid)
        name = protect(i.name)
        ext = protect(i.ext)
        ext = ext.upper()
        if (oid and name and ext):
            FileServer.addFile(name, oid, ext)
            return '{"success":true}'
        else:
            return '{"success":false}'

def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace('  ','&nbsp;&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word