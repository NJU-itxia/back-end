# -*- coding: utf-8 -*-
import json
import requests

API_URL = 'http://localhost:5000/'


def get_url(r):
    '''Concatenate API_URL and resource name'''
    return API_URL + r


def test_get_all_orders():
    '''Test if server if up and if server can response orders'''
    url = get_url('orders')
    assert requests.get(url).status_code == 200


def test_post_orders():
    url = get_url('orders')
    data = {
        "phone_number": "18613377064",
        "name": u"测试",
        "description": "description",
        "machine_model": "MacBook Pro with Retina Display",
        "campus": "gulou",
    }
    assert requests.post(url, json=data).status_code == 201
