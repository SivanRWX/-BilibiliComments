# BilibiliComments

B站评论与弹幕爬虫，提供爬取 Bilibili 视频评论数据和Bilibili弹幕数据，支持数据存储、词云生成及可视化分析。



## 概况

### 1.B站评论爬虫

基于 Python 的爬虫工具，用于从 Bilibili 视频中抓取评论数据。通过调用 Bilibili 的评论 API，解析返回的 JSON 数据，并将评论数据保存为结构化的 CSV 文件，便于后续分析和处理。

#### 操作流程

1.数据采集： 
通过 HTTP 请求获取 Bilibili 评论数据。
支持多页翻页采集，自动处理分页逻辑。
使用签名算法生成必要的加密参数。
2数据处理： 
提取评论的用户昵称、性别、地区、评论内容、点赞数等关键信息。
将时间戳转换为可读的日期格式。
3.数据保存： 
将采集到的评论数据保存为 CSV 文件，支持多页数据的追加写入。
4.错误处理： 
检查 API 返回的状态码和错误信息，支持重试机制。

#### 使用方法

1.配置参数： 
修改脚本中的 cookie、user_agent 和 video_url 变量，填写您的 Bilibili 账号信息和目标视频的 URL。
2.运行脚本： 执行以下命令运行脚本： 
python bilibili_comments.py
3.输出结果： 
生成的 CSV 文件：comments.csv，包含评论数据。



### 2.B站弹幕爬虫

基于 Python 的爬虫工具，用于从 Bilibili 视频中抓取弹幕数据。通过调用 Bilibili 的弹幕 API，解析 Protobuf 格式数据，并对弹幕数据进行可视化和统计分析。

#### 操作流程

1.数据采集
通过 HTTP 请求获取 Bilibili 弹幕数据。
使用 Protobuf 反序列化解析弹幕内容。
将弹幕数据保存为 CSV 文件。
2.数据处理：
提取弹幕的时间戳、内容和发布时间。
将时间戳转换为可读的时间格式。
3.数据可视化：
生成弹幕内容的词云图。
统计并可视化弹幕的时间分布（按分钟和小时）。

#### 使用方法

1.配置参数：
修改脚本中的 cookie、user_agent 和 video_url 变量，填写您的 Bilibili 账号信息和目标视频的 URL。
确保 oid 参数与目标视频的 ID 匹配。
2.运行脚本： 执行以下命令运行脚本： 
python bilibili_barrages.py
输出结果： 
3.生成的 CSV 文件：barrages.csv，包含弹幕数据。
4.可视化结果：
wc.png：弹幕内容的词云图。
minute_barrage_counts.png：按视频分钟时段统计的弹幕数量柱状图。
hourly_barrage_counts.png：按小时统计的弹幕数量柱状图。





## 文件介绍

#### BiliBili_comments		——B站评论父目录

- [bilibili_comments.py](BiliBili_comments\bilibili_comments.py) 								——使用requests网络请求方法的爬虫代码

- [bilibili_comments_useDrissionPage.py](BiliBili_comments\bilibili_comments_useDrissionPage.py)   ——使用DrissionPage模拟浏览器方法的爬虫代码（未完全实现）

-  [data_stats.py](BiliBili_comments\data_stats.py)                                             ——数据分析模块，包括可视化地区评论数分布，性别分析（控制台输出），评论关键词top10分布，点赞数分析（平均，最高，中位），评论时间趋势分布

- [comments.csv](BiliBili_comments\comments.csv)                                             ——评论数据存储文件

- [comments.db](BiliBili_comments\comments.db)                                              ——本地存储database

- [comments.sql](BiliBili_comments\comments.sql)                                             ——数据库结构导出文件

- area_distribution.png                               ——可视化地区分布

- time_distribution.png                                ——评论时间分布

- word_frequency.png                                 ——评论高频词汇top10

- wc.png                                                          ——生成的词云图

  

#### BiliBili_barrages		   ——B站视频弹幕父目录

- [bilibili_barrages.py](Bilibili_barrages\bilibili_barrages.py)                                  ——使用requests网络请求方法，数据抓包的爬虫代码，也有数据分析

- [dm_pb2.py](Bilibili_barrages\dm_pb2.py)                                                ——b站弹幕数据解码文件（download)

- [barrages.csv](Bilibili_barrages\barrages.csv)                                                ——生成弹幕文件

- hourly_barrage_counts                              ——弹幕发布时间时分图

- minute_barrage_counts                            ——弹幕所在时间片段分布图

  





## 采集信息

### 使用开发者工具，网络请求方式抓包

#### 评论

B站开放评论API接口：https://api.bilibili.com/x/v2/reply/wbi/main

网页内获取载荷内参数，观察有两个可变参数w_rid,wts其为bilibili加密算法处理的重要对象，经过后续访问js文件定位

```
pagination_str 直接搜这个参数是否存在某个数据包返回，下一个参数是来自上一页返回的响应数据（页面跳转）
w_rid   加密参数（在网页工具搜索中唯一） 使用JS逆向+断点调试
wts 时间戳		可以time模块获取当前时间戳
```



![QQ20250518-215242](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-215242.png)



![QQ20250518-211132](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-211132.png)





![QQ20250518-215817](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-215817.png)

**MD5加密**

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-220019.png)



#### 弹幕

通过在视频网页地址bilibili域前面加一个i可以跳转到本页面，在视频底下快速获取弹幕地址（快捷方式）

点击弹幕地址：https://api.bilibili.com/x/v1/dm/list.so?oid=226204073

![QQ20250518-151100](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-151100.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-151523.png)



抓包方式：

F12进入浏览器开发者模式，点击网络面板，点开弹幕列表，搜索栏输入seg.so抓该名称的包，在请求头获取请求地址

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-161318.png)





## 需求库安装(pip install)



| 模块名          | 模块含义                                 |
| --------------- | ---------------------------------------- |
| requests        | 数据请求模块                             |
| datetime        | 日期转换模块                             |
| csv             | csv模块                                  |
| hashlib         | 哈希模块 MD5解密                         |
| json            | json模块   序列化                        |
| urllib.parse    | 编码方法的模块(quote将字符串进行url编码) |
| time            | 时间模块                                 |
| pandas          | 数据处理模块                             |
| jieba           | 分词模块（词云图使用）                   |
| wordcloud       | 词云图模块                               |
| matplotlib      | 数据可视化模块                           |
| random          | 随机模块                                 |
| re              | 正则表达式模块                           |
| google.protobuf | 二进制序列化协议                         |
| dm_pb2          | b站弹幕解密文件                          |



![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250518-175255.png)



## 运行界面

#### 弹幕

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211402.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211418.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250520-092929.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250520-092934.png)



#### 评论

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211743.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211451.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211500.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211505.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211510.png)

![](E:\PyCharm2023.3pro\MyProject\Normal\BilibiliComments\img\QQ20250519-211515.png)