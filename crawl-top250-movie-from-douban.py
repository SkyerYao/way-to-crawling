import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
import json

# 用于发送请求，获得网页源代码以供解析
def start_requests(url):
  # 把 user-agent 伪装成浏览器
  user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
  # 构造请求头部的 user-agent
  header = {}
  header['user-agent'] = user_agent
  r = requests.get(url, headers=header)
    return r.content

# 接收网页源代码解析出需要的信息
def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find_all('div', class_ = 'item')
    result_list = []
    for movie in movie_list:
        mydict = {}
        mydict['title'] = movie.find('span', class_ = 'title').text
        mydict['score'] = movie.find('span', class_ = 'rating_num').text
        mydict['quote'] = movie.find('span', class_ = 'inq').text
        star = movie.find('div', class_ = 'star')
        mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
        result_list.append(mydict)
    return result_list

# 将数据写入json文件
def write_json(result):
    s = json.dumps(result, indent = 4, ensure_ascii=False)
    with open('movies.json', 'w', encoding = 'utf-8') as f:
        f.write(s)

# 主运行函数，调用其他函数
def main():
    url = 'https://movie.douban.com/top250'
    text = start_requests(url)
    result = parse(text)
    write_json(result)

# 一般做法
if __name__ == '__main__':
    main()
