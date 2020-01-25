from flask import Flask, render_template  # подключаем render_template, который включает функции для Jinja
import data

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', tours = data.tours)  # рендерим шаблон, передавая переменные


@app.route("/from/<direction>")
def from_direction(direction):
    return render_template('direction.html', direction=direction)


@app.route("/tours/<tour_id>")
def tours(tour_id):
    return render_template('tour.html', tour=tour_id)


app.run(port=8000)
app.debug(True)

