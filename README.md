# 进阶 Django 教程
![Language](https://img.shields.io/badge/language-Python-blue.svg?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

[Django](https://www.djangoproject.com/) 是一个有着十二年历史的 Python Web 框架，是 Python Web 开发中最流行的框架。因为 Python 容易上手的特性，能够快速开发，也能够获得非常好的稳定性和性能，MVC 的设计也非常用以理解，所以新手选择 Django 框架作为一个启蒙是非常好的，尽管我后来学了 Node.js, Rails 等等，但我依然记得 Django 就是我的第一个学习的 Web 开发框架。



虽然 Django 架构的大型网站和服务也不少，像 Instgram 就是一个以 Django 为基础的大型应用。国内很少，因为国内本身使用 Python 的公司就很少，很多都是用在运维方面，爬虫方面，各个公司可能会基于一些开源项目开发内部使用的自动化运维平台，因为自动化运维基本都是用 shell, Python 的各种开源库，所以用 Django 也是最佳选择。



我写的这篇教程不包含基础的 MVC 知识，基础的 Django 开发可以去很多地方找到教程，英文够好的话看文档是最佳选择，因为文档里面也包含了很多的示例代码。

这篇教程包含了使用 Django 在 Web 开发中遇到的常见问题的解决方案，也包含了示例应用。比如任务队列，定时任务，任务队列将介绍两个库的使用，一个是功能比较多的 Celery，另一个是功能较为简单的 django-rq，Celery 提供了非常易用的 API 来实现任务队列和定时任务，用 django-rq 实现定时任务则需要手动实现定时入队这一过程，当然如果你只需要简单的定时任务的话 django-corntab 也是一个非常好的选择。图片处理也是 Web 开发中很常见的需求，用户上传的头像、图片可能很大，需要裁剪，需要处理成大中小尺寸和略缩图来保存，以方便不同页面的展示。还有 API，Django 有一个非常方便使用的 RESTFul API 库，叫做 Django REST framework，只要定义好 model，serializer，在根据业务写好视图层的代码，加上 [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/) 作为 API token 保护，就能提供一个完整的 API 后端服务。示例代码中也包含了一个简单的用户应用（登录注册）的视图层和 API 层实现




## requirement.txt

### avatar-generator need some tweak

[avatar-generator](https://github.com/maethor/avatar-generator)

pip version is broken, use git version.

```shell
pip install git+https://github.com/maethor/avatar-generator.git
```


## Django 常用库

* 任务队列 Celery 定时任务 远程执行。每天获取 Upslash 最新图片，定时获取服务器监控信息，商品信息爬虫
* 另一个任务队列 django-rq
* 简单定时任务 django-crontab
* 属性搜索 django-elasticsearch
* RESTful API django-restframework + JWT API 限流 django-ratelimit
* django-simple-captcha and django-imagekit 验证码和图片处理
* 用户模块 API 及页面功能
* HTTP2 nginx Benchmark and API Benchmark
* 本地开发辅助 debug tools: django-debug-toolbar and django-extensions
* django-taggit 打标签
* django-activity-stream 信息流
* 前端结合 webpack django-webpack-loader
* built-in admin panel django-flat-responsive
* 接入 sentry


## celery result backend and custom scheduler
```
python manage.py migrate django_celery_results

# redis result backend
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# database result backend, use django-celery-results
# CELERY_RESULT_BACKEND = 'django-db'

python manage.py migrate django_celery_beat
```


## celery worker and beat
```
redisstart
celery -A advance_django_example  worker --loglevel=info
celery -A advance_django_example  beat --loglevel=info
```


## flower
```
flower -A advance_django_example --basic_auth=lsdvincent:1234
```


