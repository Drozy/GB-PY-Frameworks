"""
1) Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".

2) Добавьте две дополнительные страницы в ваше веб-
приложение:
○ страницу "about"
○ страницу "contact".

3) Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.

4) Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""

from flask import Flask

app = Flask(__name__)


# 1
@app.route('/')
def hello_world():
    return 'Hello World!'


# 2
@app.route('/about')
def about():
    return 'about'


@app.route('/contact')
def contact():
    return 'contact'


# 3
@app.route('/sum/<int:a>+<int:b>/')
def sum_numbers(a, b):
    return f'{a} + {b} = {a + b}'


# 4
@app.route('/len/<data>/')
def len_str(data):
    return f'Длина строки "{data}":<br>{len(data)}'


if __name__ == '__main__':
    app.run(debug=True)
