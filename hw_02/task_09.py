"""
Задание №9
📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    if request.cookies.get('username'):
        return redirect(url_for('greeting', username=request.cookies.get('username')))
    return render_template('index.html', title='Задание 9')


@app.post('/login/')
def login():
    username = request.form['username']
    email = request.form['email']
    resp = make_response("")
    resp.set_cookie('username', username)
    resp.set_cookie('email', email)
    resp.headers['location'] = url_for('index')
    return resp, 302


@app.route('/greeting/<username>')
def greeting(username):
    context = {'title': 'Приветствие',
               'username': username}
    return render_template('greeting.html', **context)


@app.route('/logout/')
def logout():
    resp = make_response("")
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    resp.headers['location'] = url_for('index')
    return resp, 302


if __name__ == '__main__':
    app.run(debug=True)
