from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
@app.route('/<answer>')
def hello_world(answer=None):
    real_answer = answer
    return render_template('main.html',front_answer = real_answer)

@app.route('/calculate')
def calculate():
    input_data1 = request.args.get('input1')
    input_data2 = request.args.get('input2')
    answer = int(input_data1) * int(input_data2)
    next_url = '/'+str(answer) # /3000 
    return redirect(next_url) # redirect(/3000)

if __name__=='__main__':
    app.run()