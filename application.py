from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Long1710@localhost:5432/ORM"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/addNewFlight_s1")
def addNewFlight_s1():
    return render_template("addNewFlight_s1.html")


@app.route("/addNewFlight_result", methods=["POST"])
def addNewFlight_result():
    """add new flight"""

    # Get form information.
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    duration = request.form.get("duration")
    flight = Flight(origin=origin, destination=destination, duration=duration)
    db.session.add(flight)
    db.session.commit()
    return render_template("success_addNewFlight.html")


@app.route("/show_flights")
def show_flights():
    """show_flights"""
    flights = Flight.query.all()
    return render_template("show_flights.html", a=flights)


@app.route("/search_flight")
def search_flight():
    return render_template("search_flight.html")


@app.route("/search_flight_result", methods=["POST"])
def search_flight_result():
    id = int(request.form.get('id'))
    flights = Flight.query.filter_by(id=id).all()
    return render_template("show_flights.html", a=flights)


@app.route("/search_flight_by_id")
def search_flight_by_id():
    return render_template("search_flight_by_id.html")


@app.route("/search_flight_by_id_result", methods=["POST"])
def search_flight_by_id_result():
    id = int(request.form.get('id'))
    flight = Flight.query.get(id)
    return render_template("show_flights_by_id.html", flight=flight)


@app.route("/update_flight")
def update_flight():
    flights = Flight.query.all()
    return render_template("update_flight.html", flights=flights)


@app.route("/update_flight_insert_infor", methods=["POST"])
def update_flight_insert_infor():
    id = request.form.get('id')
    flight = Flight.query.get(id)
    return render_template("update_flight_insert_infor.html", flight=flight)


@app.route("/add_new_passenger")
def add_new_passenger():
    flights = Flight.query.all()
    return render_template("add_new_passenger.html", flights=flights)


@app.route("/add_new_passenger_result", methods=["POST"])
def add_new_passenger_result():
    """add new passenger"""
    # Get form information.
    name = request.form.get('name')
    flight_id = int(request.form.get('flight_id'))
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return "Thêm hành khách mới thành công"
