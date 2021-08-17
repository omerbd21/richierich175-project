from elasticsearch import Elasticsearch


def get_documents(index_name):
  res = current_app.es.search(index=index_name, body={"query": {"match_all": {}}})
  return [doc["_source"] for doc in res["hits"]["hits"]]


def get_document(index_name, doc_id):
  res = current_app.es.get(index=index_name, id=doc_id)
  return res["_source"]

def post_document(index_name, doc_id, doc_body):
  res = current_app.es.index(index=index_name, id=doc_id, body=doc_body)
  return res['result']

def delete_document(index_name, doc_id):
  return current_app.es.delete(index=index_name, id=doc_id)
