from flask import request, Response, json, Blueprint
from controllers.move import moves

api = Blueprint("api", __name__)
api_v1 = Blueprint("v1", __name__)

api_v1.register_blueprint(moves, url_prefix="/moves")

api.register_blueprint(api_v1, url_prefix="/v1")
