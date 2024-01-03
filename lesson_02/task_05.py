"""
Задание №5
📌 Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
📌 При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Задание 5'}
    return render_template('index5.html', **context)


@app.post('/calc/')
def calc():
    op_list = ['+', '-', '*', '/']
    num1 = int(request.form['number1'])
    num2 = int(request.form['number2'])
    op = int(request.form['operation'])
    result = ''
    if op == 1:
        result = num1 + num2
    if op == 2:
        result = num1 - num2
    if op == 3:
        result = num1 * num2
    if op == 4:
        if num2 == 0:
            result = 'inf'
        else:
            result = num1 / num2
    return render_template('calc.html',
                           num1=num1,
                           num2=num2,
                           op=op_list[int(op) - 1],
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)
