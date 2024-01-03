"""
Задание №1
📌 Создать страницу, на которой будет кнопка "Нажми меня",
при нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Задание 1'}
    return render_template('index1.html', **context)


@app.route('/greeting', methods=['POST'])
def greeting():
    context = {'title': 'Приветствие',
               'username': request.form['username']}
    return render_template('greeting.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
