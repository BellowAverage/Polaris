import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

def get_articles_by_users(user_list):
    authors = user_list

    print(authors)

    # Initialize the CSV file and write the header before processing authors
    with open('csdn_crawler.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['author', 'type', 'href', 'name', 'date', 'view_num'])
        writer.writeheader()

    for author in authors:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        print(author)
        
        url = "https://blog.csdn.net/" + author + "/article/list"
        
        result_list = []

        for page_num in range(1, 100):  # Assuming there are up to 100 pages, adjust accordingly
            response = requests.get(f'{url}/{page_num}', headers=headers)
            response.encoding = response.apparent_encoding
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            article_table = soup.find('div', class_='article-list')
            
            if article_table is None:
                break

            for article in article_table.find_all('div', class_='article-item-box'):
                result = {
                    'author': author,
                    'type': article.a.span.text,
                    'href': article.a["href"],
                    'name': article.a.get_text().strip(),
                    'date': article.find('div', class_='info-box').find('span', class_='date').text.strip(),
                    'view_num': article.find('div', class_='info-box').find('span', class_='read-num').text
                }
                result_list.append(result)
        
        # Append the results for each author to the CSV file
        with open('csdn_crawler.csv', 'a', encoding='utf-8', newline='') as f:  # Note the 'a' mode for appending
            writer = csv.DictWriter(f, fieldnames=['author', 'type', 'href', 'name', 'date', 'view_num'])
            # No need to write the header again, it's already written at the beginning
            writer.writerows(result_list)

# # Example usage
# user_list = ['user1', 'user2']  # Replace with your actual user list
# get_articles_by_users(user_list)
