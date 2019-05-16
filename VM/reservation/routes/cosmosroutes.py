import reservation.utils.cosmos
from reservation.utils.cosmos import DocumentMgr, CollectionMgr, client
from flask import Blueprint, render_template
from flask.json import jsonify

cosmosroutes = Blueprint("cosmosroutes", __name__)


@cosmosroutes.route("/search")
def search():
    json_doc_list = DocumentMgr.ReadMany(client)
    return jsonify(json_doc_list)


@cosmosroutes.route("/maps")
def heat_maps():
    json_doc_list = DocumentMgr.ReadMany(client)
    return jsonify(json_doc_list)


@cosmosroutes.route("/model")
def model():
    json_doc_list = DocumentMgr.ReadMany(client)
    return jsonify(json_doc_list)
