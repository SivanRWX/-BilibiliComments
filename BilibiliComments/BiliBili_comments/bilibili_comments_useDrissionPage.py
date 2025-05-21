import numpy as np
from PIL import Image
from pyecharts import options as opts
from pyecharts.charts import Pie
from datetime import datetime  # 导入日期转换模块
import csv  # 导入csv模块
import hashlib  # 导入哈希模块
from urllib.parse import quote  # 导入编码的方法
import time  # 导入时间模块
import pandas as pd  # 导入数据处理模块
import jieba  # 导入分词模块
from wordcloud import WordCloud  # 导入词云模块
from matplotlib import pyplot as plt
import random  # 添加随机延迟
import requests

from DrissionPage import ChromiumPage

# Cookie 字符串
cookie_str = (
    "buvid3=B25FEA33-6B46-3C5E-A18A-C3E53763A9F932854infoc; "
    "b_nut=1747320632; "
    "_uuid=35A716DE-7109E-2293-9FF4-225FB6A5699234883infoc; "
    "CURRENT_FNVAL=4048; "
    "buvid4=F173D692-E496-759E-5D4E-88E0938645B834679-025051522-LAQ2E/2AzFkNNYOyQ++fIQ%3D%3D; "
    "rpdid=|(JY~|lk~)R)0J'u~R~Jk|YJR; "
    "SESSDATA=adedc65e%2C1762922652%2C49cf3%2A51CjDY4gBlocko40Qwo16KhMaFvccww4rFFKeNCURUEN9hEBlD2t_0Zj92oPECNZBWwF8SVnBhQ1NxQUFkUkk1clJ3WUp0QXR3MEJQSm8xdmJ3dlctUzJOQldXMmp3Qzl4UHJZN1JUcXdfUVRzZ2Jsb2wya2dzaU1xVEJlUGlxd2NLTV9qWVJ0V3ZnIIEC; "
    "bili_jct=8fe597bfefad11937b62ade21974effe; "
    "DedeUserID=473409553; "
    "DedeUserID__ckMd5=5a076712a01c326e; "
    "fingerprint=d4c24c7d411e000b2732c6d26a01f97a; "
    "buvid_fp_plain=undefined; "
    "buvid_fp=d4c24c7d411e000b2732c6d26a01f97a; "
    "bp_t_offset_473409553=1067817522205556736; "
    "b_lsid=D14B9A2B_196DD52284E; "
    "bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDc3MzI2MjEsImlhdCI6MTc0NzQ3MzM2MSwicGx0IjotMX0.lQ1Vt_etkTigl3VKsYIyYvO55TsRNpp_H1NZbjSfJlk; "
    "bili_ticket_expires=1747732561; "
    "sid=6mbf7u9r"
)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
output_csv = 'bilibili_comments.csv'
video_url = 'https://www.bilibili.com/video/BV1x54y1e7zf'


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
    print(w_rid)
    return w_rid, pagination_str


# 初始化浏览器并设置cookie
def parse_cookies(cookie_str):
    """将 Cookie 字符串解析为字典列表"""
    cookies = []
    for item in cookie_str.split('; '):
        if '=' in item:
            name, value = item.split('=', 1)
            cookies.append({
                'name': name.strip(),
                'value': value.strip(),
                'domain': '.bilibili.com',
                'path': '/',
                # 有效期设置为 1 天（单位：秒）
                'expires': int(time.time()) + 86400
            })
    return cookies


