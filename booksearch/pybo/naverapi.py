import json
import urllib


def naver_blog(keyword):
    client_id = "o_Mnz0imU7cpd_yJr0St"
    client_secret = "ajzxkOM8Rb"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        response_json = json.loads(response_body)
        response_item=response_json['items']
    else:
        print("Error Code:" + rescode)
    result = []
    for temp in response_item:
        result.append(temp['title'])

    return result #" ".join(result)

