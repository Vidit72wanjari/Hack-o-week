from flask import Flask,render_template,jsonify
import random
from model import load_model

app = Flask(__name__)
model = load_model()


zones = [
    "AI Lab",
    "Networking Lab",
    "Electronics Lab",
    "Library",
    "Seminar Hall"
]


def generate_zone_data():

    zone_predictions = []

    for zone in zones:

        occ = random.randint(5,50)
        indoor = random.uniform(22,30)
        outdoor = random.uniform(28,40)

        prediction = model.predict([[occ,indoor,outdoor]])[0]

        zone_predictions.append({
            "zone":zone,
            "occupancy":occ,
            "indoor":round(indoor,1),
            "outdoor":round(outdoor,1),
            "cooling":round(prediction,2)
        })

    return zone_predictions


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/zone_data")
def zone_data():
    return jsonify(generate_zone_data())


if __name__ == "__main__":
    app.run(debug=True)