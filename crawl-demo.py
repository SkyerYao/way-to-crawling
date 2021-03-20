# 爬取CSDN首页的精选头条标题

import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库

# 传入URL
r = requests.get('https://www.csdn.net/')

# 解析URL
soup = BeautifulSoup(r.text, 'html.parser')
content_list = soup.find_all('p', attrs = {'class': 'headP'})

for content in content_list:
    print(content.text)
