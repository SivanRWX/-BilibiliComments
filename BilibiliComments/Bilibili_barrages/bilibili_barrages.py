import requests
import dm_pb2  # b站弹幕解密文件
from google.protobuf import text_format
import re  # 正则表达式模块
from datetime import datetime
import csv
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import pandas as pd  # 图形化
import jieba  # 分词处理

"""
B站弹幕数据采集脚本
通过调用B站弹幕接口，获取并解析弹幕数据，最后保存到CSV文件中
"""

"""
1. 分析数据
        浏览器抓包分析或者使用别人开发的访问接口获取，接口获取见readme
2. 发送请求
        使用请求头模式
3. 获取数据
        protobuf反序列化
4. 解析数据
        正则匹配
5. 保存数据
        csv
"""

"""
载荷部分————对于这个视频
type: 1
oid: 226204073
pid: 841786906
segment_index           # B站的弹幕是分页存储的,每页存六分钟的弹幕
web_location: 1315873
w_rid: 8b6a976ae9ead8938556950726f3a7a0
wts: 1747556105
"""

"""
核心： 参数解密
JS逆向 MD5
1. 访问接口
2. 获取加密参数w_rid
3. 解析protobuf数据
4. 正则匹配
5. 保存数据
6. 可视化数据
7. 数据统计

"""
"""
注意：获取到的弹幕数据是二进制的protobuf格式，不能直接使用json解析，需要使用protobuf库进行解析。
protobuf库需要安装：pip install protobuf
另外，protobuf的解析需要使用到Google的protobuf库，可以通过pip安装：pip install google
"""

# 用户认证信息 （网络访问抓取）
cookie = ("buvid3=B25FEA33-6B46-3C5E-A18A-C3E53763A9F932854infoc; b_nut=1747320632; "
          "_uuid=35A716DE-7109E-2293-9FF4-225FB6A5699234883infoc; CURRENT_FNVAL=4048; "
          "buvid4=F173D692-E496-759E-5D4E-88E0938645B834679-025051522-LAQ2E/2AzFkNNYOyQ++fIQ%3D%3D; rpdid=|("
          "JY~|lk~)R)0J'u~R~Jk|YJR; "
          "SESSDATA=adedc65e%2C1762922652%2C49cf3"
          "%2A51CjDY4gBlocko40Qwo16KhMaFvccww4rFFKeNCURUEN9hEBlD2t_0Zj92oPECNZBWwF8SVnBhQ1NxQUFkUkk1clJ3WUp0QXR3MEJQSm8"
          "xdmJ3dlctUzJOQldXMmp3Qzl4UHJZN1JUcXdfUVRzZ2Jsb2wya2dzaU1xVEJlUGlxd2NLTV9qWVJ0V3ZnIIEC; bili_jct=8fe597bfefad"
          "11937b62ade21974effe; DedeUserID=473409553; DedeUserID__ckMd5=5a076712a01c326e; fingerprint=d4c24c7d411e000b"
          "2732c6d26a01f97a; buvid_fp_plain=undefined; buvid_fp=d4c24c7d411e000b2732c6d26a01f97a; bp_t_offset_473409553"
          "=1067817522205556736; b_lsid=D14B9A2B_196DD52284E; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6I"
          "kpXVCJ9.eyJleHAiOjE3NDc3MzI2MjEsImlhdCI6MTc0NzQ3MzM2MSwicGx0IjotMX0.lQ1Vt_etkTigl3VKsYIyYvO55TsRNpp_H1NZbjSf"
          "Jlk; bili_ticket_expires=1747732561; sid=6mbf7u9r")
# 用户代理标识（模拟浏览器访问）
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 "
              "Safari/537.36")
# 视频页面URL（用于Referer反爬校验）
video_url = 'https://www.bilibili.com/video/BV1x54y1e7zf'


# 请求头
headers = {
    # cookie信息检测是否有登录账号
    "cookie": cookie,
    "user-agent": user_agent,
    "referer": video_url,
}

oid = 226204073


def get_all_segments():
    """获取视频的总分段数（通常每6分钟一个分段）"""
    # 视频时长18分钟以内，分段数为3
    return 3


def rc():
    """基础图像与字体设置"""
    # plt.rcParams是一个字典，它存储了matplotlib的配置参数，用于控制图形的外观和行为
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    # 默认使用Unicode字符U+2212，可导致保存图像时的乱码问题。设置为False则用ASCII字符U+002D，避免混淆并解决保存问题
    plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号


