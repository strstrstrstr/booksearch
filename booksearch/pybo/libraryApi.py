import json
from urllib import request, parse
import datetime
import urllib
authkey = '158353134f293055e344b66fa68d3649836912a99af53dcd373bf864905e186f'

libraryValList = ['gender', 'age', 'addCode', 'ddition_symbol', 'kdc', 'dtl_kdc', 'region', 'dtl_region', 'startDt', 'endDt', 'pageSize']

def url(data=False) :
    dt_now = datetime.datetime.now()
    page = 10  # 기본 값
    abcd = dict()

    url = ""

    if type(data) == type(abcd) :
        for key, val in data.items():
            if key in libraryValList :
                url+="&"+key+"="+val
        if 'startDt' not in data:
            url += "&" + 'startDate' + "=" + str(dt_now.year)+"-01-01"
        if 'pageSize' not in data:
            url += "&" + 'pageSize' + "=" + str(page)
    else :
        url += "&" + 'startDate' + "=" + str(dt_now.year) + "-01-01"
        url += "&" + 'pageSize' + "=" + str(page)
    return url

def bestSeller(url):
    main = "http://data4library.kr/api/loanItemSrch?authKey="+authkey+"&format=json"
    req = request.Request(main+url)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')
    response_json = json.loads(res)
    return response_json

def bookSearch(url, keyword) :
    main = "http://data4library.kr/api/srchBooks?authKey="+ authkey + "&format=json"+"&keyword="+urllib.parse.quote(keyword)
    mainUrl = main+url
    req = request.Request(mainUrl)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')
    response_json = json.loads(res)
    return response_json