from flask import Blueprint, Flask, jsonify, request
import functions.user.userFunction  as functions
from bson import json_util, ObjectId
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