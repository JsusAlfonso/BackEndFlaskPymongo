from flask import Blueprint, Flask, jsonify, request
import functions.user.userFunction  as functions
from bson import json_util, ObjectId
from models.userModel import userSchema
from libraries.modelsLibrarie import fnModelValidate
import json

user = Blueprint('/user', __name__)

#request.args.get('paramName') #get query info.
#request.headers.get('headerName') #get headers info.
#request.form['bodyName'] #get body info.
#request.files['file'].filename #get file info.
#request.json["parameter"] #get parameter to json info.

@user.route('/',methods=['GET'])
def fnGetInfo():
    try:
        print(request.json)
        jsnResponse = functions.fnUserSearch()
        return jsnResponse
    except Exception as e:
        jsonResponse = {
            'intStatus': 500,
            'strMsg': 'error en el servidor: ' + str(e),
            'intCont': 0,
            'resp': []
        }
        return json.loads(json_util.dumps(jsonResponse))

@user.route('/', methods=['POST'])
def fnInsertInfo():
    try:
        # print(request.form)
        # print(request.files)

        info = fnModelValidate(userSchema, request.form)
        return 'hola'
    except Exception as e:
        jsonResponse = {
            'intStatus': 500,
            'strMsg': 'error en el servidor: ' + str(e),
            'intCont': 0,
            'resp': []
        }
        return json.loads(json_util.dumps(jsonResponse))

@user.route('/', methods=['PUT'])
def fnUpdateUserInfo():
    try:
        print(request.form)
        print(request.args.get)
        return 'hola'
    except Exception as e:
        jsonResponse = {
            'intStatus': 500,
            'strMsg': 'error en el servidor: ' + str(e),
            'intCont': 0,
            'resp': []
        }
        return json.loads(json_util.dumps(jsonResponse))

@user.route('/', methods=['DELETE'])
def fnDeleteUserInfo():
    try:
        print(request.form)
        print(request.args.get)
        return 'hola'
    except Exception as e:
        jsonResponse = {
            'intStatus': 500,
            'strMsg': 'error en el servidor: ' + str(e),
            'intCont': 0,
            'resp': []
        }
        return json.loads(json_util.dumps(jsonResponse))