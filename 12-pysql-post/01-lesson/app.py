#teste hvis Flask funker
#try:
 #   from flask import Flask
#except ImportError:
 #   print("Failed to import Flask")
#else:
#    print("Flask is ready!")

from flask import Flask, render_template, request, redirect
from mysql.connector import Error

from database import get_cities
import database


app = Flask(__name__)
# Disable strict slashes (don't care about ending slash or not)
# in all of this app. Meaning http://127.0.0.1:5000/about and http://127.0.0.1:5000/about/
# are seen as being equal
app.url_map.strict_slashes = False

# bare Hello kommer opp
# @app.route("/")
# def index():
   # return "Hello from Flask!"

# nå vises elementene fra html fila
@app.route("/")
def index():
    return render_template("index.html", heading="Lesson 12: World exploring")

@app.route("/about")
def about():
    return render_template("about.html", author="MalinEA")

@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper()
    if (len(code) != 3 or not code.isascii() or not code.isalpha()):
        return "Invalid code", 400
    try:
        rows = get_cities(code)
    except Error:
        app.logger.exception("Database query failed")
        return "Database unavailable", 503
    return render_template("cities.html", code=code, rows=rows)

@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    if city is None:
        return "City not found", 404
    return render_template(
        "city_form.html",
        name=city.name,
        city_id=city.id
    )

@app.route("/add", methods=["GET", "POST"])
def add_city():

    # Uses GET to open input field page:
    if request.method == "GET":
        return render_template("city_form.html", name="", city_id=None)

    # Uses POST to store city data in DB:
    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    database.insert_city(name)
    return redirect("/cities", code=303)


@app.route("/edit/<int:city_id>", methods=["POST"])
def edit_city(city_id):
    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 404
    database.update_city(city_id, name)
    return redirect("/cities", code=303)


@app.route("/delete/<int:city_id>", methods=["POST"])
def remove_city(city_id):
    database.delete_city(city_id)
    return redirect("/cities", 303)

