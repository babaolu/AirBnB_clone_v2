#!/usr/bin/python3
""" A Flask application """
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception=None):
    """ Cleanup procedures """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def list_states():
    """ Display States and their assoiciate cities """
    state_list = [v for k, v in storage.all("State").items()]
    amenity_list = [v for k, v in storage.all("Amenity").items()]
    place_list = [v for k, v in storage.all("Place").items()]
    return render_template('100-hbnb.html', states=state_list,
                           amenities=amenity_list, places=place_list)


if __name__ == "__main__":
    app.run(debug=True)
