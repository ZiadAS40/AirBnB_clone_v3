#!/usr/bin/python3
"""app file"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(code):
    """teardown app context"""
    storage.close()


@app.errorhandler(404)
def handel_not_found(error):
    """handle the error 404 not found"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    """ Main Function """
    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
