#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-6-11

@author: ZAK
'''
from flask import Flask
from flask.ext.mysqldb import MySQL

'''
数据库参数
'''
saedb = sae.const.MYSQL_DB
saeuser = sae.const.MYSQL_USER
saepw = sae.const.MYSQL_PASS
saehost = sae.const.MYSQL_HOST
saeport = int(sae.const.MYSQL_PORT)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = saeuser
app.config['MYSQL_DATABASE_PASSWORD'] = saepw
app.config['MYSQL_DATABASE_DB'] = saedb
app.config['MYSQL_DATABASE_HOST'] = saehost
app.config['MYSQL_DATABASE_PORT'] = saeport
mysql.init_app(app)

conn = mysql.connection()
cur = conn.cur()
'''
本地jquery,bootstrap文件
'''
basefile1 = web.storage(
   bs_js = "/static/base/bootstrap.min.js",
   bs_css = "/static/base/bootstrap.min.css",
   jq = "/static/base/jquery.min.js")

'''
最新jquery,bootstrap文件
'''
basefile2 = web.storage(
   bs_js = "http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js",
   bs_css = "http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css",
   jq = "http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js")

basefile = basefile2

web.template.Template.globals['config'] = config
web.template.Template.globals['basefile'] = basefile

'''
make qiniu token to post form
'''
import qiniu.conf
qiniu.conf.ACCESS_KEY = "51ksljf2Ej7CoI5uL5dJWLho-yQQ_XnEptc8_wpv"
qiniu.conf.SECRET_KEY = "EBGm1DhcnSmrpkenVCmmn4JIPfRBLEoZ2JPrmh6j"

import qiniu.rs
bucketName = "lcdisk"
@app.context_processor
def inject_webDistUrl():
    return dict(webDiskUrl = 
        "http://7xiyaj.com1.z0.glb.clouddn.com"
        
policy.returnUrl = "http://itxiatest.sinaapp.com"
qiniu_token = policy.token()
@app.context_processor
def inject_token():
    return dict(token = qiniu_token)

version = "2.3"
@app.context_processor
def inject_version():
    return dict(version = version)