import pandas as pd  # 导入数据处理模块
import jieba  # 导入分词模块
from matplotlib import pyplot as plt
from collections import Counter
from wordcloud import WordCloud  # 导入词云模块

"""
B站评论数据分析统计
"""


def data_statistics(filename):
    """数据分析统计"""
    # 停用词列表
    stopwords = {'了', '的', '都', '还', '就', '我', '你', '他', '啊', '在', '是', '这', '那',
                 '和', '就', '也', '有', '不', '人', '吗', '吧', '哦', '呀', '哈', '？', '！', '这个'}

    def rc():
        """基础图像与字体设置"""
        # plt.rcParams是一个字典，它存储了matplotlib的配置参数，用于控制图形的外观和行为
        plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
        # 默认使用Unicode字符U+2212，可导致保存图像时的乱码问题。设置为False则用ASCII字符U+002D，避免混淆并解决保存问题
        plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

    def location_stats():
        """地区人数分布统计"""
        # 地区人数统计
        print('\n======== 地区人数统计 ========')
        area_counts = df['地区'].value_counts().head(10)
        print(area_counts)

        # 可视化地区分布
        plt.figure(figsize=(12, 6))
        area_counts.plot(kind='bar', color='skyblue')
        plt.title('评论用户地区分布 Top10')
        plt.xlabel('地区')
        plt.ylabel('评论数量')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('area_distribution.png')  # 保存图片
        plt.show()

    def sex_stats():
        """性别分布分析"""
        # 性别分布分析
        print('\n======== 性别分布 ========')
        gender_counts = df['性别'].value_counts()
        print(gender_counts)

    def process_text(text):
        """文本处理器"""
        # 去除特殊符号
        text = text.replace('\n', '').replace('\r', '').replace('\t', '')
        # 精确分词
        words = jieba.lcut(text)
        # 过滤停用词和单字
        return [word for word in words if len(word) > 1 and word not in stopwords]

    def comments_top_words():
        """评论关键词分析"""
        # 评论关键词分析

        # 处理所有评论
        all_words = []
        for comment in df['评论']:
            all_words.extend(process_text(comment))

        # 统计词频
        word_counts = Counter(all_words)
        top_words = word_counts.most_common(10)

        # 展示词频统计结果
        print('\n======== 高频词汇 Top10 ========')
        for word, count in top_words:
            print(f'{word}: {count}次')

        # 可视化高频词
        plt.figure(figsize=(12, 6))
        words, counts = zip(*top_words)
        plt.barh(words, counts, color='salmon')
        plt.title('评论高频词汇 Top10')
        plt.xlabel('出现次数')
        plt.gca().invert_yaxis()  # 倒置Y轴使最高频显示在顶部
        plt.tight_layout()
        plt.savefig('word_frequency.png')  # 保存图片
        plt.show()

    def like_stats():
        """点赞数分析"""
        # 点赞数分析
        print('\n======== 点赞数分析 ========')
        print(f'平均点赞数：{df["点赞"].mean():.1f}')
        print(f'最高点赞数：{df["点赞"].max()}')
        print(f'点赞中位数：{df["点赞"].median()}')

    def comment_time_stats():
        """评论时间分析（小时）"""
        # 时间趋势分析（按小时）
        # 从'日期'列提取小时信息...
        print('\n======== 评论时间分析 ========')
        df['小时'] = pd.to_datetime(df['日期']).dt.hour
        # 统计每小时评论数量并排序
        hour_counts = df['小时'].value_counts().sort_index()
        print(f"每小时评论数量统计结果：\n{hour_counts}")

        # 创建画布并绘制折线图
        plt.figure(figsize=(12, 6))
        # 设置图表标题和坐标轴标签
        hour_counts.plot(kind='line', marker='o', color='green')
        plt.title('评论时间分布')
        plt.xlabel('小时')
        plt.ylabel('评论数量')

        # 设置x轴刻度为0-23小时
        plt.xticks(range(24))
        # 添加网格线
        plt.grid(True)
        # 调整布局并保存图表
        plt.tight_layout()
        plt.savefig('time_distribution.png')
        # 展示
        plt.show()

    def wordcloud():
        """生成词云图"""
        # 生成词云图
        # 读取数据
        df = pd.read_csv(filename)
        # 获取评论数据 合并成字符串
        content = ' '.join([i for i in df['评论']])
        # 分词处理
        string = ' '.join(jieba.lcut(content))

        # 词云图配置
        wc = WordCloud(
            height=700,  # 高
            width=1000,  # 宽
            background_color='white',  # 背景颜色
            font_path='msyh.ttc',  # 字体
            stopwords={'了', '的', '都', '还', '就', '我', '你', '他', '啊'}  # 停用词
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

    # 调用函数
    rc()
    # 读取数据
    df = pd.read_csv(filename)

    location_stats()
    comments_top_words()
    like_stats()
    comment_time_stats()
    wordcloud()
    sex_stats()


if __name__ == '__main__':
    data_statistics('comments.csv')
