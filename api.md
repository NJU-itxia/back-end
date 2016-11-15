
//調用此api訪問容聯雲，發送要驗證的手機號
```
POST /client/register-step-1
payload = {'phone_number': '15850551102'}
headers = {'content-type': 'application/json'}

response = {'code':1, 'message': '发送成功'}//code表示成功1或者失敗0
           {'code': 0, 'message': '该用户已经存在,注册失败'}
           {'code': 0, 'message': err_message}//err_message容聯雲傳回的錯誤信息
```
//調用此api驗證用戶信息，發送驗證碼和手機號
```
POST /client/register-step-2
payload = {'phone_number': '15850551102', 'validate_number': '454078'}
headers = {'content-type': 'application/json'}

response = {'code': 1, 'message': '短信验证通过'}
           {'code': 0, 'message': '验证没有通过'}
```

//調用此api提交密碼，發送用戶密碼和手機號，只有驗證過的手機號能提交，這裏後端對密碼格式進行檢查
```
POST /client/register-step-3
payload = {'phone_number': '15850551102', 'password': '123456', 'password_confirm': '123456'}
headers = {'content-type': 'application/json'}

response = {'code': 1, 'message': '提交密码成功'}
           {'code': 0, 'message': '密码长度不符合要求'}
           {'code': 0, 'message': '密码和密码确认不一致'}
           {'code': 0, 'message': '验证码没有通过'}
```           

//調用此api完善用戶信息，發送基本資料
```
POST /client/register-step-4
payload = {'phone_number': '15850551102', 'email': '2214102327@qq.com'}
headers = {'content-type': 'application/json'}

response = {'code': 1, 'message': '注册成功'} 
           {'code': 0, 'message': '注册失败'}
           {'code': 0, 'message': '验证码没有通过'}
``` 

//調用此api登錄用戶，發送手機號和token
```
POST /client/login
payload = {'phone_number': phone_number,
           'encryption_str': encryption_str,
           'random_str': random_str,
           'time_stamp': time_stamp}
headers = {'content-type': 'application/json'}
// 這裏是前端對明文的密碼進行處理的方式，與後端約定好
// random_str //隨機數
// time_stamp = str(int(time.time())) //時間戳
// s = hashlib.sha256()
// s.update(password)
// s.update(random_str)
// s.update(time_stamp)
// encryption_str = s.hexdigest() //用sha256方法加密的密碼，後端會做同樣的加密驗證 

response = {'code': 0, 'message': '没有此用户'}
           {'code': 0, 'message': '密码错误'}
           {'code': 1, 'message': '成功登录', 'email': '2214102327@qq.com', 'token': token}
```         
            












