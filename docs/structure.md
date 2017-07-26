# 项目结构

```
├─ config.rb  #指定额外的compass插件
├─ config.ru
├─ Rakefile   #rake的配置文件,类似于makefile 添加Tag 功能后要自动在编辑每篇Blog 时自动在前面添加tags: 提示
├─ Gemfile    #bundle要下载需要的gem依赖关系的指定文件
├─ Gemfile.lock  #这些gem依赖的对应关系,比如A的x版本依赖于B的y版本
├─ _config.yml   #站点的配置文件
├─ public/    #在静态编译完成后的目录,网站只需要这个目录下的文件树
├─ _deploy/   #deploy时候生成的缓存文件夹,和public目录一样
├─ sass/      #css文件的源文件,过程中会compass成css
├─ plugins/   #放置自带以及第三方插件的目录,ruby程序
│   └── xxx.rb
└─ source/    #站点的源文件目录,public目录就是根据这个目录下数据生成的
   └─ _includes/
      └─ custom/      #自定义的模板目录,被相应上级html include
         └─ asides/   #边栏模板自定义模板目录
      └─ asides/      #边栏模板目录
      └─ post/        #文章页面相应模板目录
   └─ _layouts/       #默认网站html相关文件,最底层
   └─ _posts/         #新增以及从其它程序迁移过来的数据都存在这里
   └─ images/         #图片目录 可手动添加，添加后Blog 应用图片可直接从这个文件中引用
└─ README.markdown    #octopress 说明
└─ CHANGELOG.markdown    # octopress 更新说明
```

