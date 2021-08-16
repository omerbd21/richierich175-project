from flask import Blueprint, Response, json, request

from crud import get_indices, get_index, put_index, post_index, delete_index

index_actions = Blueprint('index', __name__)

@index.route('/index')
def fetch_indices():
    return Response(json.dumps(get_indices()), 200)
  
  
@index.route('/index/<index_name>')
def fetch_index(index_name):
    return Response(json.dumps(get_index(index_name)), 200)

@index.route('/index')
def update_index(index_name):
    response = put_index(request.get_json())
    return Response(json.dumps(put_index(reponse["name"], response["scheme"])), 200)
  
  
@index.route('/index')
def create_index():
    response = post_index(request.get_json())
    return Response(json.dumps(response), 200)
  
  
@index.route('/names/<index_name>')
def remove_index(index_name):
    return Response(json.dumps(delete_index(index_name)), 200)
