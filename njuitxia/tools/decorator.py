#!/usr/bin/env python
# coding: utf-8

'''
Created on 2015-1-7

@author: LC
'''

from flask import redirect
from server import UserServer

def check_admin(func):
    def wrapper(*args, **kwargs):
        if (UserServer.checkInfo() == 'admin'):
            return func(*args, **kwargs)
        else:
            return redirect("/")
    return wrapper

def check_knight(func):
    def wrapper(*args, **kwargs):
        info = UserServer.checkInfo()
        if (info == 'knight' or info == 'admin'):
            return func(*args, **kwargs)
        else:
            return redirect("/")
    return wrapper

def check_helper(func):
    def wrapper(*args, **kwargs):
        info = UserServer.checkInfo()
        if (info == 'helper'):
            return func(*args, **kwargs)
        else:
            return redirect("/")
    return wrapper
