# ToDoList
个人任务卡

本项目是一个基于前后端分离技术的个人任务卡，后台url设计风格遵循restful风格，主要功能有添加新任务、删除任务、修改任务等。后台url设计风格遵循restful风格。

前端开发语言：html5 css3 javascript（es6）前端开发语言：python3.6

前端使用框架：bootstrap4       
后端使用框架：django1.11

数据库：mysql5.7

#创建项目
1.使用命令行开始一个新项目
```
django-admin startproject ToDoList
```
2.创建应用app
```
python manage.py startapp list
```
#代码结构
```
ToDoList //文件夹
    |--list //app目录
    |   |--migrations //数据库迁移的记录
    |   |--admin.py
    |   |--apps.py
    |   |--forms.py
    |   |--models.py //数据库表模型
    |   |--tests.py //测试代码
    |   |--views.py //处理业务逻辑的函数
    |--ToDoList 
    |   |--settings.py //全局配置信息
    |   |--urls.py //总路由，请求地址跟视图函数的映射
    |   |--wsgi.py
    |--manage.py //项目入口，执行一些命令
```


#使用方式
1.安装配置Django框架
```
pip install django==1.1.18
```
2.修改数据库连接配置
将settings.py中的数据库配置信息替换成自己的本地数据库信息。

3.在包含`manage.py`的文件目录下运行如下命令生成数据表
```
python manage.py makemigrations
python manage.py migrate
```
4.在命令行输入如下命令，启动服务
```
python manage.py runserver
```
5.在浏览器窗口输入 http://127.0.0.1:8000/即可运行web项目。