# flask를 비롯해 필요한 함수들을 import 한다.
from flask import Flask, render_template, request, redirect, url_for
# app이란 이름으로 flask 프로젝트 초기화
app = Flask(__name__)

# / 이란 주소와 /<특정값> 이라는 주소에 접근하면,
@app.route('/')
@app.route('/<url_answer>')
# hello_world 함수를 실행하는데, 이때 url_answer의 기본값은 None이다.
def hello_world(url_answer=None):
    # answer라는 값에 url_answer로 받은 값을 준다.
    answer = url_answer
    # render_template 함수를 이용하여 gu_main.html 파일을 연다.
    # 이때, html에서 사용하기 위해 render_answer라는 변수 이름으로 answer값을 준다.
    return render_template('gu_main.html',render_answer = answer)

# /calculate 라는 주소에 접근하면,
@app.route('/calculate')
# calculate 함수를 실행한다.
def calculate():
    # html에서 get방식으로 넘어온 것들 중 Input1이름을 가진친구를 input_data1 으로 받는다.
    input_data1 = request.args.get('input1')
    # html에서 get방식으로 넘어온 것들 중 Input2이름을 가진친구를 input_data2 으로 받는다.
    input_data2 = request.args.get('input2')
    # answer 라는 변수에 위에서 받은 두 값을 int(정수형)으로 바꾸어서 곱한다.
    answer = int(input_data1) * int(input_data2)
    # 답을 str(문자열)로 변환시켜주고 url에 붙여서 redirect함수로 전달한다.
    next_url = '/'+str(answer)
    return redirect(next_url)


if __name__=='__main__':
    app.run()