#!/usr/bin/env python
# coding: utf-8

'''
Created on 2014-6-11

@author: LC
'''

urls = ("/",                            "action.user.login",
        "/login",                       "action.user.login",
        "/knightlogin",                 "action.user.knightlogin",
        "/logout",                      "action.user.logout",
        
        "/helper",                      "action.helper.now",
        "/helper/now",                  "action.helper.now",
        "/helper/history",              "action.helper.history",
        "/helper/order/add",            "action.helper.addorder",
        "/helper/order/del/(.*)",       "action.helper.delorder",
        "/helper/reply",                "action.helper.reply",
        "/helper/upload",               "action.helper.upload",
        "/helper/modify",               "action.helper.modify",
        
        "/knight",                      "action.knight.wait",
        "/knight/wait",                 "action.knight.wait",
        "/knight/work",                 "action.knight.work",
        "/knight/finish",               "action.knight.finish",
        "/knight/message",              "action.knight.message",
        "/knight/towait",               "action.knight.toWait",
        "/knight/towork",               "action.knight.toWork",
        "/knight/tofinish",             "action.knight.toFinish",
        "/knight/setting",              "action.knight.setting",
        "/knight/reply/(.*)",           "action.knight.reply",
        "/knight/delreply/(.*)",        "action.knight.delreply",
        "/knight/setting/add",          "action.knight.addknight",
        "/knight/setting/up/(.*)",      "action.knight.upadmin",
        "/knight/setting/del/(.*)",     "action.knight.delknight",
        "/knight/delfile",              "action.knight.delfile",

        "/eggs",                        "action.user.eggs",)