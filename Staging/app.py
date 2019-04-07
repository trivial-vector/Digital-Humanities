from routes.api import apiroutes
from routes.html import htmlroutes
from flask import Flask, url_for

app = Flask(__name__)

app.register_blueprint(htmlroutes)
app.register_blueprint(apiroutes, url_prefix="/api")

app.run()
