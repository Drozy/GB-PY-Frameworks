"""
Создать базовый шаблон для интернет-магазина, содержащий общие элементы
дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров. Например, создать страницы «Одежда»,
«Обувь» и «Куртка», используя базовый шаблон.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)


@app.route('/clothes/jacket')
def jacket():
    context = {'title': 'Зеленая куртка'}
    return render_template('jacket1.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
