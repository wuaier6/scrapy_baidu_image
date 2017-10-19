# baidu image scrapy
通过scrapy3.6 爬取百度图片 


## 运行环境
安装 python3  and mongodb 数据库

```
$ pip install -r requirements.txt
```


## 执行

 修改爬取关键字

> /JiashanRencai/spiders/baiduimage.py

```
pages = 100
keywords = list(set(['日本人']))
```

```
$ python3 main.py
```

