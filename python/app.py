from flask import Flask, Response
from routes import index_actions, document_actions
from elasticsearch import Elasticsearch

# Creates a flask instance
app = Flask(__name__)


# uses app context to run elasticsearch api in python. this is usable all through api with current_app.es
with app.app_context():
    es = Elasticsearch()
    
# Registring blueprints, which contains all the api routes for each object
app.register_blueprint(index_actions)
app.register_blueprint(document_actions)

# Basic route for index
@app.route("/")
def index():
    return "Welcome to my Elastic app!"

# run the flask app on localhost in 8080
def run():
    app.run(host='0.0.0.0', port=8080)
