from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>������, ������! � - ������ ������.�����</h1>"


@app.route('/image_sample')
def image():
    return f'''<html><body><h1>���������</h1>
    <img src="{
    url_for('static', filename='img/�����.jpg')
    }" alt="����� ������ ���� ���� ��������, �� �� �������"></body><html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)