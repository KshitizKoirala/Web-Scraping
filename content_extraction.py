import requests
BASE_URL = 'https://www.onlinekhabar.com/'
content = requests.get(BASE_URL).content

from bs4 import BeautifulSoup
context = BeautifulSoup(content, features="html.parser")
a_tags = context.find_all('a')
links = set()

for a_tag in a_tags:
    if '2019' in a_tag.get('href', ''):
        links.add(a_tag.get('href'))

with open('news_collection.txt', 'w', encoding='utf-8') as news_file:

    for link in links:
        inner_content = requests.get(link).content
        inner_context = BeautifulSoup(inner_content, features="html.parser")
        news_div = inner_context.select_one('.ok18-single-post-content-wrap')

        #here . in front of class link is required like in css to differenciate between class and id()for id #

        news_file.write(news_div.text)
        news_file.write('\n\n\n\n')