from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', 
    title = data.title,
    subtitle = data.subtitle,
    description = data.description,
    departures = data.departures,
    tours = data.tours) 


@app.route("/from/<direction>")
def from_direction(direction):
    direction_tours = dict()
    for tour_id,tour in data.tours.items():
        if tour.get("departure") == direction:
            direction_tours[tour_id] = tour

    direction_tours.values()
    return render_template('direction.html', 
    title = data.title,
    direction = data.departures.get(direction),
    departures = data.departures, 
    tours = direction_tours)


@app.route("/tours/<id>/")
def tours(id):
    tour = data.tours.get(int(id))
    return render_template('tour.html',
    title = data.title,
    departures = data.departures,
    tour = tour)

if __name__ == '__main__':
    app.run(port=8000)

