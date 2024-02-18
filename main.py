from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def second():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promotion():
    pr_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
               'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
               'Присоединяйся!']
    return '</br>'.join(pr_list)

@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='MARS.jpg')}" alt="">\n 
                    <h2></h2> Вот она какая, красная планета
                  </body>
                </html>'''

@app.route('/promotion_image')
def adverb_with_pict():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.jpg')}" alt="">\n 
                    <                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                                        <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                                        <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                                        <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                                       <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''

@app.route('/choice/<planet_name>')
def choose(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <                    <div class="alert alert-light" role="alert">
                      Эта планета близка к земле;
                    </div>
                                        <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                                        <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                                        <div class="alert alert-warning" role="alert">
                      На ней есть большое магнитное поле;
                    </div>
                                           <div class="alert alert-danger" role="alert">
                      Наконец, она просто красивая!
                    </div>
                  </body>
                </html>'''

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choose_2(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h1>
                                        <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {str(level)} этапа опроса
                    </div>
                    <h2>составляет {str(rating)}!</h2>
                                        <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')