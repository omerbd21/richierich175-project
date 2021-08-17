from flask import Blueprint, Response, json, request

from crud import get_indices, get_index, post_index, delete_index

index_actions = Blueprint('index_actions', __name__)

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
