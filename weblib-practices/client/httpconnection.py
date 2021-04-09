from http.client import HTTPConnection

conn = HTTPConnection('www.example.com') # naver.com: 302 ok 나옴. (redirect 응답)

conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason) # 응답의 헤더만 본 것 : 200 ok 로 나옴

# 성공
# GET / HTTP / 1.1
# 응답은 200 ok
if resp.status == 200:
    body = resp.read()
    print(type(body), body)

# 실패
# GET / hello.html HTTP / 1.1
# 404 not found

conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)