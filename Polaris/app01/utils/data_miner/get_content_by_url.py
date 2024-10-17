import requests
import parsel
import tomd
import os
import re
import pandas as pd
import time

def sanitize_filename(filename):
    # 去除Windows文件名中的非法字符
    sanitized = re.sub(r'[\\/*?:"<>|]', "", filename)
    # 将空白字符替换为下划线
    sanitized = re.sub(r'\s+', '_', sanitized)
    # 去除emoji和其他非ASCII字符
    sanitized = re.sub(r'[^\x00-\x7F]+', '', sanitized)
    # 去除除字母数字字符、点、连字符和下划线外的所有字符
    sanitized = re.sub(r'[^\w.-]', '', sanitized)
    return sanitized.rstrip("_").lstrip("_")  # 去除首尾可能出现的下划线

def spider_csdn(author, title_url, article_count):
    if article_count >= 100:
        return True
    start_time = time.time()
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52",
            "Referer": "https://blog.csdn.net/tansty_zh"
        }
        html = requests.get(url=title_url, headers=head, timeout=10).text
        page = parsel.Selector(html)
        title = page.css(".title-article::text").get()
        content = page.css("article").get()
        
        if content is None:
            print(f"Failed to extract article content from {title_url}")
            return False
        
        content = re.sub("<a.*?a>", "", content)
        content = re.sub("<br>", "", content)
        head = "\n--- \ntitle:  " + title + " \ntags: []\ncategories: [] \n\n---"
        text = tomd.Tomd(content).markdown
        text = head + text
        
        final_road = os.path.join(".", sanitize_filename(author))
        if not os.path.exists(final_road):
            os.makedirs(final_road)
            print('创建文件夹: ' + final_road)
        
        sanitized_title = sanitize_filename(title)
        file_path = os.path.join(final_road, sanitized_title + ".md")
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(text)
        print("成功保存：", file_path)
        return False
    
    except requests.exceptions.Timeout:
        print(f"Error: Timeout for {title_url}")
        return False
    except Exception as e:
        print(f"Error processing {title_url}: {e}")
        return False
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 10:
            print(f"Processing {title_url} took too long ({elapsed_time} seconds), skipping.")

def main():
    urls_df = pd.read_csv('csdn_crawler.csv', usecols=["author", "href"])
    author_article_count = {}
    
    for index, row in urls_df.iterrows():
        author = row['author']
        if author in ["m0_58523831", "ityard"]:  # 跳过特定的作者
            continue
        if author not in author_article_count:
            author_article_count[author] = 0
        
        if author_article_count[author] < 100:
            limit_reached = spider_csdn(author, row['href'], author_article_count[author])
            if not limit_reached:
                author_article_count[author] += 1
            else:
                print(f"Reached article limit for author {author}")
        else:
            print(f"Skipping additional articles for author {author}, limit reached.")

if __name__ == '__main__':
    main()
