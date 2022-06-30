import re
import json
import urllib.request
import lxml
from requests import request


def booksearch_info(bookname):
    client_id = "oZDAxVWYW3Xowt5LS37e"
    client_secret = "5qMuJh47cL"
    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        # print(response_body.item)
        # print(json.loads(response_body))
        a=json.loads(response_body)['items'][0]
        # print(re.sub(r'\([^)]*\)', '', a['title']).replace('<b>','').replace('</b>',''))
        bookname=re.sub(r'\([^)]*\)', '', a['title']).replace('<b>','').replace('</b>','')
        bookyear=a['pubdate'][:4]
        bookisbn=a['isbn'].split(' ')[1]
        # print(bookname,bookyear,bookisbn)
        bookinfo={'bookname':bookname,'bookyear':bookyear,'bookauthor':a['author'],'bookisbn':bookisbn}
        return bookinfo
    else:

        print("Error Code:" + rescode)

import requests
from bs4 import BeautifulSoup

def yes24_steady_sell():
    url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03'

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html,"lxml")
    # print(soup.text)
    soup_list = soup.find_all('td',class_='goodsTxtInfo')
    result=[]
    for temp in range(5):
        result.append(soup_list[temp].find('a').text)

    return result