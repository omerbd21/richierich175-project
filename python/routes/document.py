from flask import Blueprint, Response, json, request

from crud import get_documents, get_document, post_document, delete_document

document_actions = Blueprint('document_actions', __name__)

@document.route('/document')
def fetch_documents():
    return Response(json.dumps(get_documents()), 200)
  
  
@document.route('/document/<document_name>')
def fetch_document(document_name):
    return Response(json.dumps(get_document(document_name)), 200)
  
  
@document.route('/document',methods = ['POST'])
def create_document():
    response = post_document(request.get_json())
    return Response(json.dumps(response), 200)
  
  
@document.route('/document/<document_name>',methods = ['DELETE'])
def remove_document(document_name):
    return Response(json.dumps(delete_document(document_name)), 200)
