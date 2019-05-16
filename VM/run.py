# import reservation.utils.cosmos
# from reservation.utils.cosmos import DocumentMgr, CollectionMgr, client
from reservation.routes.cosmosroutes import cosmosroutes
from flask import Flask, url_for, render_template

app = Flask(__name__)

app.register_blueprint(cosmosroutes, url_prefix="/api")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
