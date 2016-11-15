# coding:utf-8
import requests
import json
from qiniu import put_file
import time
import random
import hashlib


class API_1_1(object):
    base_url = 'http://127.0.0.1:5000/api/v1_1'

    def __init__(self):
        self.headers = {}
        self.token = None
        self.qiniu_token = None
        self.qiniu_key = None
        self.qiniu_base_url = 'http://ogkkyym4h.bkt.clouddn.com/'


    def login(self, phone_number, password, path='/client/login'):
        random_str = str(random.randint(10000, 100000))
        time_stamp = str(int(time.time()))
        s = hashlib.sha256()
        s.update(password)
        s.update(random_str)
        s.update(time_stamp)
        encryption_str = s.hexdigest()

        payload = {'phone_number': phone_number, 'encryption_str': encryption_str, 'random_str': random_str, 'time_stamp': time_stamp}
        self.headers = {'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        self.token = response_data.get('token')
        print json.dumps(response_data, ensure_ascii=False, indent=4)
        return response_data


    def client(self, path='/client'):
        self.headers = {'token': self.token}
        response = requests.get(url=self.base_url + path, headers=self.headers)
        response_data = json.loads(response.content)
        print json.dumps(response_data, ensure_ascii=False, indent=4)
        return response_data


    def logout(self, path='/client/logout'):
        self.headers = {'token': self.token}
        response = requests.get(url=self.base_url + path, headers=self.headers)
        response_data = json.loads(response.content)
        print json.dumps(response_data, ensure_ascii=False, indent=4)
        return response_data


    def get_qiniu_token(self, path='/client/get-qiniu-token'):
        response = requests.get(url=self.base_url + path)
        response_data = json.loads(response.content)
        self.qiniu_token = response_data.get('token')
        self.qiniu_key = response_data.get('key')
        localfile = '1.png'
        ret, info = put_file(self.qiniu_token, self.qiniu_key, localfile)
        print info.status_code
            if info.status_code == 200:
                print '上传成功'
                self.head_picture = self.qiniu_base_url + self.qiniu_key
                print '其url为:' + self.head_picture.encode('utf-8')
            else:
                print '上传失败'
        return response_data


    def set_head_picture(self, path='/client/set-head-picture'):
        payload = {'head_picture': self.head_picture}
        self.headers = {'token': self.token, 'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data


    def register_step_1(self, phone_number, path='/client/register-step-1'):
        payload = {'phone_number': phone_number}
        self.headers = {'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data


    def register_step_2(self, phone_number, validate_number, path='/client/register-step-2'):
        payload = {'phone_number': phone_number, 'validate_number': validate_number}
        self.headers = {'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data


    def register_step_3(self, phone_number, password, password_confirm, path='/client/register-step-3'):
        payload = {'phone_number': phone_number, 'password': password, 'password_confirm': password_confirm}
        self.headers = {'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data


    def register_step_4(self, phone_number, email, path='/client/register-step-4'):
        payload = {'phone_number': phone_number, 'email': email}
        self.headers = {'content-type': 'application/json'}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data
      
        
    def get_multi_qiniu_token(self, count, path='/get-multi-qiniu-token'):
        self.headers = {'token': self.token}
        payload = {'count': count}
        response = requests.get(url=self.base_url + path, params=payload, headers=self.headers)
        response_data = json.loads(response.content)
        key_token_s = response_data.get('key_token_s')
        return key_token_s


    def post_form(self, campus, machine_model, OS, description, picture_files, path='/client/forms/post'):
        self.headers = {'token': self.token}
        count = len(picture_files)
        
        pictures = []
        if count != 0:
            key_token_s = self.get_multi_qiniu_token(count=count)
        
            for i in range(count):
                put_file(key_token_s[i]['token'], key_token_s[i]['key'], picture_files[i])
                pictures.append(self.qiniu_base_url + key_token_s[i]['key'])

        payload = {'campus': campus, 'machine_model': machine_model, 'OS': OS, 'description': description, 'pictures': pictures}
        self.headers = {'content-type': 'application/json', 'token': self.token}
        response = requests.post(url=self.base_url + path, data=json.dumps(payload), headers=self.headers)
        response_data = json.loads(response.content)
        print response_data.get('message')
        return response_data


    def get_forms(self, path='/client/forms'):
        self.headers = {'token': self.token}
        payload = {}
        response = requests.get(url=self.base_url + path, params=payload, headers=self.headers)
        response_data = json.loads(response.content)
        print json.dumps(response_data, ensure_ascii=False, indent=4)
        return response_data

if __name__ == '__main__':
    api = API_1_1()
    api.login('15850551103', '123456')
#    api.get_multi_qiniu_token(2)
#    api.post_form('xianlin', 'mac', 'win', 'sjfjjsklj',['1.png', '2.png'])
#    api.client()
    api.get_forms()
    #api.logout()
#    api.register_step_1('15850551102')
#    validate_number = input("Please input the validate_number in message:\n")
#    api.register_step_2('15850551102', str(validate_number))
#    api.register_step_3('15850551102', '1234567', '1234567')
#    api.register_step_4('15850551102', '2214102@qq.com')
    #api.get_qiniu_token()
    #api.set_head_picture()
    #api.logout()
