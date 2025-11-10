import requests  # 导入数据请求模块
from datetime import datetime  # 导入日期转换模块
import csv  # 导入csv模块
import hashlib  # 导入哈希模块
import json  # 导入序列化模块
from urllib.parse import quote  # 导入编码的方法
import time  # 导入时间模块
import random  # 添加随机延迟
import os  # 导入系统模块，用于文件路径处理

from data_stats import data_statistics

"""
B站评论数据采集脚本
通过调用B站评论接口，获取并解析弹幕数据，最后保存到CSV文件中
该脚本主要用于批量采集B站视频的评论数据，支持多页翻页采集，并将结果保存为结构化的CSV文件，便于后续分析和处理。
"""

def load_config():
    """加载配置文件"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    
    # 检查配置文件是否存在，不存在则报错
    if not os.path.exists(config_path):
        print(f"错误: 配置文件不存在: {config_path}")
        print("请创建config.json配置文件，包含以下字段:")
        print('{\n    "cookie": "你的cookie",')
        print('    "user_agent": "你的user_agent",')
        print('    "video_url": "视频URL",')
        print('    "video_id": "视频ID"\n}')
        return None
    
    # 读取配置文件
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"配置文件加载成功: {config_path}")
            return config
    except json.JSONDecodeError as e:
        print(f"错误: 配置文件格式错误: {e}")
        return None
    except Exception as e:
        print(f"错误: 加载配置文件失败: {e}")
        return None


def get_sign(now_time, next_page):
    """获取签名"""
    pagination_str = '{"offset":%s}' % next_page

    """获取加密参数w_rid"""
    params = [
        "mode=2",
        f"oid={video_id}",
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
    url = 'https://api.bilibili.com/x/v2/reply/main?'

    # 获取时间戳
    now_time = int(time.time())
    # 获取加密参数
    w_rid, pagination_str = get_sign(now_time=now_time, next_page=next)

    # 查询参数 (在载荷中复制) 按最热排列
    params = {
        'oid': video_id,
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
    time.sleep(random.uniform(3, 6))  # 添加请求时延
    # response.raise_for_status()
    print(f"请求响应状态码：{response.status_code}")

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
    
    # 安全地获取下一页参数 offset参数
    try:
        # 检查所需的嵌套键是否存在
        if ('data' in json_data and 
            'cursor' in json_data['data'] and 
            'pagination_reply' in json_data['data']['cursor']):
            
            pagination_reply = json_data['data']['cursor']['pagination_reply']
            
            # 检查next_offset是否存在
            if 'next_offset' in pagination_reply:
                next_offset = pagination_reply['next_offset']
                return json.dumps(next_offset) if next_offset else ""
            else:
                # 如果next_offset不存在，说明可能已到达最后一页
                print("未找到next_offset字段，可能已到达最后一页")
                return ""
        else:
            print("响应中缺少分页相关信息")
            return ""
    except Exception as e:
        print(f"获取分页参数时发生错误: {e}")
        return None


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
    page = 1
    
    # 构建循环翻页
    while True:
        print(f'正在采集第{page}页的数据内容')
        result = get_comments(next=offset)
        
        # 如果get_comments返回None或空字符串，说明没有更多数据，跳出循环
        if not result or result == '""' or result == "":
            print("已采集完所有数据或出现错误，停止翻页")
            break
            
        offset = result
        page += 1
        
        # 添加保护机制，防止无限循环
        if page > 100:
            print("达到最大页数限制，停止采集")
            break
    
    # 关闭文件
    f.close()
    print(f"数据采集完成，共采集了{page-1}页数据")


if __name__ == '__main__':
    # 加载配置文件
    config = load_config()
    if not config:
        print("无法加载配置文件，程序退出")
        exit(1)
    
    # 从配置文件中获取变量
    cookie = config.get('cookie', '')
    user_agent = config.get('user_agent', '')
    video_url = config.get('video_url', '')
    video_id = config.get('video_id', '')
    
    # 验证必要的配置项
    if not all([cookie, user_agent, video_url, video_id]):
        print("配置文件中缺少必要的参数，请检查config.json文件")
        exit(1)
    
    global_csv_writer = None
    retry_count = 0

    save_csv('comments.csv')
    data_statistics('comments.csv')