# back-end
##安装python依赖  
`$ pip install -r requirements.txt`

##设置数据库  
```
$ sudo apt-get install mysql
$ mysql -u root -p
mysql> create user 'itxiadb'@localhost identified by 'secret_password'
mysql> create database apidb character set utf8;
mysql> grant all on apidb.* to 'itxiadb'@localhost;
mysql> exit
```
```
$ sudo apt-get install redis
$ redis-cli
127.0.0.1:6379> CONFIG SET requirepass secret_password
127.0.0.1:6379> QUIT
```
```
$ python manage.py db init //如果没有migrations文件则运行此行
$ python manage.py db migrate -m "add new" // 当数据库模型改变时(model.py)要再次运行此行以及下一行更新
$ python manage.py db upgrade     
$ python manage.py testdb //向数据库导入测试数据
```
##运行服务器
```
$ python manage.py runserver        
```
##测试API
```
$ python client_test.py //测试api，用注释的方式禁止一部分代码运行 
