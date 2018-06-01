# 필요한 라이브러리를 우측 명령어를 통해 설치하여 import 한다.
import requests # pip install requests 
from bs4 import BeautifulSoup # pip install bs4

# flask 프로젝트 가져오기
from flask import Flask, render_template
# app이라는 이름으로 플라스크 프로젝트 초기화
app = Flask(__name__)

# / 라는 url로 들어오게 되면
@app.route('/')
# hello_wolrd()함수를 실행한다.
def hello_world():
    # HTTP GET Request, 입력한 url에 대한 정보를 가져온다.
    req = requests.get('http://uos.ac.kr/korNotice/list.do?list_id=FA1')
    # HTML 소스 가져오기, req에 존재하는 text(html code)를 가져온다.
    html = req.text
    # HTTP Header 가져오기, req에 있는 headers를 가져온다. 현재 우리에겐 필요 x
    header = req.headers
    # HTTP Status 가져오기 (200: 정상), status 확인, 현재 우리에겐 필요 x
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False), 정상적으로 접근이 안된다면 위에서 가져온 html코드가 잘못된 것일 수 있으므로
    # 이를 체크하여, 정상적으로 접근되었을때를 처리한다.
    is_ok = req.ok
    if is_ok: # is_ok, 즉 정상접근이 Ture라면
        # bs를 이용하여 우리가 가져온 html코드를 파싱한다(나눈다.) 왜? 우리가 보고 싶은 부분만 보기 위해서
        soup = BeautifulSoup(html, 'html.parser')
        # 우리는 학교 공지사항에서 각 제목만 가져올것, 개발자도구에서 가져오고자 하는 요소의 코드에서 우클릭하여 copy selector를 누르면된다.
        # 이를 통해 걸러낸 요소를 리스트로 반환한다. 즉, title = [제목1, 제목2, ...] 이런식으로 저장될 것
        title = soup.select('#contents > ul > li > a')
        # render_template 함수를 이용하여 main.html을 반환하고 이때 titles라는 이름의 변수로 우리가 가져온 리스트 title을 넘겨준다.
        return render_template('main.html', titles = title)
    else:
        return '가져오기 실패'
if __name__=='__main__':
    app.run()