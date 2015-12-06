#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-5

@author: LC
'''
from config.setting import conn,cur
import random
def getUser(account):
    result = []
    try:
        cur.execute("select * from members where account = " + account)
        userInfo = cur.fetchall()
        for each in userInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def getAll():
    result = []
    try:
        cur.execute('select * from members order by id ASC')
        userInfo = cur.fetchall()
        for each in userInfo:
            result.append(each)
    except Exception, e:
        print e
    return result

def insert(name, account, email, pw, location):
    try:
        cur.execute('insert into members (name,account,password,location,admin,email) values ('+name+','+account+','+pw+','+location+','+admin+','+email+')')
        con.commit()
        return 1
    except:
        return None

    
def delete(account):
    try:
        cur.execute('delete from members where accout = ' + account)
        conn.commit()
        return 1
    except:
        return None


def changeAdmin(account):
    try:
        cur.execute('delete from members where accout = ' + account + 'and admin = 1')
        return 1
    except:
        return None
    
def test():
    placeList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
    name1 = "两岸猿声啼不住轻舟已过万重山"
    name2 = "两个黄鹂鸣翠柳一行白鹭上青天"
    name3 = "老夫聊发少年狂左牵黄右擒苍"
    kc1 = ["物理", "历史"]
    kc2 = ["地理", "政治", "化学", "生物"]
    kccj = ["A+", "A", "B", "C", "D"]
    bkzz = ["", "Z"]
    zzxx = ["南京大学", "东南大学", "北京大学", "上海交大"]
    school = ["南京市第一中学", "南通市第二中学", "苏州市第三中学"]
    sex = ["男", "女"]
    for place in placeList:
        for i in range(1000):
            kjh = "14848484" + place + str(i)
            ksh = "1432" + place + "546684" + str(i)
            zkzh = ksh + "12"
            xm = name1[i%len(name1)] + name2[i%len(name2)] + name3[i%len(name3)]
            xb = sex[i%len(sex)]
            tylwhzf = 0
            ptlzf = str(random.randint(1,480))
            xxkm4mc = kc1[i%2]
            xxkm4dd = kccj[i%5]
            xxkm5mc = kc2[i%4]
            xxkm5dd = kccj[i%5]
            qswc = str(0)
            bkzzxbbj = bkzz[i%2]
            if (i%2 == 1):
                bkzzxbgx = zzxx[i%2]
            else:
                bkzzxbgx = ""
            lxdhyd = "15850771998"
            lxdhgd = "02583691104"
            kstzmc = ""
            byzxmc = school[i%3]
            add(kjh, ksh, zkzh, xm, xb, tylwhzf, ptlzf, xxkm4mc, xxkm4dd, xxkm5mc, xxkm5dd, qswc, bkzzxbbj, bkzzxbgx, lxdhyd, lxdhgd, kstzmc, byzxmc)
 
def add(kjh, ksh, zkzh, xm, xb, tylwhzf, ptlzf, xxkm4mc, xxkm4dd, xxkm5mc, xxkm5dd, qswc, bkzzxbbj, bkzzxbgx, lxdhyd, lxdhgd, kstzmc, byzxmc):
    mydb.insert('stu', kjh=kjh, ksh=ksh, zkzh=zkzh, xm=xm, xb=xb, tylwhzf=tylwhzf, ptlzf=ptlzf, xxkm4mc=xxkm4mc, xxkm4dd=xxkm4dd, xxkm5mc=xxkm5mc, xxkm5dd=xxkm5dd, qswc=qswc, bkzzxbbj=bkzzxbbj, bkzzxbgx=bkzzxbgx, lxdhyd=lxdhyd, lxdhgd=lxdhgd, kstzmc=kstzmc, byzxmc=byzxmc)
    