from flask import Blueprint
from controllers.move import moves
from controllers.video import video
from controllers.battery import battery

api = Blueprint("api", __name__)
api_v1 = Blueprint("v1", __name__)

api_v1.register_blueprint(moves, url_prefix="/moves")
api_v1.register_blueprint(video, url_prefix="/video")
api_v1.register_blueprint(battery, url_prefix="/battery")

api.register_blueprint(api_v1, url_prefix="/v1")
