"""
Задание №2
📌 Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Задание 2'}
    return render_template('index2.html', **context)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    context = {'title': 'Загрузка файла'}
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        # file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} загружен на сервер'
    return render_template('upload.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
