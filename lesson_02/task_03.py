"""
Задание №3
📌 Создать страницу, на которой будет форма для ввода логина и пароля
📌 При нажатии на кнопку "Отправить" будет произведена проверка
соответствия логина и пароля и переход на страницу приветствия
пользователя или страницу с ошибкой.
"""
import logging
from flask import Flask, request, render_template


app = Flask(__name__)
logger = logging.getLogger(__name__)

users = {
    'user1': '12345',
    'admin': 'Qwerty11'
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return render_template('greeting.html', title='Приветствие', username=username)
        context = {
            'title': 'Пользователь не найден',
            'url': username,
        }
        return render_template('404.html', **context)
    context = {'title': 'Задание 3'}
    return render_template('index3.html', **context)


@app.route('/greeting/<username>')
def greeting(username):
    context = {'title': 'Приветствие',
               'username': username}
    return render_template('greeting.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
