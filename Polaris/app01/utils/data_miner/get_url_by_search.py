import json
import requests
import csv

class CSDN:
    def __init__(self, search_keyword=None):
        self.url = 'https://so.csdn.net/api/v3/search?q={}&t=all&p={}'
        self.headers = {
            # Your headers here
        }
        self.keyword = search_keyword
        self.csv_file = "csdn_data.csv"  # 设置CSV文件名

    def send_request(self, url):
        try:
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                html = res.text
            else:
                html = None
            return html
        except requests.RequestException:
            print("请求网页失败")

    @staticmethod
    def get_data(html):
        data_list = json.loads(html)
        data = data_list['result_vos']
        for obj in data:
            _id = obj['id']
            author = obj['nickname']
            title = obj['title']
            url = obj['url_location']
            comment_num = obj.get('comment', 0)
            like_num = obj.get('digg', 0)
            view_num = obj.get('view_num', 0)
            create_time_str = obj['created_at']
            yield {
                "编号": _id,
                "作者": author,
                "标题": title,
                "链接": url,
                "浏览量": view_num,
                "评论数量": comment_num,
                "点赞数量": like_num,
                "发布时间": create_time_str
            }

    def save_to_csv(self, data):
        with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:  # 如果文件是空的，写入表头
                writer.writeheader()
            writer.writerow(data)
            print("数据保存到CSV成功")

    def main(self):
        start_page = int(input("请输入起始页码:"))
        end_page = int(input("请输入终止页码:"))
        for offset in range(start_page, end_page + 1):
            print("正在获取第{}页".format(offset))
            url = self.url.format(self.keyword, offset)
            html = self.send_request(url)
            for data in self.get_data(html):
                print(data)
                self.save_to_csv(data)

if __name__ == '__main__':
    keyword = input("请输入您想要搜索的关键词:")
    CSDN(search_keyword=keyword).main()