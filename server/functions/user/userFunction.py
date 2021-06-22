from flask import Flask, jsonify, request
import config.config  as config
#from server import db
from bson import json_util, ObjectId
import json
db = config.connection().db

def fnUserSearch():
	try:
		x = []
		online_users = db.clUser.find({})
		if(type(online_users) != dict):
				online_users = list(online_users)
		else:
				online_users = [online_users]

		if(len(online_users) > 0):
				for doc in online_users:
						x.append(doc)
				jsonResponse = {
						'intStatus': 200,
						'strMsg': 'información obtenida correctamente.',
						'intCont': len(x),
						'resp': x
				}
				return json.loads(json_util.dumps(jsonResponse))
		else:
				jsonResponse = {
						'intStatus': 404,
						'strMsg': 'No se encontro la información en la base de datos',
						'intCont': 0,
						'resp': []
				}
				return json.loads(json_util.dumps(jsonResponse))

	except Exception as e:
		jsonResponse = {
            'intStatus': 400,
            'strMsg': 'error en el sistema: ' + str(e),
            'intCont': 0,
            'resp': []
        }
		return json.loads(json_util.dumps(jsonResponse))

		
