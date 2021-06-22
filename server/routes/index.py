# Necessary imports
from flask import Blueprint, Flask, jsonify, request
api = Blueprint('/api', __name__)

#Routes imports
import routes.user.userRoute as user

#Paths
api.register_blueprint(user.user, url_prefix='/user')