from flask import Flask, Response
from routes import index_actions, document_actions
from elasticsearch import Elasticsearch


app = Flask(__name__)

with app.app_context():
    es = Elasticsearch()
    
    
app.register_blueprint(index_actions)
app.register_blueprint(document_actions)

@app.route("/")
def index():
    return "Welcome to my Elastic app!"

def run():
    app.run(host='0.0.0.0', port=8080)
