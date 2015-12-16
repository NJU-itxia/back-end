#NJU-ITXia

!!! 安装最新版的 eve
```
pip install git+git://github.com/nicolaiarocci/eve.git
```

* RESTFul API design and implementation.
* NoSQL database.
* User management: user roles, authentication and authorization.
* Frontend framework.
* Web deploying and hosting.

## 代码规范

* 所有代码文件使用 UTF-8 编码。
* Python 代码遵从 PEP8 规范。
* HTML, JavaScript, CSS 代码缩进为 2 个空格。

## 本机部署和测试方法
* 安装 virtualenv, virtualenvwrapper
* 安装 MongoDB
* 安装所需的库 pip install -r requirements.txt
* 进入 njuitxia/API 文件夹，终端输入 python api.py 启动 API 服务。
* 进入 njuitxia/API 文件夹，终端输入 py.test 运行测试。
