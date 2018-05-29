from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<url_answer>')
def hello_world(url_answer=None):
    answer = url_answer
    return render_template('gu_main.html',render_answer = answer)

@app.route('/calculate')
def calculate():
    input_data1 = request.args.get('input1')
    input_data2 = request.args.get('input2')
    answer = int(input_data1) * int(input_data2)
    next_url = '/'+str(answer)
    return redirect(next_url)


if __name__=='__main__':
    app.run()