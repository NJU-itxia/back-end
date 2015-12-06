#!/usr/bin/env python
# coding: utf-8

'''
Created on 2014-7-29

@author: LC
'''
from datetime import datetime


from tools.decorator import check_knight, check_admin
from server import UserServer, OrderServer, ReplyServer, FileServer
from flask import session,request,render_template,abort, redirect, url_for

@app("/knight",methods=['GET', 'POST'])
@check_knight
def wait():
    if request.method == "GET":
        status = UserServer.checkInfo()
        location = UserServer.getLocation()
        data = OrderServer.getWaitList(location)
        number = OrderServer.getOrderNum(location)
        user = session["account"]
        return render_template("wait.html",
            number = number,
            waitlist = data, 
            status = status,
            usrt = user)
    

    
@app("/knight/finish",methods=['GET', 'POST'])
@check_knight
def finish(self):
    if request.method == "GET":
        status = UserServer.checkInfo()
        page = request.args.get("page")
        search = request.args.get("search")
        page = int(i.page)
        location = UserServer.getLocation()
        number = OrderServer.getOrderNum(location)
        user = session["session"]
        if (search):
            data = OrderServer.getSearchList(search, page)
            searchNum = OrderServer.getSearchNum(search)
            return render_template("search.html",
                number = number, 
                searchist = data,
                page = page,
                status = status,
                search = search,
                searchNum = searchNum,
                user = user)
        else:
            data = OrderServer.getFinishList(location, page)
            return render_template("finish.html",
                number = number,
                finishlist = data,
                page = page,
                status = status,
                user = user)

@app("/knight/message",methods=['GET', 'POST'])
@check_knight
def message():
    if request.method == "GET":
        status = UserServer.checkInfo()
        location = UserServer.getLocation()
        data = OrderServer.getNewReplyOrder(location)
        number = OrderServer.getOrderNum(location)
        user = session.account
        return render_template.("message.html",
            number = number,
            waitlist = data,
            status = status,
            user = user)

@app("/knight/setting",methods=['GET', 'POST'])
@check_admin
def setting():
    if request.method == "GET":
        status = UserServer.checkInfo()
        data = UserServer.allknight()
        locallist = FileServer.get_mysql_list()
        yunlist = FileServer.get_qiniu_list()
        for each in locallist:
            if each.name in yunlist:
                each.exist = True
                yunlist.remove(each.name)
            else:
                each.exist = False
        return render_template("setting.html",
            userlist = data,
            status = status, 
            filelist = locallist, 
            unuselist = yunlist)
            
@app("/knight/setting/add",methods=['GET', 'POST'])
@check_admin
def addknight():
    if request.method == "POST":
        try:
            name = protect(request.args.get("name"))
            account = protect(request.args.get("account"))
            email = protect(request.args.get("email"))
            password = protect(request.args.get("password"))
            location = protect(request.args.get("location"))
            UserServer.addknight(name, account, email, password , location)
            return redirect(url_for("setting")
        except Exception, e:
            print e
            return redirect((url_for("setting")))

@app("/knight/setting/del/<account>",methods=['GET', 'POST'])
@check_admin    
def delknight():
    if request.method == "GET":
        account = protect(account)
        UserServer.delknight(account)
        return redirect(url_for("setting"))

@app("/knight/setting/up/<account>",methods=['GET', 'POST'])
@check_admin
def upadmin():
    if request.method == "GET":
        account = protect(account)
        UserServer.upadmin(account)
        return redirect(url_for("setting"))

@app("/knight/towait",methods=['GET', 'POST'])
@check_knight
def toWait():
    @check_knight
    if request.method == "GET":
        oid = protect(request.args.get("id"))
        if (oid):
            OrderServer.changeWait(oid)
            pass
        referer = request.headers.get("HTTP_REFERER")
        return redirect(referer)

@app("/knight/towait",methods=['GET', 'POST'])
@check_knight
def toWork():
    if request.method == "GET":
        oid = protect(request.args.get("id"))
        if (oid):
            OrderServer.changeWork(oid)
            pass
        referer = request.headers.get("HTTP_REFERER")
        return redirect(referer)
    
@app("/knight/tofinish",methods=['GET', 'POST'])
@check_knight
def toFinish():
    if request.method == "GET":
        oid = protect(request.args.get("id"))
        if (oid):
            OrderServer.changeWork(oid)
            pass
        referer = request.headers.get("HTTP_REFERER")
        return redirect(referer)

@app("/knight/reply",methods=['GET', 'POST'])
@check_knight
def reply():
    if request.method == "POST":
        try:
            order = request.args.get("order")
            content = request.args.get("content")
            ReplyServer.knightRelpy(order, content)
            referer = request.headers.get("HTTP_REFERER") + "?p=ihateie"
            return redirect(referer)
        except Exception, e:
            print e
            return redirect(referer)

@app("/knight/delreply/<id>",methods=['GET', 'POST'])
@check_knight
def delreply():
    if request.method == "POST":
        rid = id
        if (ReplyServer.checkIsPoster(rid)):
            ReplyServer.delReply(rid)
        referer = request.headers.get("HTTP_REFERER") + "?p=ihateie"
        return redirect(referer)

@app("/knight/delfile",methods=['GET', 'POST'])
@check_knight
class delfile()
    @check_admin
    def POST(self):
        i = web.input()
        name = i.name
        answer = FileServer.delFile(name)
        referer = web.ctx.env.get("HTTP_REFERER") + "?p=ihateie"
        return web.seeother(referer)

def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace('  ','&nbsp;&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word