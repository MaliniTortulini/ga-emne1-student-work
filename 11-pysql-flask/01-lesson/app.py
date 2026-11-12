# teste om Flask funker
#try:
 #   from flask import Flask
#except ImportError:
 #   print("Failed to import Flask")
#else:
#    print("Flask is ready!")

from flask import Flask, render_template, request
from mysql.connector import Error
from database import get_cities


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
    return render_template("index.html", heading="World exploring Jinja")

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
