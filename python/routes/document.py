from flask import Blueprint, Response, json, request

from crud import get_documents, get_document, post_document, delete_document

document_actions = Blueprint('document_actions', __name__)

@document.route('/document/<index_name>')
def fetch_documents(index_name):
    return Response(json.dumps(get_documents(index_name)), 200)
  
  
@document.route('/document/<index_name>/<document_id>')
def fetch_document(index_name, document_id):
    return Response(json.dumps(get_document(index_name, document_id)), 200)
  
  
@document.route('/document',methods = ['POST'])
def create_document():
    index_name = request.get_json()["index"]
    doc_id = request.get_json()["id"]
    doc_body = request.get_json()["body"]
    return Response(json.dumps(post_document(index_name, doc_id, doc_body)), 200)
  
  
@document.route('/document/<index_name>/<doc_id>',methods = ['DELETE'])
def remove_document(index_name, doc_id):
    return Response(json.dumps(delete_document(index_name, doc_id)), 200)
