# djangotest
一：创建Django项目框架：
* 执行django-admin startproject mblog
* 运行python manage.py runserver，此时可以通过本地浏览器访问localhost:8000即可看到django成功的画面。
(本次在腾讯云服务器centos7系统下直接创建项目，需要先对外开启服务器的8000端口,
再在settings.py中设置allowed_hosts=[' * '],
然后runserver 0.0.0.0:8000,这样才可以在外网访问ip:8000)
* 创建app,python manage.py startapp mainsite
* 创建git文库
>git init

>git add .

>git commit -m 'first commit'

>git remote add origin https://github.com/namex/x.git （如果出现已存在错误,先执行git remote rm origin）

>git pull(提交之前先进行更新，如果发生错误，执行git pull origin master --allow-unrelated-histories)

>git push -u origin master（如果出现error，注意是否没有pull导致的）

* 在setting.py里更改时区信息，增加app信息。即install_apps中增加'mainsite',设置language_code='zh-Hans',time_zone='Asia/Shanghai'
* 创建数据库python manage.py migrate
以上即为搭建了django项目框架。

二：创建博客数据表
* mainsite/models.py中增加models Post。然后执行python manage.py makemigrations mainsite记录数据库改动。
最后执行python manage.py migrate提交数据库更新
* 创建管理员账号密码python manage.py createsuperuser
* 新增管理模型Post,修改mainsite/admin.py，导入并注册Post
* runserver，然后浏览器打开*/admin页面，登录django管理后台
* 手动增加Post内容后，修改mainsite/views.py
* 修改urls.py
* 创建模板template
