import flask
import config.config  as config
import datetime
import routes.index as index
from bson import json_util, ObjectId
import json

import sys
import requests
import os

db = config.connection().db
bdOnOff = config.dbOnline(db)
if(bdOnOff['intResp'] == 1):
    print(bdOnOff['strMsg'])
    config.app.register_blueprint(index.api, url_prefix='/api')
else:
    print(bdOnOff['strMsg'])


if __name__ == '__main__':
    config.app.run(host=config.strHost,port=config.strPort,debug=True,threaded=True)