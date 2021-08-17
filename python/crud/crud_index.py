from elasticsearch import Elasticsearch


def get_indices():
  return current_app.es.indices.get_alias("*")


def get_index(index_name):
  index = current_app.es.search(index=index_name, body={"query": {"match_all": {}}})
  return index

def post_index(index_name, index_schema):
  return current_app.es.indices.create(index = index_name, body = index_schema)

def delete_index(index_name):
  return current_app.es.indices.delete(index=index_name, ignore=[400, 404])
