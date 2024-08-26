#!/usr/bin/python3
""" make the Blueprint """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """hbnbStatus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_of_stats():
    """the number of stats"""
    from models import storage
    classes = ["Amenity", "BaseModel", "City",
               "Place", "Review" "State", "User"]
    count_dict = {}
    for cls in classes:
        count_dict.update({cls: storage.count(cls)})
    return jsonify(count_dict)
