from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет, Яндекс! Я - ученик Яндекс.Лицея</h1>"


@app.route('/image_sample')
def image():
    return f'''<html><body><h1>Заголовок</h1>
    <img src="{url_for('static', filename='img/Риана.jpg')}" 
    alt="здесь должна была быть картинка, но не нашлась"></body><html>'''


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                  integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                  crossorigin="anonymous">
            <title>Привет, Яндекс!</title>
        </head>
        <body>
        <nav class="navbar navbar-light bg-light">
            <span class="navbar-brand mb-0 h1">Navbar</span>
        </nav>
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="{url_for('static', filename='img/2.jpg')}" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="https://get-link-youtube.com/wp-content/uploads/2016/12/1481979215_maxresdefault_live.jpg" 
                    class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/3.jpg')}" class="d-block w-100" alt="...">
                </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        <button type="button" class="btn btn-primary">Primary</button>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
                integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
                crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
                integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
                crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js"
                integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp"
                crossorigin="anonymous"></script>
        </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)