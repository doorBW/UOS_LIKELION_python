from flask import Flask
from flask_mail import Mail, Message
# https://pythonhosted.org/Flask-Mail/
# mail app을 만드는 2가지 방법
# 1. flask app을 먼저 만들고 이를 통해 Mail 객체 생성
app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'doobw@likelion.org',
	MAIL_PASSWORD = ''
	)
mail = Mail(app)

# 2. Mail객체를 먼저 만들고, 이후에 만든 flask app을 mail 객체에 설정
mail = Mail()

app = Flask(__name__)
mail.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/email')
def email_test():
    msg = Message("Hello",
                  sender="doorbw@outlook.com",
                  recipients=["qjadn9@naver.com"])
    msg.body = "testing"
    # msg.html = "<b>testing</b>"
    mail.send(msg)
    return 'email'

if __name__=='__main__':
    app.run()