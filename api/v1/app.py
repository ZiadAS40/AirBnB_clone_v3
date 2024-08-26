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
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')), tthreaded=True)
