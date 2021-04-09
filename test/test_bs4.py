from bs4 import BeautifulSoup

html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=189075" title="자산어보">자산어보</a>
    </div>
</td>'''


# 1. tag 조회 (순회)
def ex01():
    bs = BeautifulSoup(html, 'html.parser')  # 이거 만들면서 파씽?이 끝남.
    # print(bs)

    tag_td = bs.td
    #print(tag_td)

    #tag_a = bs.a
    #print(tag_a)

    tag_a = tag_td.a # 깊이 들어갈때 위에서 찾는것 보다 찾아놓고 하는게 더 속도가 빠름. 부모에 들어가서 배로 빼옴.
    print(tag_a)

    # None (아무것도 없는 것을 부르면 none 이 나옴)
    tag_h1 = bs.td.h1
    print(tag_h1)

# attribute 로 조회하기
def ex02():
    pass

if __name__ == '__main__':
    #ex01()
    ex02()