def crawl_comments():
    """主爬虫逻辑"""

    # 创建浏览器对象并设置 Cookie
    page = ChromiumPage()
    cookies = parse_cookies(cookie_str)
    page.set.cookies(cookies)

    # 验证登录状态
    page.get('https://www.bilibili.com')
    if page.title == '哔哩哔哩 (゜-゜)つロ 干杯~-bilibili':
        print('✅ Cookie 登录成功')
    else:
        print('❌ 登录状态异常，请检查 Cookie 有效性')
        page.quit()
        exit()

    # 获取时间戳
    now_time = int(time.time())
    # 获取加密参数
    w_rid, pagination_str = get_sign(now_time, '{"offset":""}')

    # 监听带签名的接口
    page.listen.start(f'api.bilibili.com/x/v2/reply/main?*w_rid={w_rid}*')

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

    # 访问视频页面
    page.get(video_url)
    page.wait.load_start()

    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['昵称', '性别', '地区', '日期', '内容', '点赞'])
        writer.writeheader()

        collected = set()  # 用于去重
        retry_count = 0

        # # 跳转到抓取页面
        # page.get(video_url)
        # page.wait(1)

        while len(collected) < 200 and retry_count < 5:  # 最多采集200条或重试5次
            # 滚动到评论区
            page.scroll.to_bottom()

            # 获取所有评论卡片
            comments = page.eles('.reply-item:not([data-loaded="true"])')

            for comment in comments:
                try:
                    # 标记已处理
                    comment.set.attr('data-loaded', 'true')

                    # 提取用户信息
                    user_info = comment.ele('.user-info')
                    username = user_info.ele('.user-name').text
                    gender = '男' if 'male' in user_info.ele('.user-gender').attr('class') else '女'

                    # 提取IP属地
                    location = comment.ele('.ip-location').text.replace('IP属地：', '')

                    # 提取评论内容
                    content = comment.ele('.text-con').text

                    # 提取点赞数
                    like = comment.ele('.like span').text

                    # 时间处理
                    time_str = comment.ele('.time').text
                    comment_time = datetime.now().strftime('%Y-%m-%d')  # 如果时间是相对时间需要额外处理

                    # 去重检查
                    if content not in collected:
                        writer.writerow({
                            '昵称': username,
                            '性别': gender,
                            '地区': location,
                            '日期': comment_time,
                            '内容': content,
                            '点赞': like
                        })
                        collected.add(content)
                        print(f'✅ 已采集：{username} 的评论')
                except Exception as e:
                    print(f'⚠️ 解析失败：{str(e)}')
                    continue

            # 滚动加载更多
            page.scroll.down(800)
            time.sleep(random.uniform(1.5, 3.5))

            # 检查是否到底
            if page.ele('.no-more', timeout=2):
                print('已加载全部评论')
                break

            # 重试机制
            if not comments:
                retry_count += 1
                page.scroll.down(1000)
                time.sleep(2)
            else:
                retry_count = 0

        print(f'🎉 采集完成，共获得 {len(collected)} 条评论')
        page.quit()


def process_comments(data, writer):
    """处理评论数据"""
    for reply in data['data']['replies']:
        try:
            ctime = reply['ctime']
            writer.writerow({
                '昵称': reply['member']['uname'],
                '性别': reply['member']['sex'],
                '地区': reply['reply_control']['location'].replace('IP属地：', ''),
                '日期': datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S'),
                '内容': reply['content']['message'],
                '点赞': reply['like']
            })
            print(f"已采集：{reply['member']['uname']}的评论")
        except Exception as e:
            print(f"解析失败：{str(e)}")


def generate_visualization():
    # 地区分布可视化
    def create_area_chart():
        df = pd.read_csv('bilibili_comments.csv')
        area_counts = df['地区'].value_counts()

        pie = (
            Pie()
            .add("", [list(z) for z in zip(area_counts.index.tolist(), area_counts.values.tolist())])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="B站评论地区分布"),
                legend_opts=opts.LegendOpts(pos_left="right", orient="vertical")
            )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        pie.render("bilibili_area_distribution.html")

    # 生成词云
    def create_wordcloud():
        df = pd.read_csv('bilibili_comments.csv')
        content = ' '.join(df['内容'].astype(str))

        # 使用自定义形状
        mask = np.array(Image.open('mask_shape.png'))  # 准备一个PNG形状文件

        wc = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            max_words=200,
            mask=mask,
            stopwords={'了', '的', '是', '我', '在', '有', '就', '也', '啊', '这个'}
        )

        words = ' '.join(jieba.lcut(content))
        wc.generate(words)

        plt.figure(figsize=(10, 8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('bilibili_wordcloud.png')
        plt.show()


if __name__ == '__main__':
    crawl_comments()
    generate_visualization()
