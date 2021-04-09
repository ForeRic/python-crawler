from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET 방식 요청
# data 보낼때 url로 보내고 바디는 비워놓는 것이 get 방식
http_response = urlopen('https://www.example.com') # www.example.com?a=10&no=10
body = http_response.read() # 한글 바이트 x84 이런거로만 표현됨. 한글 다 깨져서.
body = body.decode('utf-8') # 한글이 나올 수 있게
print(body)
print('==================================')
# POST 방식 요청 : data를 딕셔너리로 보냄. 이름 값으로. 바디에 붙어서 데이터가 가니까 서버한테 알려줘야 함.
data = {
    'id': 'kickscar',
    'name': '정지윤',
    'pw': '1234'
}

data = urlencode(data).encode('utf-8') # post 방식

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

# http_response = urlopen('https://www.naver.com' + data) # get 방식

http_response = urlopen(request) # url open : post 일땐 이렇게 그냥 하고 get 방식은 string 으로 가니까 그걸 받아야.
print(http_response) # <http.client.HTTPResponse object at 0x0000024CE67D1A60>
print(http_response.status, http_response.reason) # 200 ok
body = http_response.read()
html = body.decode('utf-8')
print(html)
