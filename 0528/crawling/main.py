import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # HTTP GET Request
    req = requests.get('http://uos.ac.kr/korNotice/list.do?list_id=FA1')
    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok
    if is_ok:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select('#contents > ul > li > a')
        print(title)
        return render_template('main.html', titles = title)
    else:
        return '가져오기 실패'

if __name__=='__main__':
    app.run()