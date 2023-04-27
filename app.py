from flask import Flask,url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>欢迎来到我的Watchlist! 啦啦啦啦</h1>'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'
