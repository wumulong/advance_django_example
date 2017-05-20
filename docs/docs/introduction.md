# 进阶 Django 教程
![Language](https://img.shields.io/badge/language-Python-blue.svg?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)


## requirement.txt

### avatar-generator need some tweak

[avatar-generator](https://github.com/maethor/avatar-generator)

pip version is broken, use git version.

```shell
pip install git+https://github.com/maethor/avatar-generator.git
```


## Django 常用库

* Celery 任务队列 定时任务 远程执行。每天获取 Upslash 最新图片，定时获取服务器监控信息，商品信息爬虫
* django-rq 另一个任务队列
* 简单定时任务 django-crontab
* 商品属性搜索应用 django-elasticsearch
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


