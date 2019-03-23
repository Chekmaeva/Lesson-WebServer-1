# coding: utf8

from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/yandex_music/')
def bootstrap():
    return '''<!doctype html>
              <html lang="en">
               <head>
              <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Yandex music for your taste!</title>
  </head>
  <body>
    <h1>Welcome!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
    <iframe frameborder="0" style="border:none;width:900px;height:600px;" width="900" height="600" src="https://music.yandex.ru/iframe/#album/6017186/">Слушайте <a href='https://music.yandex.ru/album/6017186'>Imagine Dragons</a> — на Яндекс.Музыке</iframe>
  </body>
</html>'''

@app.route('/list/<int:number>')
def list(number):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Список чисел до текущего введённого</title>
                  </head>
                  <body>
                    <h2>{}</h2>
                  </body>
                  
                </html>'''.format(' '.join(str(i) for i in range(1, number + 1)))


@app.route('/table/<int:m>/<int:n>')
def table(m, n):
    res = []
    for i in range(m):
        res.append("<tr>")
        res.append("".join([f'<td>({i}, {j})</td>' for j in range(n)]))
        res.append("</tr>")
    return f'''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                  integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                  crossorigin="anonymous">
        </head>
        <body>
        <h1>Привет! Вы ввели:</h1>
        <table class="table">
            {''.join(res)}
        </table>
        </body>
        </html>'''

@app.route('/youtube/<int:num>')
def youtube(num):
    li = ["9itwt_opsvQ",
          "04854XqcfCY",
          "NvR60Wg9R7Q",
          "Qq4j1LtCdww",
          "YpJAmlnBxoA"
          ]
    if num < 0 or num > 5:
        return "Введите корректное число"
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Привет! Вы ввели:</h1>
                    <div>
                      {"".join([f"""
                      <iframe width="560" height="315" src="https://www.youtube.com/embed/{li[i]}" 
                      frameborder="0" allow="accelerometer; 
                      encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                      """ for i in range(num)])}
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True, use_reloader=False)