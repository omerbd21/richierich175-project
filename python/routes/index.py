from flask import Blueprint, Response, json, request

from crud import get_indices, get_index, post_index, delete_index

# Create the blueprint
index_actions = Blueprint('index_actions', __name__)

# All routes are here, they basically just call the crud functions. Request objects are coming from the actual api request (see from flask import request)
@index.route('/index')
def fetch_indices():
    return Response(json.dumps(get_indices()), 200)
  
  
@index.route('/index/<index_name>')
def fetch_index(index_name):
    return Response(json.dumps(get_index(index_name)), 200)
  
  
@index.route('/index', methods = ['POST'])
def create_index():
    index_name = request.get_json()["name"]
    index_scheme = request.get_json()["scheme"]
    response = post_index(index_name, index_scheme)
    return Response(json.dumps(response), 200)
  
  
@index.route('/index/<index_name>', methods = ['DELETE'])
def remove_index(index_name):
    return Response(json.dumps(delete_index(index_name)), 200)
