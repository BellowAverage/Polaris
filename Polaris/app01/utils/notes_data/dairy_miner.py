import requests
import csv
from lxml import etree

def get_diary(url, writer):
    headers = {
        # 'Cookie': "lang=zh-CN; nickname=syndrome; YouGamSession=025dfc3cde959a5d",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code in (301, 302, 303, 307, 308):
            redirect_url = response.headers.get('Location')
            if redirect_url:
                response = requests.get(redirect_url)

        tree = etree.HTML(response.content)

        # Update these XPath expressions based on the actual HTML structure
        user_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a'
        title_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/h1'
        location_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/i[3]'
        time_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/i[2]'
        content_xpath = '//*[@id="diary-content"]'


        user = tree.xpath(f"{user_xpath}/text()")
        title = tree.xpath(f"{title_xpath}/text()")
        location = tree.xpath(f"{location_xpath}/text()")
        time = tree.xpath(f"{time_xpath}/text()")
        content = tree.xpath(f"{content_xpath}/text()")

        user_text = user[0] if user else "Not Found"
        title_text = title[0] if title else "Not Found"
        location_text = location[0] if location else "Not Found"
        time_text = time[0] if time else "Not Found"

        if content:
            content_text = "".join(content)
            writer.writerow([user_text, title_text, content_text, location_text, time_text])
            print(user_text, title_text, content_text, location_text, time_text)
        else:
            print(url, "Content not found.")
    
    except requests.exceptions.TooManyRedirects:
        print(url, "Too many redirects. Skipping to the next loop iteration.")
    except Exception as e:
        print(url, "Error occurred:", e)
        

if __name__ == '__main__':
    with open('diary_info_20w_to_1000.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['User', 'Title', 'Content', 'Location', 'Time'])
        
        # Example of iterating over a range of diary entries
        for i in range(196000, 176000, -1):
            url = f"http://www.lapuda.org/diary/{i}/"
            get_diary(url, writer)
