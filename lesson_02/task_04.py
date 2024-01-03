"""
Задание №4
📌 Создать страницу, на которой будет форма для ввода
текста и кнопка "Отправить"
📌 При нажатии кнопки будет произведен подсчет количества
слов в тексте и переход на страницу с результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Задание 4'}
    return render_template('index4.html', **context)


@app.post('/text_proc')
def text_proc():
    text = request.form['text']
    count_words = len(text.split())
    context = {'title': 'Текст',
               'count_words': count_words,
               'text': text}
    return render_template('text.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
