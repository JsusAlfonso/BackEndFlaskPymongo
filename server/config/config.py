# mongo.py
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request, url_for

app = Flask(__name__)

def connection(*uri): #connect = connection('url pero en string')

    if uri != ():
        uri = uri[0]
    # mongodb_client = PyMongo(app, uri or "mongodb://localhost:27017/runners", serverSelectionTimeoutMS = 3000)
    app.config["MONGO_URI"] = uri or "mongodb://localhost:27017/runners"
    mongodb_client = PyMongo(app)
    return mongodb_client 

strPort = '5050'
strHost = '0.0.0.0'
