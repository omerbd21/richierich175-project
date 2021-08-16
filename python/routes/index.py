from flask import Blueprint, Response, json, request

from crud import get_indices, get_index, post_index, delete_index

index = Blueprint('index', __name__)

@website.route('/index')
def fetch_indices():
    return Response(json.dumps(get_indices()), 200)
  
  
@website.route('/index/<index_name>')
def fetch_index(index_name):
    return Response(json.dumps(get_index(index_name)), 200)
  
  
@website.route('/index')
def create_index():
    response = post_index(request.get_json())
    return Response(json.dumps(response), 200)
  
  
@website.route('/names/<index_name>')
def remove_index(index_name):
    return Response(json.dumps(delete_index(index_name)), 200)
