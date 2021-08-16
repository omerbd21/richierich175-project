from flask import Flask, Response
from routes import index, document
from elasticsearch import Elasticsearch


app = Flask(__name__)

with app.app_context():
    es = Elasticsearch()
    
    
app.register_blueprint(index)
app.register_blueprint(document)

@app.route("/")
def index():
    return "Hello to my Elastic app!"

def run():
    app.run(host='0.0.0.0', port=8080)
