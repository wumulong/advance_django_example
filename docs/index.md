# Django 进阶教程

![Language](https://img.shields.io/badge/language-Python-blue.svg?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

[Django](https://www.djangoproject.com/) 是一个有着十二年历史的 Python Web 框架，是 Python Web 开发中最流行的框架。因为 Python 容易上手的特性，有大量的第三方库，能够快速开发，也能够获得非常好的稳定性和性能，MVC 的设计也非常用以理解，所以新手选择 Django 作为一个启蒙框架是非常适合的。尽管我后来学了 Node.js, Rails 等等，但我依然记得 Django 就是我的第一个学习的 Web 开发框架，因 Django 可插拔 App 这一特性给我留下了很深的印象。



虽然 Django 架构的大型网站和服务也不少，像 [Instagram](https://engineering.instagram.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad) 就是一个以 Django 为基础的大型应用。国内的例子就很少，因为国内本身使用 Python 的公司就很少，很多都是用在运维方面，爬虫方面，各个公司可能会基于一些开源项目开发内部使用的自动化运维平台，因为自动化运维基本都是用 shell, Python 的各种开源库，所以用 Django 也是最佳选择。



我写的这篇教程不包含基础的 Django 内容，也不包含基础的 Python 内容，Python 和 Django 都是使用的最新的，分别是 3.6.1 和 1.11。基础的 Django 教程可以去很多地方找到教程，CRUD 看看官方文档的 Tutorial 就能上手了，英文够好的话看文档是最佳选择，因为文档里面也包含了很多的示例代码。



这篇教程包含了使用 Django 在 Web 开发中遇到的常见问题的解决方案，包含了简单的示例应用，总共分为三部分，第一部分是任务队列和搜索，第一章到第四章；第二部分是两个实战 App 的 视图及 API 实现，API 实现有两种，一种是常见的 RESTFul，还有一种是 GraphQL，穿插介绍了打标签和信息流这两个库，第五章到第八章；第三部分是本地开发辅助工具 django-debug-toolbar 和 django-extensions，前端结合 Webpack，以及接入 Sentry 异常捕获服务，结合 Ansible 在本地进行自动化部署 Django 应用，包含 CLI 和 GUI 实现，最后会对 API 进行一个 Benchmark，第九章到第十二章。



详细的目录在项目中的 GitHub Pages 能看到，GitHub Pages 是用的 [MkDocs](http://mkdocs.org) 生成的，用了一个 Material Design 的主题，字体是 Souce Sans Pro 和 Source Code Pro，还挺好看，可读性也不错，目录、TOC 都有，还有 GFM 的语法，想直接读阅读 GitHub 渲染的 md 文件可以直接到 `docs` 目录打开文件。README 中我就不放目录了，简单介绍下这个教程中涉及到了那些内容，有那些示例。



## 任务队列/定时任务

任务队列将介绍两个库的使用，一个是功能比较多的 [Celery](http://docs.celeryproject.org/en/latest/index.html)，另一个是功能较为简单的 [django-rq](https://github.com/ui/django-rq)，Celery 提供了非常易用的 API 来实现任务队列和定时任务，用 django-rq 实现定时任务则需要手动实现定时入队这一过程，当然如果你只需要简单的定时任务的话 [django-corntab](https://github.com/kraiz/django-crontab) 也是一个非常好的选择。



## 搜索

ElasticSearch 也是一个在 Web 应用中经常使用的东西，一个搜索引擎后端，被用来索引复杂数据，如商品属性数据，或者用来处理大量日志，教程中也包含了如何在 Django 中使用 [django-elasticsearch](https://github.com/liberation/django-elasticsearch) 这个库的示例。



## API

Django 有一个非常方便使用的 RESTFul API 库，叫做 [Django REST framework](http://www.django-rest-framework.org)，只要定义好 model，serializer，在根据业务写好视图层的代码，加上 [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/) 作为 API token 保护，就能提供一个完整的 API 后端服务。示例代码中也包含了一个简单的用户应用（登录注册）的视图层和 API 层实现，包含了基本的功能，登录注册、修改资料、修改密码、删除账户，全部提供了 RESTFul API 实现，另外也包含了这个用户 App 的 GraphQL 实现。



## 图片处理

图片处理也是 Web 开发中很常见的需求，用户上传的头像、图片可能很大，需要裁剪，需要处理成大中小尺寸和略缩图来保存，以方便不同页面的展示。教程中包含了简单用户注册是给表单添加一个验证码，防止应用被恶意爬虫盯上进行垃圾用户注册，也简单介绍了用 django-imagekit 进行图片处理。



## 本地开发辅助

介绍了两个本地开发辅助工具：django-debug-toolbar 和 django-extensions，django-debug-toolbar 能在本地测试的时候页面右侧有个可隐藏的面板，看到一些调试信息，应用变量、SQL 执行时间、模板文件、运行时间等等。django-extensions 给 Django 应用的 manage.py 添加了命令，比如查看应用的全部 URL 和对于的方法，可视化应用的 model，验证模板等等。



## 前端结合

前端结合介绍了一个非常神奇的包，让 Django 应用也能获得非常接近单页应用的用户体验，来自 Rails 社区的 [Turbolinks](https://github.com/turbolinks/turbolinks)，有人根据 Django 的 middleware 原理开发了适合 Django 的包，非常容易接入，就能让 Django 应用使用体验大变样。还介绍了一个 Django 结合 Webpack 的工具，Webpack 是现在前端最流行的打包工具，用来打包全部前端内容，CSS/JS/字体/图片，我也使用过 Django 的一些前端辅助工具，就是把全部 JS 和 CSS 拼接成一个文件然后 minifier，JS 还要在 uglify 混淆，其实都不太好用，还不如我自己写个 gulpfile。



## 接入 Sentry 和部署问题

最后介绍了如何接入 Sentry，Python 这样的动态语言，没有类型，要在运行时才会报错，很难在最开始就把代码中的异常处理都考虑到，所以就需要 Sentry 这样的捕获工具。作为一个『全干』工程师，部署应用，服务器 trouble shotting 也是一项必须掌握的技能。其实 Django 非常容易部署，只要选对了发行版，我对比下来用 Ubunt 是最方便的，环境问题最少，熟练的话从启动服务器到完成二十分钟就能搞定。
