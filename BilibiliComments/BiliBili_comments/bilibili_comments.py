import requests  # 导入数据请求模块
from datetime import datetime  # 导入日期转换模块
import csv  # 导入csv模块
import hashlib  # 导入哈希模块
import json  # 导入序列化模块
from urllib.parse import quote  # 导入编码的方法
import time  # 导入时间模块
import random  # 添加随机延迟

from data_stats import data_statistics

"""
B站评论数据采集脚本
通过调用B站评论接口，获取并解析弹幕数据，最后保存到CSV文件中
该脚本主要用于批量采集B站视频的评论数据，支持多页翻页采集，并将结果保存为结构化的CSV文件，便于后续分析和处理。
"""

"""
1. 分析数据
        浏览器抓包分析或者使用B站自维护的访问接口获取，接口获取见readme
2. 发送请求
        使用请求头模式
3. 获取数据
        签名算法（MD5解密）
4. 解析数据
        正则匹配：使用正则匹配和字典操作提取评论的关键信息，包括用户昵称、性别、地区、评论内容、点赞数等。
5. 保存数据
        csv:将提取的评论数据保存到CSV文件中，支持多页数据的追加写入，便于后续数据分析。
"""


def get_sign(now_time, next_page):
    """获取签名"""
    pagination_str = '{"offset":%s}' % next_page

    """获取加密参数w_rid"""
    params = [
        "mode=2",
        "oid=841786906",
        f"pagination_str={quote(pagination_str)}",
        "plat=1",
        "type=1",
        "web_location=1315875",
        f"wts={now_time}"
    ]
    string = '&'.join(params) + 'ea1db124af3c7062474693fa704f4ff8'
    w_rid = hashlib.md5(string.encode('utf-8')).hexdigest()
    # 打印显示每一页匹配的参数变化
    print(f"w_rid动态参数:{w_rid}")
    return w_rid, pagination_str


def get_comments(next):
    """获取评论核心方法"""
    # 模拟浏览器 cookie必须要加/不加登陆账号的cookie获取不到IP属地
    headers = {
        # cookie信息检测是否有登录账号
        "cookie": cookie,
        "user-agent": user_agent,
        "referer": video_url,
    }
    # 请求网址(b站评论的api)
    url = 'https://api.bilibili.com/x/v2/reply/wbi/main'

    # 获取时间戳
    now_time = int(time.time())
    # 获取加密参数
    w_rid, pagination_str = get_sign(now_time=now_time, next_page=next)

    # 查询参数 (在载荷中复制) 按最热排列
    params = {
        'oid': '841786906',
        'type': '1',
        'mode': '2',
        'pagination_str': pagination_str,
        'plat': '1',
        'web_location': '1315875',
        'w_rid': w_rid,
        'wts': now_time
    }

    # # 使用代理IP
    # proxies = {
    #     'http': 'http://192.168.1.1:port',
    #     'https': 'https://your_proxy_ip:port'
    # }

    # 发送请求
    response = requests.get(url=url, params=params, headers=headers)
    # time.sleep(random.uniform(3, 6))  # 添加请求时延
    response.raise_for_status()
    print(f"请求响应状态码：{response.raise_for_status()}")  # 响应为空

    # 添加响应状态检查
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None

    """获取数据"""
    # 获取响应的json数据
    json_data = response.json()
    print(json_data)

    global retry_count  # 声明使用全局变量

    # 检查API返回的错误码
    if json_data.get('code') != 0:
        print(f"API返回错误: {json_data.get('message')}")
        retry_count += 1
        print(f"错误请求{retry_count}")
        if retry_count >= 3:
            print("达到最大重试次数，退出程序")
            exit()
        return None

    if 'data' not in json_data:
        print("响应中缺少data字段")
        return None

    """解析数据"""
    # 字典取值, 提取评论信息所在列表
    replies = json_data['data']['replies']
    # for循环遍历, 提取列表里面的元素
    for index in replies:
        """提取具体每条评论信息"""

        ctime = index['ctime']  # 提取评论时间戳
        date = str(datetime.fromtimestamp(ctime))  # 把时间戳转成日期
        dit = {  # 提取main请求响应回来需要的数据
            '昵称': index['member']['uname'],
            '性别': index['member']['sex'],
            '地区': index['reply_control']['location'].replace('IP属地：', ''),
            '日期': date,
            '评论': index['content']['message'],
            '点赞': index['like'],
        }
        # 写入数据
        global_csv_writer.writerow(dit)
        print(dit)
    # 获取下一页参数 offset参数
    next_offset = json_data['data']['cursor']['pagination_reply']['next_offset']
    return json.dumps(next_offset)


def save_csv(filename):
    """保存评论数据到CSV文件"""
    global global_csv_writer
    # 创建文件对象 如果使用utf-8出现乱码 -> utf-8-sig
    f = open(filename, mode='w', encoding='utf-8', newline='')
    # 字典写入方法
    global_csv_writer = csv.DictWriter(f, fieldnames=[
        '昵称',
        '性别',
        '地区',
        '日期',
        '评论',
        '点赞',
    ])
    # 写入表头
    global_csv_writer.writeheader()

    offset = '""'
    # 构建循环翻页
    for page in range(1, 30):
        print(f'正在采集第{page}页的数据内容')
        offset = get_comments(next=offset)


if __name__ == '__main__':
    cookie = ("buvid3=B25FEA33-6B46-3C5E-A18A-C3E53763A9F932854infoc; b_nut=1747320632; "
              "_uuid=35A716DE-7109E-2293-9FF4-225FB6A5699234883infoc; CURRENT_FNVAL=4048; "
              "buvid4=F173D692-E496-759E-5D4E-88E0938645B834679-025051522-LAQ2E/2AzFkNNYOyQ++fIQ%3D%3D; rpdid=|("
              "JY~|lk~)R)0J'u~R~Jk|YJR; "
              "SESSDATA=adedc65e%2C1762922652%2C49cf3"
              "%2A51CjDY4gBlocko40Qwo16KhMaFvccww4rFFKeNCURUEN9hEBlD2t_0Zj92oPECNZBWwF8SVnBhQ1NxQUFkUkk1clJ3WUp0QXR3MEJ"
              "QSm8xdmJ3dlctUzJOQldXMmp3Qzl4UHJZN1JUcXdfUVRzZ2Jsb2wya2dzaU1xVEJlUGlxd2NLTV9qWVJ0V3ZnIIEC; bili_jct=8fe5"
              "97bfefad11937b62ade21974effe; DedeUserID=473409553; DedeUserID__ckMd5=5a076712a01c326e; fingerprint=d4c2"
              "4c7d411e000b2732c6d26a01f97a; buvid_fp_plain=undefined; buvid_fp=d4c24c7d411e000b2732c6d26a01f97a; bp_t_"
              "offset_473409553=1067817522205556736; b_lsid=D14B9A2B_196DD52284E; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZ"
              "CI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDc3MzI2MjEsImlhdCI6MTc0NzQ3MzM2MSwicGx0IjotMX0.lQ1Vt_etkTigl3VK"
              "sYIyYvO55TsRNpp_H1NZbjSfJlk; bili_ticket_expires=1747732561; sid=6mbf7u9r")
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 "
                  "Safari/537.36")
    video_url = 'https://www.bilibili.com/video/BV1x54y1e7zf'

    global_csv_writer = None
    retry_count = 0

    save_csv('comments.csv')
    data_statistics('comments.csv')