def create_csv(filename):
    # 创建CSV文件并写入表头
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["弹幕所在位置", "弹幕内容", "弹幕发布时间"])


def get_barrages(segment_index, filename):
    # 弹幕接口URL（包含加密参数，需通过抓包分析获取）
    url = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={oid}&segment_index={segment_index}'

    # 发送GET请求(请求头做伪装)
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        print(f"分段 {segment_index} 请求失败: {response.status_code}")
        return

    # 使用protobuf反序列化数据
    my_seg = dm_pb2.DmSegMobileReply()  # 创建协议缓冲区对象
    data = response.content  # 获取二进制响应内容
    my_seg.ParseFromString(data)  # 解析protobuf数据

    # 遍历解析后的弹幕元素
    for i in my_seg.elems:
        # 转换为文本格式以便提取数据
        parse_data = text_format.MessageToString(i, as_utf8=True)
        try:
            # 使用正则表达式提取弹幕出现时间点（视频进度，单位毫秒）
            progress = re.findall('progress: (.*)', parse_data)[0]
        except:
            progress = 1000  # （当progress字段不存在时）

        # 将毫秒转换为 00 : 00格式
        minutes, seconds = divmod(int(progress) // 1000, 60)
        current_time = f'{minutes:02d}:{seconds:02d}'

        # 提取弹幕内容（正则匹配content字段）
        content = re.findall('content: (.*)', parse_data)[0]

        # 提取创建时间戳并转换为可读格式（UTC时间戳转本地时间）
        ctime = re.findall('ctime: (.*)', parse_data)[0]
        date_time = datetime.fromtimestamp(int(ctime)).strftime('%Y-%m-%d %H:%M:%S')

        # 控制台打印结果
        print(current_time, content, date_time)

        # 追加写入剩余CSV文件
        with open(filename, mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([current_time, content, date_time])


def wordcloud(filename):
    # 词云图配置
    # 读取数据
    df = pd.read_csv(filename)
    # 获取评论数据 合并成字符串
    content = ' '.join([i for i in df['弹幕内容']])
    # 分词处理
    string = ' '.join(jieba.lcut(content))
    wc = WordCloud(
        height=700,  # 高
        width=1000,  # 宽
        background_color='white',  # 背景颜色
        font_path='msyh.ttc',  # 字体
        stopwords={'了', '的', '都', '还', '就', '我', '你', '他', '啊', '呢', '哦'}  # 停用词
    )
    # 导入词汇
    wc.generate(string)
    # 导出词云图
    wc.to_file('wc.png')

    # 展示词云图
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


def barrages_stats(filename):
    # 读取数据
    df = pd.read_csv(filename)

    # 弹幕所在时段（每分钟）数量统计
    # 将"弹幕所在位置"转换为时间戳（秒数）
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    df['时间秒数'] = df['弹幕所在位置'].apply(time_to_seconds)

    # 按每分钟分段统计
    df['分钟段'] = (df['时间秒数'] // 60).astype(int)

    # 统计每分钟的弹幕数量
    minute_counts = df['分钟段'].value_counts().sort_index()

    # 可视化每分钟弹幕数量
    plt.figure(figsize=(12, 6))
    minute_counts.plot(kind='bar', color='skyblue')
    plt.title('每分钟弹幕数量统计')
    plt.xlabel('视频时间（分钟）')
    plt.ylabel('弹幕数量')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('minute_barrage_counts.png')
    plt.show()

    # 输出统计结果
    print("\n弹幕每分钟数量统计：")
    print(minute_counts)

    # 热门时段分析
    # 找出弹幕最多的前5个分钟段
    top_minutes = minute_counts.nlargest(5)
    print("\n弹幕最多的前5个分钟段：")
    print(top_minutes)

    # 弹幕发布时段分析（按小时）
    df['发布时间'] = pd.to_datetime(df['弹幕发布时间'])
    df['发布小时'] = df['发布时间'].dt.hour

    hour_counts = df['发布小时'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    hour_counts.plot(kind='bar', color='lightgreen')
    plt.title('弹幕发布时间分布（按小时）')
    plt.xlabel('小时')
    plt.ylabel('弹幕数量')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('hourly_barrage_counts.png')
    plt.show()


if __name__ == '__main__':
    rc()
    create_csv("barrages.csv")
    total_segments = get_all_segments()

    for segment in range(1, total_segments + 1):
        print(f"正在获取分段 {segment}/{total_segments}...")
        get_barrages(segment, "barrages.csv")

    wordcloud('barrages.csv')
    barrages_stats("barrages.csv")
