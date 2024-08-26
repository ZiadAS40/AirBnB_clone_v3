#!/usr/bin/python3
"""state RESTfull API"""

import models
from flask import abort, jsonify, make_response, request
from models.state import State
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """return all the states"""
    state_objs = models.storage.all(State)
    state_list = [state.to_dict() for state in state_objs.values()]

    return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    """get state with specific id <state_id>"""
    state_objs = models.storage.all(State)

    for state in state_objs.values():
        if state_id == state.id:
            return jsonify(state.to_dict())
    
    abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """delete state based on its id"""
    state_objs = models.storage.all(State)

    for state in state_objs.values():
        if state_id == state.id:
            models.storage.delete(state) 
            models.storage.save() 
            return make_response(jsonify({}), 200)
    
    abort(404)

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """post a new state"""

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """put attrs in state"""
    state = models.storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ig = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for k, v in data.items():
        if k not in ig:
            setattr(state, k, v)
    models.storage.save()
    return make_response(jsonify(state.to_dict()), 200)
