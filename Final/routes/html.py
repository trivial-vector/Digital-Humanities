from flask import Blueprint, jsonify, render_template

htmlroutes = Blueprint('htmlroutes', __name__)


@htmlroutes.route('/')
def homeroute():
    return render_template("index.html")
