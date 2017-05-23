## 安装 requirements.txt 中的第三方库

因为这个教程用到了挺多东西，但都非常容易在本地下载了跑起来，首先是数据库用的是 PostgreSQL，任务队列用到了 Redis，其他的话可能 requirements.txt 中的某些库在不同环境下可能会出现问题，在 macOS 上使用 Python3 都能安装成功，我就不在这里详细写了，全部安装完成后需要有两个 GUI 客户端方便看数据库，PostgreSQL 我用的是 [Postico](https://eggerapps.at/postico/)，Redis 用的是 [Medis](http://getmedis.com/)。

```shell
# clone code and install pip packages
git clone https://github.com/lsdlab/advance_django_example
cd advence_django_example
pip install -r requirements.txt
```



## 启动本地开发服务

项目在 conf 文件夹下将 prodution 和 development 环境的配置进行了区分，使用 python-dotenv 读取 .env 文件，获得项目的 secret_key、数据库用户名密码等等。

启动了本地的 PostgreSQL 和 Redis 服务后，手动新建一个数据库，进入项目文件夹下，运行 `python manage.py migrate --settings=conf.development.settings`，进行数据库迁移，然后运行 `python manage.py runserver 0.0.0.0:8000 --settings=conf.development.settings`，浏览器打开 `localhost:8000` 就能看到首页了。